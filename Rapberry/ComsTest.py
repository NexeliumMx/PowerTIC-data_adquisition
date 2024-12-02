from pymodbus.client import ModbusSerialClient
import json
import requests
import datetime
from datetime import timezone
import os
import csv

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
def meter_param(model,mbdadd):     

    with open('modbusrtu_commands.csv',newline='') as csvfile:
        rows = csv.DictReader(csvfile) 
        #print(rows)
        table_name = {}
        table_name["table"] = "meters"
        settings = {}
        
        if client.connect():
            print("Conexión exitosa")
            print("rows: ",rows)
            try:
                for row in rows: 
                    print(row)
                    print(row["parameter"],row["modbus_address"])      
                    print(row["setupRead"],type(row["setupRead"]), bool(row["setupRead"]),type(bool(row["setupRead"])) )
                    print("--------------------------------------------------------------------------------")
                    print(row["model"]) 
                    print(model==row["model"])    
                    print('aqui')
                    if model==row["model"]:
                        print('aqui')
                        if row["setupRead"] == "t":
                            setup = True
                        elif row["setupRead"] == "f":
                            setup = False
                        
                        #print(setup, type(setup))
                        if setup == True: 
                            #print("parameter: ", row["parameter_description"] )
                            parameter = row['parameter']
                            #print("Parameter: ",parameter)
                            set_val = ""
                            #print("modbus_address: ", row['modbus_address'],type(row["modbus_address"]))
            
                            modbus_address = row["modbus_address"]
                            #print("modbus_addresses: ", modbus_addresses,type(modbus_addresses))
                            print(row["register_length"])
                            print('aqui')
                            if int(row["register_length"])>1:
                                for i in range(0,int(row["register_length"])):
                                    #print("Modbus Address: ", modbus_address)
                                    
                                    try:
                                        result = client.read_holding_registers(modbus_address+i, mbdadd)
                                        print('aquisetv')
                                        if not result.isError():
                                            
                                            for i in result.registers:
                                                
                                                (set_val) += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                                                
                                            set_val = set_val.replace('\x00', '')
                                            print(set_val)
                                            settings[f'{parameter}'] = set_val  
                                            print('aquisetv')
                                        else:
                                            print(f"Error de lectura ({parameter}):", result)
                                    except ValueError:
                                        print(f"Invalid address for {parameter}: {str(modbus_address)}")
                                        continue
                                print(f"Adquirido valor para {parameter}: {set_val}")
                            else:
                                print('aquielse')
                                print(modbus_address)
                                #print("Integer Modbus Address: ", modbus_address)
                                modbus_address = int(modbus_address)
                                result = client.read_holding_registers(modbus_address, mbdadd)
                                if not result.isError():
                                    set_val = str(result.registers[0])
                                    settings[f"{parameter}"] = set_val
                                    print(f"{parameter}: {set_val}")
                                else:
                                    print(f"Error de lectura {parameter} en {modbus_address}", result)       
            except Exception as e:
                print("Exception:", e)
            finally:
                client.close()
                #Solo para probar sn diferente
                #settings["serial_number"] = "E3T15060694"

                settings["client"] = "not_set"
                settings["branch"] = "not_set"
                settings["location"] = "not_set"
                settings["load_center"] = "not_set"
                settings["facturation_intervalmonths"] = 1
                timestamp = datetime.datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z"
                settings["register_date"] = timestamp

                json_data = [table_name, settings]
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


        else:
            print("Error de conexión con el medidor")

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
                            modbus_address = (row['modbus_address'])
                            registers = int(row["register_length"])
                            print(parameter_description,registers)
                            #debug
                            #print("Modbus Address: ", modbus_address)

                            if registers == 2:
                                address = modbus_address[0]
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
                                address = modbus_address[0]
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
                                    meas = client.read_holding_registers(modbus_address, mbdadd)
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

            timestamp = timestamp_adquisition(sn)
            print("timestamp: ", timestamp)
            measurement["timestamp"] = timestamp
            measurement["serial_number"] = sn
            json_data = [table_name, measurement]
            data = json.dumps(json_data)
            uniquekey=str(timestamp)+str(sn)
            
            # Debug
            print("Table to insert:", table_name)
            print("Obtained measurements:", measurement)
            print("JSON object: ", json_data)
            print("Built JSON: ", data)

            # Send data
            url = "https://powertic-api.azurewebsites.net/api/pushdata"
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
        return None
