from datetime import datetime
from pymodbus.client import ModbusSerialClient
import time
import json
import os
from pathlib import Path

# Modbus Initialization
client = ModbusSerialClient(
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

# Constants
SETTINGS_DIR = Path(__file__).parent
SETTINGS_PATH = SETTINGS_DIR / 'settingsData.json'
PROJECT_DIR = Path(__file__).parent
METER_DATA_PATH = PROJECT_DIR / 'meter_data.json'

# Ensure settings and meter data files exist
SETTINGS_PATH.touch(exist_ok=True)
METER_DATA_PATH.touch(exist_ok=True)

# Initialize the settings file if it is empty
if SETTINGS_PATH.stat().st_size == 0:
    with open(SETTINGS_PATH, 'w') as f:
        json.dump({}, f, indent=4)  # Changed to a dictionary instead of a list

# Settings Acquisition
def meter_param():
    sn_val = ''
    manufacturer_val = ''
    model_val = ''
    version_val = ''
    
    if client.connect():
        print("Conexión exitosa")
        try:
            settings = {}

            # Serial Number Acquisition
            sn = client.read_holding_registers(0x1034, 15, 1)
            if not sn.isError():
                for i in sn.registers:
                    sn_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                sn_val = sn_val.replace('\x00', '')
                settings['SN'] = sn_val
                print("SN:", sn_val)
            else:
                print("Error de lectura (SN):", sn)

            # ID Acquisition
            id_reg = client.read_holding_registers(0x1002, 1, 1)
            if not id_reg.isError():
                id_val = id_reg.registers[0]
                settings['ID'] = id_val
                print("ID:", id_val)
            else:
                print("Error de lectura ID")

            # Manufacturer Acquisition
            manufacturer_reg = client.read_holding_registers(0x1004, 15, 1)
            if not manufacturer_reg.isError():
                for i in manufacturer_reg.registers:
                    manufacturer_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                manufacturer_val = manufacturer_val.replace('\x00', '')
                settings['Manufacturer'] = manufacturer_val
                print("Manufacturer:", manufacturer_val)
            else:
                print("Error de lectura Manufacturer:", manufacturer_reg)

            # Model Acquisition
            model_reg = client.read_holding_registers(0x1014, 15, 1)
            if not model_reg.isError():
                for i in model_reg.registers:
                    model_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                model_val = model_val.replace('\x00', '')
                settings['Model'] = model_val
                print("Model:", model_val)
            else:
                print("Error de lectura Model:", model_reg)

            # Version Acquisition
            version_reg = client.read_holding_registers(0x102C, 7, 1)
            if not version_reg.isError():
                for i in version_reg.registers:
                    version_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                version_val = version_val.replace('\x00', '')
                settings['Version'] = version_val
                print("Version:", version_val)
            else:
                print("Error de lectura Version:", version_reg)
               
        except Exception as e:
            print("Exception:", e)
        finally:
            client.close()
            
        # Settings local storage
        with open(SETTINGS_PATH, 'w') as f:
            json.dump(settings, f, indent=4)
    else:
        print("Error de conexión con el medidor")
    return sn_val

def reading_meter():
    data = {}
    if client.connect():
        try:
            # Voltage LN average
            voltage_average_ln_reg = client.read_holding_registers(0x104C, 1, 1)
            if not voltage_average_ln_reg.isError():
                voltage_average_ln_val = voltage_average_ln_reg.registers[0]
                data['voltage_average_LN'] = voltage_average_ln_val
                print("Voltaje LN (V):", voltage_average_ln_val)
            else:
                print("Error de lectura (Voltaje LN):", voltage_average_ln_reg)

            # (Omitido por brevedad: resto de las lecturas y manejo de errores)

            # TimeStamp
            dt = datetime.utcnow()
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
while True: 
    meter_param()
    reading_meter()
    time.sleep(30)
