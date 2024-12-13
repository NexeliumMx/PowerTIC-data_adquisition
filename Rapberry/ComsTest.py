import json
import requests
from datetime import timezone, datetime
import os
import csv
import logging
from decode_modbus import modbus_commands, compute_crc, decode_modbus_response
from modbus16bit import modbus_read, kill_processes, reset_instruction
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
        #print(rows)
        set_params = []
        for row in rows:
            #print("Debug: ", row.get('setup_read'))
            if row.get('setup_read') == 'True':
                set_params.append(row)
                #print(set_params)
        
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
                        #logger.debug(f"Status: ", status)
                        settings[f"{parameter}"] = status
                        #print(settings)
                        break
                else:
                    logger.warning(f"No response, retrying ({attempt+1}/{max_retries})")
                    kill_processes()
            else:
                logger.error("Failed to get response after retries")
                continue

    except Exception as e:
        print("Exception: ", e)
    finally:
        ser.close()
        #settings["facturation_interval_months"] = 1
        timestamp = datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z"
        settings["register_date"] = timestamp
        #settings["facturation_day"]=datetime.datetime.now().day

        json_data = settings
        del json_data["reset"]
        data = json.dumps(json_data)
        print(settings)

        print(data)
        print(settings.get("serial_number", "serial_number not found"))
        url = "https://powertick-api-js.azurewebsites.net/api/powermeter"
        response = requests.post(url, json=json_data)

        if response.status_code == 200:
            print('Success:')
        else:
            print('Error:', response.status_code, response.text)

            file_path = r"Raspberry_backup/parameters.json"  # Corrected directory name            
            info_backup(data=json_data, file_path=file_path)
    
    return settings.get('serial_number')


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

        timestamp = datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z"
        current_date = datetime.now().strftime("%Y-%m-%d")
        facturation_date(current_date=current_date, mbadd=mbadd, model=model)   

        print("timestamp: ", timestamp)
        measurement["timestamp"] = timestamp
        measurement["serial_number"] = sn
        json_data =  measurement
        data = json.dumps(json_data)
        uniquekey=str(timestamp)+str(sn)
        
        #print("Obtained measurements:", measurement)
        #print("JSON object: ", json_data)
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

def facturation_date(current_date: str, mbadd: int, model: str):
    f_date_file = './facturation_date.txt'

    if not os.path.exists(f_date_file):
        url = "https://powertick-api-js.azurewebsites.net/api/nextFacturationDay"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            print('Success:', response.status_code, response.text)
            date = response.json()
            f_date = date["nextFacturationDay"]
            print("API date:", f_date, type(f_date))
        
        except requests.RequestException as e:
            print('Error during API call:', e)
            return

        with open(f_date_file, "w") as file:
            file.write(f_date)

        print(f"{f_date_file} created with current date: {f_date}")

    else:
        with open(f_date_file, "r") as file:
            stored_date = file.read().strip()  # Strip extra whitespace or newlines

        print("Current date:", current_date, type(current_date))
        print("Stored date:", stored_date, type(stored_date))

        # Convert dates to datetime objects for accurate comparison
        current_date_dt = datetime.strptime(current_date, "%Y-%m-%d")
        stored_date_dt = datetime.strptime(stored_date, "%Y-%m-%d")

        if current_date_dt >= stored_date_dt:
            url = "https://powertick-api-js.azurewebsites.net/api/nextFacturationDay"
            
            try:
                response = requests.get(url)
                response.raise_for_status()
                print('Success:', response.status_code, response.text)
                date = response.json()
                f_date = date["nextFacturationDay"]
                print("API date:", f_date, type(f_date))
            
            except requests.RequestException as e:
                print('Error during API call:', e)
                return

            with open(f_date_file, "w") as file:
                file.write(f_date)


            reset_instruction(slave_address=mbadd, model=model)
            print(f"Updated ated with current date: {f_date}")


mbadd = 0x03
model = "EM210-72D.MV5.3.X.OS.X" #EM210-72D.MV5.3.X.OS.X  |  acurev-1313-5a-x0

sn= meter_param(model=model,mbadd=mbadd)
reading_meter(sn=sn,mbadd=mbadd,model=model)


