from datetime import datetime
from pymodbus.client import ModbusSerialClient
import time
import json
from pathlib import Path
import csv
import ast
import pytz  # Importar pytz para manejo de zonas horarias
import psycopg2

#PostgreSQL Init
conn = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="postgres",
    password="postgres",  # luis: Tono2002 //Arturo: 2705
    port=5432
)
print('Connected to the database.')

# Inicialización de Modbus
client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

def meter_param(table_name):
    # Constantes
    SETTINGS_DIR = Path(__file__).parent
    SETTINGS_PATH = SETTINGS_DIR / 'settingsData.json'

    # Asegurar que el archivo de configuración existe
    SETTINGS_PATH.touch(exist_ok=True)
    
    # Inicializar el archivo de configuración si está vacío
    if SETTINGS_PATH.stat().st_size == 0:
        with open(SETTINGS_PATH, 'w') as f:
            json.dump({}, f, indent=4)
            
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT parameter_description, modbus_address, register_number FROM {table_name}")
        rows = cursor.fetchall()
        settings = {}  # Inicializar configuración antes del bloque try
    
        if client.connect():
            print("Conexión exitosa")
            try:
                # Adquisición de configuración
                for row in rows:                    
                    #try:
                     #   modbus_addresses = ast.literal_eval(row['modbus_address_DEC'])
                    #except (ValueError, SyntaxError):
                    #    modbus_addresses = int(row['modbus_address_DEC'])                 
                    if isinstance(row[1], list):
                        parameter = row[0]
                        regs = row[2]
                        set_val = ""  # Inicializar set_val para cada parámetro
                        for modbus_address in row[1]:
                            try:
                                
                                result = client.read_holding_registers(modbus_address, 1)
                                if not result.isError():
                                    for i in result.registers:
                                        set_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                                    set_val = set_val.replace('\x00', '')
                                    settings[parameter] = set_val
                                    
                                else:
                                    print(f"Error de lectura ({parameter}):", result)
                            except ValueError:
                                print(f"Invalid address for {parameter}: {modbus_address}")
                                continue
                        print(f"Adquirido valor para {parameter}: {set_val}")
                    else:
                        parameter = row[0]
                        modbus_address = row[1] 
                        regs = row[2]
                        set_val = ""  # Inicializar set_val para cada parámetro
                        # Data acquisition for single address
                        result = client.read_holding_registers(modbus_address, 1)
                        if not result.isError():
                            set_val = result.registers[0]
                            settings[parameter] = set_val
                            print(f"{parameter}: {set_val}")
                        else:
                            print(f"Error de lectura {parameter} en {modbus_address}", result)
                    
            except Exception as e:
                print("Exception:", e)
            finally:
                client.close()
            # Almacenamiento local de configuración
            with open(SETTINGS_PATH, 'w') as f:
                json.dump(settings, f, indent=4)
        else:
            print("Error de conexión con el medidor")
    
    print(settings.get("serial_number", "serial_number not found"))

    return settings.get('serial_number')


def reading_meter(table_name):
    # Constantes
    PROJECT_DIR = Path(__file__).parent
    METER_DATA_PATH = PROJECT_DIR / 'meter_data.json'
    # Asegurar que el archivo de datos del medidor existe
    METER_DATA_PATH.touch(exist_ok=True)
    data = {}

    # Extracting Modbus addresses from the CSV
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT parameter_description, modbus_address, register_number FROM {table_name}")
        rows = cursor.fetchall()
        address = []
        if client.connect():
            try:        
                for row in rows:
                    if isinstance(row[1], list):
                        parameter = row[0]
                        modbus_address = row[1]
                        # Iterate over each address in the list
                        for modbus_address in row[1]:
                            try:
                                # Data acquisition for each address
                                meas = client.read_holding_registers(modbus_address, 1)
                                if not meas.isError():
                                    meas_val = meas.registers[0]
                                    #data[f"{parameter}_{modbus_address}"] = meas_val
                                else:
                                    print(f"Error de lectura {parameter} en {modbus_address}:", meas)
                            except ValueError:
                                print(f"Invalid address for {parameter}: {modbus_address}")
                                continue
                    else:
                        parameter = row[0]
                        modbus_address = row[1]
                        # Data acquisition for a single address
                        meas = client.read_holding_registers(modbus_address, 1)
                        if not meas.isError():
                            meas_val = meas.registers[0]
                            data[parameter] = meas_val
                            print(f"{parameter}: {meas_val}")
                        else:
                            print(f"Error de lectura {parameter} en {modbus_address}", meas)

                # Timestamp
                mexico_city_tz = pytz.timezone('America/Mexico_City')
                dt = datetime.now(mexico_city_tz)
                data["timestamp"] = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                print("Timestamp: ", data["timestamp"])

            except Exception as e:
                print("Exception:", e)
            finally:
                client.close()
                with open(METER_DATA_PATH, 'w') as f:
                    json.dump(data, f, indent=4)
                return METER_DATA_PATH
        else:
            print("Error de conexión con el medidor")

while True:
    meter_param('device_info_addresses')
    reading_meter('readings_addresses')
    time.sleep(30)