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

# Settings Acquisition
def meter_param():
    #Constants
    SETTINGS_DIR = Path(__file__).parent
    SETTINGS_PATH = SETTINGS_DIR / 'settingsData.json'
    #Ensure Settings file exist
    SETTINGS_PATH.touch(exist_ok=True)
    # Initialize the settings file if it is empty
    if SETTINGS_PATH.stat().st_size == 0:
        with open(SETTINGS_PATH, 'w') as f:
            json.dump({}, f, indent=4)  # Changed to a dictionary instead of a list

    #Decode adresses
    address_settings=[0x1034,0x1004,0x1014,0x102C]
    reg_num=[15,15,15,7]
    parameters=['SN','Manufacturer','Model','Version']
    if client.connect():
        print("Conexión exitosa")
        try:
            settings = {}
            #Settings Acquisition
            for k in range(0,len(parameters)):
                set_val = ''
                set = client.read_holding_registers(address_settings[k], reg_num[k], 1)
                if not set.isError():
                    for i in set.registers:
                        set_val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                    set_val = set_val.replace('\x00', '')
                    settings[parameters[k]] = set_val
                    print("acquiered value:", set_val)
                else:
                    print("Error de lectura (SN):", set)

            # ID Acquisition
            id_reg = client.read_holding_registers(0x1002, 1, 1)
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
            
        # Settings local storage
        with open(SETTINGS_PATH, 'w') as f:
            json.dump(settings, f, indent=4)
    else:
        print("Error de conexión con el medidor")
    return set_val

def reading_meter():
    # Constants
    PROJECT_DIR = Path(__file__).parent
    METER_DATA_PATH = PROJECT_DIR / 'meter_data.json'
    # Ensure meter data files exist
    METER_DATA_PATH.touch(exist_ok=True)

    #Meter addresses
    meter_addresses = [0x104C,0x104D,0x104E,0x104F,0x1050,0x1051,0x1052,0x1053,0x1055,0x1058,0x1059,0x105A,0x105C,0x105D,0x105E,0x105F,0x1047,0x1048,0x1049,0x104A,0x1061,0x1062,0x1063,0x1064,0x1057,0x1066,0x1067,0x1068,0x1069,0x106B,0x106D,0x106F,0x1071,0x1073,0x1075,0x1077,0x1079,0x107C,0x107E,0x1080,0x1082,0x1084,0x1086,0x1088,0x108A,0x108D,0x108F,0x1091,0x1093]
    meas_param = ['voltage_average_LN','phase_voltage_AN','phase_voltage_BN','phase_voltage_CN','voltage_average_LL','phase_voltage_AB','phase_voltage_BC','phase_voltage_CA','frequency','watts_phase_A','watts_phase_B','watts_phase_C','AC_Apparent','VA_phase_A','VA_phase_B','VA_phase_C','amps_total','amps_phase_A','amps_phase_B','amps_phase_C','reactive_power_VAR','VAR_phase_A','VAR_phase_B','VAR_phase_C','total_real_power','power_factor','pf_phase_A','pf_phase_B','pf_phase_C','total_real_energy_exported','total_real_energy_exported_phase_A','total_real_energy_exported_phase_B','total_real_energy_exported_phase_C','total_real_energy_imported','total_real_energy_imported_phase_A','total_real_energy_imported_phase_B','total_real_energy_imported_phase_C','total_VA_hours_exported','total_VA_hours_exported_phase_A','total_VA_hours_exported_phase_B','total_VA_hours_exported_phase_C','total_VA_hours_imported','total_VA_hours_imported_phase_A','total_VA_hours_imported_phase_B','total_VA_hours_imported_phase_C','total_VAR_hours_imported_Q1','total_VAR_hours_imported_Q1_phase_A','total_VAR_hours_imported_Q1_phase_B','total_VAR_hours_imported_Q1_phase_C']
    regs=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    print("Corriente por fase: ", meas_param('amps_phase_A'))
    data = {}
    if client.connect():
        try:
            for j in range(0,len(meas_param)):
                meas_val=''
                # Data
                meas = client.read_holding_registers(meter_addresses[j], regs[j], 1)
                if not meas.isError():
                    meas_val = meas.registers[0]
                    data[meas_param[j]] = meas_val
                    print(meas_param[j], meas_val)
                else:
                    print("Error de lectura"+meas_param[j], meas)
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
