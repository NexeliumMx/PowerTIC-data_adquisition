from pymodbus.client import ModbusSerialClient
import json
import requests
import datetime
from datetime import timezone
import os
import csv
import logging
from decode_modbus import modbus_commands, compute_crc, decode_modbus_response
from modbus16bit import modbus_read
import serial

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

ser =  serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0.07)


#Conexión con el medidor mediante modbus
client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

def info_backup(data,file_path):
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if not os.path.exists(file_path):
        # Write the data as a list
        with open(file_path, 'w') as f:
            json.dump([data], f, indent=4)
        print(f"Created {file_path} and backed up info.")
    else:
        # Read existing data
        with open(file_path, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
        # Append new data
        existing_data.append(data)
        # Write back to the file
        with open(file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print(f"Data ({data}) was backed up successfully.")


#obtención y envío de datos de información del medidor

def meter_param(model:str,mbadd:int):
    if not ser.is_open:
        ser.open()
    #Read function
    function_code = 0x04

    table_name = {}
    table_name["table"] = "meters"
    settings = {}
    try:
        #Filter Setup Read rows
        rows, reset_command = modbus_commands(model=model)
        #print(rows)
        set_params = []
        for row in rows:
            if row.get('setupread') == 't':
                set_params.append(row)
        
        #print("setup parameters: ", set_params)

        for address in set_params:
            try:
                parameter = address.get('parameter', 'Unknown')
                logger.info(f"Parameter: {parameter}")
                datatype = address.get("data_type", "raw")
                quantity_of_registers = int(address.get("register_length", "0"), 0)
                modbus_address = eval(address["modbus_address"])
                starting_address = modbus_address[0] if isinstance(modbus_address, list) else modbus_address
            except KeyError as e:
                logger.error(f"Missing key in address: {e}")
                continue
            except ValueError as e:
                logger.error(f"Invalid value in address: {e}")
                continue

            # Build the message
            message = bytearray()
            message.append(mbadd)
            message.append(function_code)
            message.append((starting_address >> 8) & 0xFF)
            message.append(starting_address & 0xFF)
            message.append((quantity_of_registers >> 8) & 0xFF)
            message.append(quantity_of_registers & 0xFF)

            # Compute CRC16 checksum
            crc = compute_crc(message)
            crc_low = crc & 0xFF
            crc_high = (crc >> 8) & 0xFF

            # Append CRC to the message
            message.append(crc_low)
            message.append(crc_high)

            #logger.debug(f"Sent: {message}")

            # Send the message over serial port
            max_retries = 10
            for attempt in range(max_retries):
                ser.write(message)
                response_length = 5 + (quantity_of_registers * 2) + 2
                response = ser.read(response_length)
                if response:
                    #logger.debug(f"Received: {response}")
                    status = decode_modbus_response(response, mbadd, datatype, parameter)
                    if status != "Incorrect CRC":
                        settings[f"{parameter}"] = status
                        print(settings)
                        break
                else:
                    logger.warning(f"No response, retrying ({attempt+1}/{max_retries})")
            else:
                logger.error("Failed to get response after retries")
                continue

    except Exception as e:
        print("Exception: ", e)
    finally:
        ser.close()
        settings["client_id"] = "not_set"
        settings["facturation_interval_months"] = 1
        timestamp = datetime.datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z"
        settings["register_date"] = timestamp
        settings["facturation_day"]=datetime.datetime.now().day

        json_data = settings
        data = json.dumps(json_data)
        print(table_name)
        print(settings)

        print(data)
        print(settings.get("serial_number", "serial_number not found"))
        url = "https://powertick-api-js.azurewebsites.net/api/RegisterNewMeter"
        response = requests.post(url, json=json_data)

        if response.status_code == 200:
            print('Success:')
        else:
            print('Error:', response.status_code, response.text)

            file_path = r"Raspberry_backup/parameters.json"  # Corrected directory name            
            info_backup(data=json_data, file_path=file_path)
    
    return settings.get('serial_number'), table_name.get("table")


            


def timestamp_adquisition(sn,mbdadd,model):
    if client.connect():
        meter_time = {}
        with open('modbusrtu_commands.csv', newline='') as csvfile:
            rows = csv.DictReader(csvfile)

            try:
                for row in rows:
                    if row["timestamp"] == "t":
                        time = True
                    elif row["timestamp"] == "f":
                        time = False

                    if time and row["model"]==model:
                        parameter_description = row['parameter_description']

                        modbus_address = row['modbus_address']
                        registers = int(row['register_length'])
                        value = ''
                        try:
                            meas = client.read_holding_registers(modbus_address, mbdadd)
                            if not meas.isError():
                                value = meas.registers[0]
                                meter_time[f"{parameter_description}"] = value
                                print(f"{parameter_description}: {value}")
                            else:
                                print(f"Error reading {parameter_description} at {modbus_address}: {meas}")
                        except Exception as e:
                            print(f"Invalid address for { parameter_description}: {modbus_address}")
            except Exception as e:
                print("Exception during data acquisition: ", e)
            finally:
                client.close()
                year = meter_time["clock: year"]
                month = meter_time["clock: month"]
                date = meter_time["clock: date"]
                hour = meter_time["clock: hour"]
                minute = meter_time["clock: minute"]
                second = meter_time["clock: second"]
                print(f"{year}-{month}-{date} {hour}:{minute}:{second}Z")
                timestamp = f"{year}-{month}-{date} {hour}:{minute}:{second}Z"
                print(timestamp)
    return timestamp

"""
def reading_meter(sn,mbdadd,model):


    if client.connect():
        # Constants
        measurement = {}
        table_name = {"table": "measurements"}


        with open('modbusrtu_commands.csv', newline='') as csvfile:
            rows = csv.DictReader(csvfile)

            #print("rows: ", rows)
            try:
                for row in rows:

                    if row["indb"] == "t":
                        indb = True
                    elif row["indb"] == "f":
                        indb = False
                    
                    #debug
                    #print("in db: ", indb)
                    if row["model"]==model:
                        if indb:
                            #print("row: ", row)
                            parameter_description = row['parameter']
                            #debug
                            #print("Parameter Description: ", parameter_description)
                            modbus_address = int(row['modbus_address'])
                            registers = int(row["register_length"])
                            print(parameter_description,registers)
                            #debug
                            #print("Modbus Address: ", modbus_address)

                            if registers == 2:
                                address = modbus_address
                                print("Address: ", address)
                                try:
                                    meas_val = ''
                                    meas = client.read_holding_registers(address, int(registers), mbdadd)
                                    if not meas.isError():
                                        high = meas.registers[0]
                                        low = meas.registers[1]
                                        meas_val = (high << 16) + low
                                        print("measurement value: ",meas_val)
                                        measurement[f'{parameter_description}'] = meas_val
                                    else:
                                        print(f"Error reading {parameter_description} at {address}: {meas}")
                                except ValueError:
                                    print(f"Invalid address for {parameter_description}: {modbus_address}")
                                    print("Error value: ", meas_val)   
                            
                            elif registers == 3:
                                address = modbus_address
                                print("Address:", address)
                                try:
                                    result = client.read_holding_registers(address, int(registers), mbdadd)  # adjust address and unit accordingly

                                    if not result.isError():
                                        # Combine the three 16-bit registers into a single 48-bit value
                                        high = result.registers[0]
                                        mid = result.registers[1]
                                        low = result.registers[2]
                                        
                                        # Shift and combine to get 48-bit value
                                        meas_val = (high << 32) + (mid << 16) + low
                                        print(high)
                                        # Extract components from the 48-bit value (YYMMDDhhmmss format)
    #                                    year = (meas_val >> 40) & 0xFF  # last 8 bits for year (YY)
    #                                   month = (meas_val >> 32) & 0xFF  # next 8 bits for month (MM)
    #                                  day = (meas_val >> 24) & 0xFF  # next 8 bits for day (DD)
    ###                               second = meas_val & 0xFF  # last 8 bits for second (ss)

                                        # Convert to string format YYMMDD hh:mm:ss
                                        occur_time = datetime.datetime.fromtimestamp(meas_val,timezone.utc)

                                        print(f"Occur Time: {occur_time}")
                                    else:
                                        print("Error reading Modbus data")
                                except ValueError:
                                    print(f"Invalid address for {parameter_description}: {modbus_address}")
                                    print("Error value: ", meas_val)       
                            else:
                                # 'modbus_address' is a single address
                                meas_val = ''
                                try:
                                    meas = client.read_holding_registers(modbus_address, int(registers),mbdadd)
                                    if not meas.isError():
                                        meas_val = meas.registers[0]
                                        measurement[f"{parameter_description}"] = meas_val
                                        print(f"{parameter_description}: {meas_val}")
                                    else:
                                        print(f"Error reading {parameter_description} at {modbus_address}: {meas}")
                                except ValueError:
                                    print(f"Invalid address for {parameter_description}: {modbus_address}")
            except Exception as e:
                print("Exception during data acquisition:", e)
                print("Error value: ", meas_val)
            finally:
                client.close()

            timestamp =datetime.datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z"
            print("timestamp: ", timestamp)
            measurement["timestamp"] = timestamp
            measurement["serial_number"] = sn
            json_data =  measurement
            data = json.dumps(json_data)
            uniquekey=str(timestamp)+str(sn)
            
            # Debug
            print("Table to insert:", table_name)
            print("Obtained measurements:", measurement)
            print("JSON object: ", json_data)
            print("Built JSON: ", data)

            # Send data
            url = "https://powertick-api-js.azurewebsites.net/api/postReading"
            try:
                response = requests.post(url, json=json_data)
                if response.status_code == 200:
                    print('Success')
                    f=open(rf'vals/success/{uniquekey}.json',"x")
                    f.write(data)
                    
                    f.close()
                else:
                    print('Error:', response.status_code, response.text)
                    f=open(rf'vals/apifail/{uniquekey}.json',"x")
                    f.write(data)
                    
                    f.close()
            except requests.exceptions.RequestException as e:
                print("Network error:", e)
                f=open(rf'vals/nfail/{uniquekey}.json',"x")
                f.write(data) 
                f.close()
                return None
            
            return data  # Return the Python object, not the serialized string
    else:
        print("Error connecting to the meter")
        return None"""

def reading_meter(sn:str, mbadd: int, model: str):
    if not ser.is_open:
        ser.open()
    #Read function
    function_code = 0x04

    measurement = {}
    table_name = {"table": "measurements"}

    try:
        #Filter Setup Read rows
        rows, reset_command = modbus_commands(model=model)
        #print(rows)
        meas_params = []
        for row in rows:
            if row.get('setupread') == 'f':
                meas_params.append(row)
        
        #print("measurement parameters: ", meas_params)
        for address in meas_params:
            try:
                parameter = address.get('parameter', 'Unknown')
                logger.info(f"Parameter: {parameter}")
                datatype = address.get("data_type", "raw")
                quantity_of_registers = int(address.get("register_length", "0"), 0)
                modbus_address = eval(address["modbus_address"])
                starting_address = modbus_address[0] if isinstance(modbus_address, list) else modbus_address
            except KeyError as e:
                logger.error(f"Missing key in address: {e}")
                continue
            except ValueError as e:
                logger.error(f"Invalid value in address: {e}")
                continue

            # Build the message
            message = bytearray()
            message.append(mbadd)
            message.append(function_code)
            message.append((starting_address >> 8) & 0xFF)
            message.append(starting_address & 0xFF)
            message.append((quantity_of_registers >> 8) & 0xFF)
            message.append(quantity_of_registers & 0xFF)

            # Compute CRC16 checksum
            crc = compute_crc(message)
            crc_low = crc & 0xFF
            crc_high = (crc >> 8) & 0xFF

            # Append CRC to the message
            message.append(crc_low)
            message.append(crc_high)

            #logger.debug(f"Sent: {message}")

            # Send the message over serial port
            max_retries = 10
            for attempt in range(max_retries):
                ser.write(message)
                response_length = 5 + (quantity_of_registers * 2) + 2
                response = ser.read(response_length)
                if response:
                    #logger.debug(f"Received: {response}")
                    status = decode_modbus_response(response, mbadd, datatype, parameter)
                    if status != "Incorrect CRC":
                        measurement[f"{parameter}"] = status
                        #print(measurement)
                        break
                else:
                    logger.warning(f"No response, retrying ({attempt+1}/{max_retries})")
            else:
                logger.error("Failed to get response after retries")
                continue
    except Exception as e:
        print("Exception during data acquisition:", e)
    finally:
        ser.close()

        timestamp =datetime.datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z"
        print("timestamp: ", timestamp)
        measurement["timestamp"] = timestamp
        measurement["serial_number"] = sn
        json_data =  measurement
        data = json.dumps(json_data)
        uniquekey=str(timestamp)+str(sn)
        
        # Debug
        print("Table to insert:", table_name)
        print("Obtained measurements:", measurement)
        print("JSON object: ", json_data)
        print("Built JSON: ", data)

        # Send data
        url = "https://powertick-api-js.azurewebsites.net/api/postReading"
        try:
            response = requests.post(url, json=json_data)
            if response.status_code == 200:
                print('Success')
                f=open(rf'vals/success/{uniquekey}.json',"x")
                f.write(data)
                
                f.close()
            else:
                print('Error:', response.status_code, response.text)
                f=open(rf'vals/apifail/{uniquekey}.json',"x")
                f.write(data)
                
                f.close()
        except requests.exceptions.RequestException as e:
            print("Network error:", e)
            f=open(rf'vals/nfail/{uniquekey}.json',"x")
            f.write(data) 
            f.close()
            return None
    
    return data  # Return the Python object, not the serialized string
mbadd = 0x03
model = "EM210-72D.MV5.3.X.OS.X"
sn, table_name = meter_param(model=model,mbadd=mbadd)

reading_meter(sn=sn,mbadd=mbadd,model=model)