import json
import requests
import datetime
from datetime import timezone
import os
import csv
import logging
from decode_modbus import modbus_commands, compute_crc, decode_modbus_response
from modbus16bit import modbus_read, kill_processes
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
    settings = {}
    try:
        #Filter Setup Read rows
        rows, reset_command = modbus_commands(model=model)
        print(rows)
        set_params = []
        for row in rows:
            print("Debug: ", row.get('setup_read'))
            if row.get('setup_read') == 'True':
                set_params.append(row)
                print(set_params)
        
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
                        #print(settings)
                        break
                else:
                    logger.warning(f"No response, retrying ({attempt+1}/{max_retries})")
                    #kill_processes()
            else:
                logger.error("Failed to get response after retries")
                continue

    except Exception as e:
        print("Exception: ", e)
    finally:
        ser.close()
        #settings["facturation_interval_months"] = 1
        timestamp = datetime.datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z"
        settings["register_date"] = timestamp
        settings["facturation_day"]=datetime.datetime.now().day

        json_data = settings
        data = json.dumps(json_data)
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
    
    return settings.get('serial_number')


            


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

def reading_meter(sn:str, mbadd: int, model: str):
    if not ser.is_open:
        ser.open()
    #Read function
    function_code = 0x04

    measurement = {}
    try:
        #Filter Setup Read rows
        rows, reset_command = modbus_commands(model=model)
        #print(rows)
        meas_params = []
        for row in rows:
            if row.get('setup_read') == 'False':
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
                    #kill_processes()
                    continue
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
sn= meter_param(model=model,mbadd=mbadd)

reading_meter(sn=sn,mbadd=mbadd,model=model)