from datetime import datetime
from pymodbus.client import ModbusSerialClient
import time
import json
from pathlib import Path
import csv
import ast
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
            
    with open(r'Rapberry/CSV_tests/meter_config_info_address.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        settings = {}  # Inicializar configuración antes del bloque try
    
        if client.connect():
            print("Conexión exitosa")
            try:
                # Adquisición de configuración
                for row in reader:
                    parameter = row['parameter_description']
                    regs = len(modbus_addresses)
                    try:
                        modbus_addresses = ast.literal_eval(row['modbus_address_DEC'])
                    except (ValueError, SyntaxError):
                        modbus_addresses = int(row['modbus_address_DEC'])
                    
                    if isinstance(modbus_addresses, list):
                        for modbus_address in modbus_addresses:
                            try:

                                result = client.read_holding_registers(modbus_address, regs)
                                if not result.isError():
                                    for i in result.registers:
                                        set_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                                    set_val = set_val.replace('\x00', '')
                                    settings[parameter] = set_val
                                    print("Adquirido valor:", set_val)
                                else:
                                    print(f"Error de lectura ({parameter}):", result)
                            except ValueError:
                                print(f"Invalid address for {parameter}: {modbus_address}:")
                                continue
                    else:
                        #Data acquisition for single address
                        result = client.read_holding_registers(modbus_addresses,1)
                        if not result.isError():
                            set_val = result.registers[0]
                            settings[parameter] = set_val
                            print(f"{parameter}:{set_val}")
                        else:
                            print(f"Error de lectura {parameter} en {modbus_addresses}", result)
    
            except Exception as e:
                print("Exception:", e)
            finally:
                client.close()
                
            # Almacenamiento local de configuración
            with open(SETTINGS_PATH, 'w') as f:
                json.dump(settings, f, indent=4)
        else:
            print("Error de conexión con el medidor")
    return settings.get('SN')


def reading_meter():
    # Constantes
    PROJECT_DIR = Path(__file__).parent
    METER_DATA_PATH = PROJECT_DIR / 'meter_data.json'
    # Asegurar que el archivo de datos del medidor existe
    METER_DATA_PATH.touch(exist_ok=True)
    data = {}

    # Extracting Modbus addresses from the CSV
    with open(r'Rapberry/CSV_tests/measurement_address.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        address = []
        if client.connect():
            try:        
                for row in reader:
                    parameter = row['parameter_description']
                    
                    # Convert the string to a list of integers or a single integer
                    try:
                        modbus_addresses = ast.literal_eval(row['modbus_address_DEC'])
                    except (ValueError, SyntaxError):
                        modbus_addresses = int(row['modbus_address_DEC'])

                    if isinstance(modbus_addresses, list):
                        # Iterate over each address in the list
                        for modbus_address in modbus_addresses:
                            try:
                                # Data acquisition for each address
                                meas = client.read_holding_registers(modbus_address, 1)
                                if not meas.isError():
                                    meas_val = meas.registers[0]
                                    data[f"{parameter}_{modbus_address}"] = meas_val
                  #                  print(f"{parameter}_{modbus_address}: {meas_val}")
                                else:
                                    print(f"Error de lectura {parameter} en {modbus_address}:", meas)
                            except ValueError:
                                print(f"Invalid address for {parameter}: {modbus_address}")
                                continue
                 #       print(f"Número de elementos en la lista: {len(modbus_addresses)}")
                    else:
                        # Data acquisition for a single address
                        meas = client.read_holding_registers(modbus_addresses, 1)
                        if not meas.isError():
                            meas_val = meas.registers[0]
                            data[parameter] = meas_val
                            print(f"{parameter}: {meas_val}")
                        else:
                            print(f"Error de lectura {parameter} en {modbus_addresses}", meas)
                    
                    # Append the address to the list
                    address.append(modbus_addresses)
                #    print(f"Dirección: {modbus_addresses}, Parámetro: {parameter}")
                        
                # Print the complete list of addresses
               # print("Lista completa de direcciones:", address)

                # Timestamp
                mexico_city_tz = pytz.timezone('America/Mexico_City')
                dt = datetime.now(mexico_city_tz)
                data["timestamp"] = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                print("Timestamp: ", data["timestamp"])

            except Exception as e:
                print("Exception: ", e)
            finally:
                client.close()
                with open(METER_DATA_PATH, 'w') as f:
                    json.dump(data, f, indent=4)
                return METER_DATA_PATH
        else:
            print("Error de conexión con el medidor")

# Ejecución del código

while True: 
    meter_param()
    reading_meter()
    time.sleep(30)
