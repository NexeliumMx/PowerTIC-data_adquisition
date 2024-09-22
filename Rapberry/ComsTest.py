from pymodbus.client import ModbusSerialClient
import psycopg2
import json
import requests
import datetime
from datetime import timezone
#conxión con el servidor local de postgres
conn = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="postgres",
    password="postgres",
    port=5432
)
print('Connected to the database.')

#Conexión con el medidor mediante modbus
client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

#obtención y envío de datos de información del medidor
def meter_param():      
    with conn.cursor() as cursor:
        cursor.execute("SELECT parameter_description, modbus_address, register_number, setup FROM powertic.modbusqueries")
        rows = cursor.fetchall()
        table_name = {}
        table_name["table"] = "meters"
        settings = {}
        
        if client.connect():
            print("Conexión exitosa")
            try:
                for row in rows:       
                    if row[3]: 
                        parameter = row[0]
                        set_val = ""
                        
                        if isinstance(row[1][0], list):
                            for modbus_address in row[1][0]:
                                try:
                                    result = client.read_holding_registers(modbus_address, 1)
                                    if not result.isError():
                                        for i in result.registers:
                                            set_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                                        set_val = set_val.replace('\x00', '')
                                        settings[f'{parameter}'] = set_val  
                                    else:
                                        print(f"Error de lectura ({parameter}):", result)
                                except ValueError:
                                    print(f"Invalid address for {parameter}: {modbus_address}")
                                    continue
                            print(f"Adquirido valor para {parameter}: {set_val}")
                        else:
                            modbus_address = row[1][0]
                            result = client.read_holding_registers(modbus_address, 1)
                            if not result.isError():
                                set_val = result.registers[0]
                                settings[f"{parameter}"] = set_val
                                print(f"{parameter}: {set_val}")
                            else:
                                print(f"Error de lectura {parameter} en {modbus_address}", result)       
            except Exception as e:
                print("Exception:", e)
            finally:
                client.close()
                json_data = [table_name, settings]
                data = json.dumps(json_data)
                url = "https://powertic-apis-js.azurewebsites.net/api/sql_manager"
                response = requests.post(url, json=data)

                if response.status_code == 200:
                    print('Success:')
                else:
                    print('Error:', response.status_code, response.text)
        else:
            print("Error de conexión con el medidor")
    print(table_name)
    print(settings)

    print(data)
    print(settings.get("serial_number", "serial_number not found"))
    return settings.get('serial_number')

def reading_meter(sn):
    # Constants
    measurement = {}
    table_name = {"table": "measurements"}

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT parameter_description, modbus_address, register_number, indb FROM powertic.modbusqueries")
            rows = cursor.fetchall()
    except Exception as e:
        print("Database error:", e)
        return None

    if client.connect():
        try:
            for row in rows:
                parameter_description = row[0]
                modbus_address = row[1]
                indb = row[3]

                if indb:
                    if isinstance(modbus_address, list):
                        # 'modbus_address' is a list
                        for address in modbus_address:
                            try:
                                # Data acquisition for each address
                                meas = client.read_holding_registers(address, 1)
                                if not meas.isError():
                                    meas_val = meas.registers[0]
                                    measurement[parameter_description] = meas_val
                                else:
                                    print(f"Error reading {parameter_description} at {address}: {meas}")
                            except ValueError:
                                print(f"Invalid address for {parameter_description}: {address}")
                    else:
                        # 'modbus_address' is a single address
                        try:
                            meas = client.read_holding_registers(modbus_address, 1)
                            if not meas.isError():
                                meas_val = meas.registers[0]
                                measurement[parameter_description] = meas_val
                                print(f"{parameter_description}: {meas_val}")
                            else:
                                print(f"Error reading {parameter_description} at {modbus_address}: {meas}")
                        except ValueError:
                            print(f"Invalid address for {parameter_description}: {modbus_address}")
        except Exception as e:
            print("Exception during data acquisition:", e)
        finally:
            client.close()

        timestamp = datetime.datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z"
        measurement["timestamp"] = timestamp
        measurement["serial_number"] = sn
        data = [table_name, measurement]

        # Debug
        print("Table to insert:", table_name)
        print("Obtained measurements:", measurement)
        print("Built JSON: ", data)

        # Send data
        url = "https://powertic-apis-js.azurewebsites.net/api/sql_manager"
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print('Success')
            else:
                print('Error:', response.status_code, response.text)
        except requests.exceptions.RequestException as e:
            print("Network error:", e)
            return None

        return data  # Return the Python object, not the serialized string
    else:
        print("Error connecting to the meter")
        return None
#debug
#print(reading_meter())

reading_meter("E3T15060693")
#meter_param()
