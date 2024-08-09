from datetime import datetime
from pymodbus.client import ModbusSerialClient
import time
import json
import os
from pathlib import Path
import re
import pytz  # Importar pytz para manejo de zonas horarias

# Inicialización de Modbus
client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

def meter_param():
    # Constantes
    SETTINGS_DIR = Path(__file__).parent
    SETTINGS_PATH = SETTINGS_DIR / 'settingsData.json'

    # Asegurar que el archivo de configuración existe
    SETTINGS_PATH.touch(exist_ok=True)
    
    # Inicializar el archivo de configuración si está vacío
    if SETTINGS_PATH.stat().st_size == 0:
        with open(SETTINGS_PATH, 'w') as f:
            json.dump({}, f, indent=4)

    # Decodificar direcciones
    address_settings = [0x1034, 0x1004, 0x1014, 0x102C]
    reg_num = [15, 15, 15, 7]
    parameters = ['SN', 'Manufacturer', 'Model', 'Version']
    
    settings = {}  # Inicializar configuración antes del bloque try
    
    if client.connect():
        print("Conexión exitosa")
        try:
            # Adquisición de configuración
            for k in range(len(parameters)):
                set_val = ''
                result = client.read_holding_registers(address_settings[k], reg_num[k])
                if not result.isError():
                    for i in result.registers:
                        set_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                    set_val = set_val.replace('\x00', '')
                    settings[parameters[k]] = set_val
                    print("Adquirido valor:", set_val)
                else:
                    print(f"Error de lectura ({parameters[k]}):", result)

            # Adquisición de ID
            id_reg = client.read_holding_registers(0x1002, 1)
            if not id_reg.isError():
                id_val = id_reg.registers[0]
                settings['ID'] = id_val
                print("ID:", id_val)
            else:
                print("Error de lectura ID")
   
        except Exception as e:
            print("Exception:", e)
        finally:
            client.close()
            
        # Almacenamiento local de configuración
        with open(SETTINGS_PATH, 'w') as f:
            json.dump(settings, f, indent=4)
    else:
        print("Error de conexión con el medidor")
    return settings['SN']

def extract_sql():
    # Cargar el contenido del archivo SQL
    file_path = '/home/power-tic/MICO/PowerTIC/Rapberry/measurement_address.sql'

    with open(file_path, 'r') as file:
        sql_content = file.read()

    # Extraer datos de las sentencias INSERT INTO
    insert_statements = re.findall(
        r"INSERT INTO measurements_address \((.*?)\) VALUES \((.*?)\);",
        sql_content,
        re.DOTALL
    )

    # Extraer nombres de columnas
    columns = [col.strip() for col in insert_statements[0][0].split(',')]

    # Extraer filas de datos
    data = []
    for statement in insert_statements:
        values = re.findall(r"'(?:[^'\\]|\\.)*'|[^,]+", statement[1])
        values = [val.strip().strip("'") for val in values]
        if len(values) == len(columns):
            data.append(values)

    # Convertir datos a una lista de diccionarios
    data_dicts = [dict(zip(columns, row)) for row in data]

    # Crear un diccionario que mapea cada parameter_description a su correspondiente modbus_address_dec
    parameter_to_address = {}
    for row in data_dicts:
        address_dec = row['modbus_address_hex']
        if address_dec and address_dec.endswith('H'):
            try:
                address = int(address_dec[:-1], 16)
                parameter_to_address[row['parameter_description']] = address
            except ValueError:
                print(f"Skipping invalid address: {address_dec}")

    # Imprimir el diccionario resultante
    for parameter, address in parameter_to_address.items():
        print(f"{parameter}: {address}")

    return parameter_to_address

def reading_meter():
    # Constantes
    parameter_to_address=extract_sql()
    PROJECT_DIR = Path(__file__).parent
    METER_DATA_PATH = PROJECT_DIR / 'meter_data.json'
    # Asegurar que el archivo de datos del medidor existe
    METER_DATA_PATH.touch(exist_ok=True)

    data = {}
    if client.connect():
        try:
            for parameter, address in parameter_to_address.items():
                meas_val = ''
                try:
                    address_int = int(address)
                except ValueError:
                    print(f"Invalid address for {parameter}: {address}")
                    continue
                # Datos
                meas = client.read_holding_registers(address_int, 1)
                if not meas.isError():
                    meas_val = meas.registers[0]
                    data[parameter] = meas_val
                    print(parameter, meas_val)
                else:
                    print(f"Error de lectura {parameter}:", meas)
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

# Ejecución del código

