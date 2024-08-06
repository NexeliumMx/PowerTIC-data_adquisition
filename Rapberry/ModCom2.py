from datetime import datetime
from pymodbus.client import ModbusSerialClient
import time
import json
import os
from pathlib import Path


# Inicializar Modbus
client = ModbusSerialClient(
    method='rtu',
    port='/dev/ttyUSB0',
    baudrate=19200,
    parity='N',
    stopbits=1,
    bytesize=8,
    timeout=5
)

# # ID set
# id_path = db.reference('ID/pasillo')

# Lectura de registros de Power Factor
SN_Val = ''
Manufacturer_Val=''
Model_Val=''
Version_Val=''
#Settings Acquisition
def meterParam():
    while True:
        if client.connect():
            print("Conexión exitosa")
            try:
                settings = {}
                #Serial Number Aquisition
                SN = client.read_holding_registers(0x1034, 15, 1)
                if not SN.isError():
                    for i in SN.registers:
                        SN_Val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                    # Limpiar caracteres nulos
                    SN_Val = SN_Val.replace('\x00', '')
                    settings['SN'] = SN_Val
                    print("SN:", SN_Val)
                    #imprint(SN_Val)
                    #break
                else:
                    print("Error de lectura (SN):", SN)

                #ID acquisition
                ID_Reg=client.read_holding_registers(0x1002, 1, 1)
                if not ID_Reg.isError():
                    ID_Val = ID_Reg.registers[0]
                    settings['ID'] = ID_Val
                    print("ID", ID_Val)
                else:
                    print("Error de lectura ID")
                
                #Manufacturer Acquisition
                Manufacturer_Reg=client.read_holding_registers(0x1004, 15, 1)
                if not Manufacturer_Reg.isError():
                    for i in Manufacturer_Reg.registers:
                        Manufacturer_Val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                    # Limpiar caracteres nulos
                    Manufacturer_Val = Manufacturer_Val.replace('\x00', '')
                    settings['Manufacturer'] = Manufacturer_Val
                    print("Manufacturer:", Manufacturer_Val)
                else:
                    print("Error de lectura Manufacturer", Manufacturer_Reg)

                #Model Acquisition
                Model_Reg=client.read_holding_registers(0x1014, 15, 1)
                if not Model_Reg.isError():
                    for i in Model_Reg.registers:
                        Model_Val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                    # Limpiar caracteres nulos
                    Model_Val = Model_Val.replace('\x00', '')
                    settings['Model'] = Model_Val
                    print("Model:", Model_Val)
                else:
                    print("Error de lectura Model", Model_Reg)
                
                #Version acquisition
                Version_Reg=client.read_holding_registers(0x102C, 7, 1)
                if not Version_Reg.isError():
                    for i in Version_Reg.registers:
                        Version_Val += chr((i & 0b1111111100000000) >> 8) + chr(i & 0b0000000011111111)
                    # Limpiar caracteres nulos
                    Version_Val = Version_Val.replace('\x00', '')
                    settings['Version'] = Version_Val
                    print("Version:", Version_Val)
                    break
                else:
                    print("Error de lectura Version", Version_Reg)
                #"'timestamp_server'": "serverTimestamp()",
                #"location": "San Angel"
                
            except Exception as e:
                print("Exception:", e)
            finally:
                client.close()
                
            # Almacenamiento Local
            SETTINGS_DIR = Path(__file__).parent
            storage_Settings_path = SETTINGS_DIR/'meter_data.json'
            
            # Verificar si el archivo existe
            if not os.path.isfile(storage_Settings_path):
                with open(storage_Settings_path, 'w') as f:
                    json.dump([], f)
            
            # Leer el archivo existente
            with open(storage_Settings_path, 'r') as f:
                file_data = json.load(f)
                
            # Añadir nuevos registros
            file_data.append(settings)
            
<<<<<<< HEAD
            # Escribir de nuevo en el archivo con los datos actualizados
            with open(storage_Settings_path, 'w') as f:
                json.dump(file_data, f, indent=4)
            return SN_Val
        else:
            print("Error de conexión con el medidor")
            return None
=======
        # Almacenamiento Local
        SETTINGS_DIR = Path(__file__).parent
        storage_Settings_path = SETTINGS_DIR/'meterData.json'
        
        # Verificar si el archivo existe
        if not os.path.isfile(storage_Settings_path):
            with open(storage_Settings_path, 'w') as f:
                json.dump([], f)
        
        # Leer el archivo existente
        with open(storage_Settings_path, 'r') as f:
            file_Settings_data = json.load(f)
            
        # Añadir nuevos registros
        file_Settings_data.append(settings)
        
        # Escribir de nuevo en el archivo con los datos actualizados
        with open(storage_Settings_path, 'w') as f:
            json.dump(file_Settings_data, f, indent=4)
    else:
        print("Error de conexión con el medidor")
>>>>>>> 7c231d1def9f5752e016e921bc1615e1e3bfe8b2

#id_path.set(SN1_Val)

def reading_meter():
    data = {}
    if client.connect():
        
        try:
            # Lectura de registros de voltaje LN promedio
            voltage_average_LN_Reg = client.read_holding_registers(0x104C, 1, 1)
            if not voltage_average_LN_Reg.isError():
                voltage_average_LN_Val = voltage_average_LN_Reg.registers[0]
                data['voltage_average_LN'] = voltage_average_LN_Val
                print("Voltaje LN (V)", voltage_average_LN_Val)
            else:
                print("Error de lectura (Voltaje LN)", voltage_average_LN_Reg)
                
            # Lectura de registros de phase_voltage_AN
            phase_voltage_AN_Reg = client.read_holding_registers(0x104D, 1, 1)
            if not phase_voltage_AN_Reg.isError():
                phase_voltage_AN_Val = phase_voltage_AN_Reg.registers[0]
                data['phase_voltage_AN'] = phase_voltage_AN_Val
                print("Voltaje AN (V)", phase_voltage_AN_Val)
            else:
                print("Error de lectura (Voltaje AN)", phase_voltage_AN_Reg)
                
            # Lectura de registros de voltaje phase_voltage_BN
            phase_voltage_BN_Reg = client.read_holding_registers(0x104E, 1, 1)
            if not phase_voltage_BN_Reg.isError():
                phase_voltage_BN_Val = phase_voltage_BN_Reg.registers[0]
                data['phase_voltage_BN'] = phase_voltage_BN_Val
                print("Voltaje BN (V)", phase_voltage_BN_Val)
            else:
                print("Error de lectura (Voltaje BN)", phase_voltage_BN_Reg)
            
            # Lectura de registros de phase_voltage_CN
            phase_voltage_CN_Reg = client.read_holding_registers(0x104F, 1, 1)
            if not phase_voltage_CN_Reg.isError():
                phase_voltage_CN_Val = phase_voltage_CN_Reg.registers[0]
                data['phase_voltage_CN'] = phase_voltage_CN_Val
                print("Voltaje CN (V)", phase_voltage_CN_Val)
            else:
                print("Error de lectura (Voltaje CN)", phase_voltage_CN_Reg)
            
            # Lectura de registros de voltage_average_LL
            voltage_average_LL_Reg = client.read_holding_registers(0x1050, 1, 1)
            if not voltage_average_LL_Reg.isError():
                voltage_average_LL_Val = voltage_average_LL_Reg.registers[0]
                data['voltage_average_LL'] = voltage_average_LL_Val
                print("Voltaje promedio LL (V)", voltage_average_LL_Val)
            else:
                print("Error de lectura (Voltaje promedio LL (V))", voltage_average_LL_Reg)

            # Lectura de registros de phase_voltage_AB
            phase_voltage_AB_Reg = client.read_holding_registers(0x1051, 1, 1)
            if not phase_voltage_AB_Reg.isError():
                phase_voltage_AB_Val = phase_voltage_AB_Reg.registers[0]
                data['phase_voltage_AB'] = phase_voltage_AB_Val
                print("Voltaje AB (V)", phase_voltage_AB_Val)
            else:
                print("Error de lectura (Voltaje AB)", phase_voltage_AB_Reg)
            
            # Lectura de registros de phase_voltage_BC
            phase_voltage_BC_Reg = client.read_holding_registers(0x1052, 1, 1)
            if not phase_voltage_BC_Reg.isError():
                phase_voltage_BC_Val = phase_voltage_BC_Reg.registers[0]
                data['phase_voltage_BC'] = phase_voltage_BC_Val
                print("Voltaje BC (V)", phase_voltage_BC_Val)
            else:
                print("Error de lectura (Voltaje BC)", phase_voltage_BC_Reg)

            # Lectura de registros de phase_voltage_CA
            phase_voltage_CA_Reg = client.read_holding_registers(0x1053, 1, 1)
            if not phase_voltage_CA_Reg.isError():
                phase_voltage_CA_Val = phase_voltage_CA_Reg.registers[0]
                data['phase_voltage_CA'] = phase_voltage_CA_Val
                print("Voltaje CA (V)", phase_voltage_CA_Val)
            else:
                print("Error de lectura (Voltaje CA)", phase_voltage_CA_Reg)

            # Lectura de registros de frequency
            frequency_Reg = client.read_holding_registers(0x1055, 1, 1)
            if not frequency_Reg.isError():
                frequency_Val = frequency_Reg.registers[0]
                data['frequency'] = frequency_Val
                print("frequency (Hz)", frequency_Val)
            else:
                print("Error de lectura (frequency (Hz))", frequency_Reg)

            # Lectura de registros de watts_phase_A
            watts_phase_A_Reg = client.read_holding_registers(0x1058, 1, 1)
            if not watts_phase_A_Reg.isError():
                watts_phase_A_Val = watts_phase_A_Reg.registers[0]
                data['watts_phase_A'] = watts_phase_A_Val
                print("watts_phase_A (W)", watts_phase_A_Val)
            else:
                print("Error de lectura (watts_phase_A (W))", watts_phase_A_Reg)

            # Lectura de registros de watts_phase_B
            watts_phase_B_Reg = client.read_holding_registers(0x1059, 1, 1)
            if not watts_phase_B_Reg.isError():
                watts_phase_B_Val = watts_phase_B_Reg.registers[0]
                data['watts_phase_B'] = watts_phase_B_Val
                print("watts_phase_B (W)", watts_phase_B_Val)
            else:
                print("Error de lectura (watts_phase_B (W))", watts_phase_B_Reg)

            # Lectura de registros de watts_phase_C
            watts_phase_C_Reg = client.read_holding_registers(0x105A, 1, 1)
            if not watts_phase_C_Reg.isError():
                watts_phase_C_Val = watts_phase_C_Reg.registers[0]
                data['watts_phase_C'] = watts_phase_C_Val
                print("watts_phase_C (W)", watts_phase_C_Val)
            else:
                print("Error de lectura (watts_phase_C (W))", watts_phase_C_Reg)

            # Lectura de registros de AC_apparent
            AC_apparent_Reg = client.read_holding_registers(0x105C, 1, 1)
            if not AC_apparent_Reg.isError():
                AC_apparent_Val = AC_apparent_Reg.registers[0]
                data['AC_apparent'] = AC_apparent_Val
                print("AC_apparent (VA)", AC_apparent_Val)
            else:
                print("Error de lectura (AC_apparent (VA))", AC_apparent_Reg)

            # Lectura de registros de VA_phase_A
            VA_phase_A_Reg = client.read_holding_registers(0x105D, 1, 1)
            if not VA_phase_A_Reg.isError():
                VA_phase_A_Val = VA_phase_A_Reg.registers[0]
                data['VA_phase_A'] = VA_phase_A_Val
                print("VA_phase_A (VA)", VA_phase_A_Val)
            else:
                print("Error de lectura (VA_phase_A (VA))", VA_phase_A_Reg)

            # Lectura de registros de VA_phase_B
            VA_phase_B_Reg = client.read_holding_registers(0x105E, 1, 1)
            if not VA_phase_B_Reg.isError():
                VA_phase_B_Val = VA_phase_B_Reg.registers[0]
                data['VA_phase_B'] = VA_phase_B_Val
                print("VA_phase_B (VA)", VA_phase_B_Val)
            else:
                print("Error de lectura (VA_phase_B (VA))", VA_phase_B_Reg)

            # Lectura de registros de VA_phase_C
            VA_phase_C_Reg = client.read_holding_registers(0x105F, 1, 1)
            if not VA_phase_C_Reg.isError():
                VA_phase_C_Val = VA_phase_C_Reg.registers[0]
                data['VA_phase_C'] = VA_phase_C_Val
                print("VA_phase_C (VA)", VA_phase_C_Val)
            else:
                print("Error de lectura (VA_phase_C (VA))", VA_phase_C_Reg)
                
            # Lectura de registros de amps_total
            amps_total_Reg = client.read_holding_registers(0x1047, 1, 1)
            if not amps_total_Reg.isError():
                amps_total_Val = amps_total_Reg.registers[0]
                data['amps_total'] = amps_total_Val
                print("Corriente Total (A):", amps_total_Val)
            else:
                print("Error de lectura (Corriente Total):", amps_total_Reg)
                    
            # Lectura de registros de amps_phase_A
            amps_phase_A_Reg = client.read_holding_registers(0x1048, 1, 1)
            if not amps_phase_A_Reg.isError():
                amps_phase_A_Val = amps_phase_A_Reg.registers[0]
                data['amps_phase_A'] = amps_phase_A_Val
                print("Corriente A (A):", amps_phase_A_Val)
            else:
                print("Error de lectura (Corriente A):", amps_phase_A_Reg)
            
            # Lectura de registros de amps_phase_B
            amps_phase_B_Reg = client.read_holding_registers(0x1049, 1, 1)
            if not amps_phase_B_Reg.isError():
                amps_phase_B_Val = amps_phase_B_Reg.registers[0]
                data['amps_phase_B'] = amps_phase_B_Val
                print("Corriente B (A):", amps_phase_B_Val)
            else:
                print("Error de lectura (Corriente B):", amps_phase_B_Reg)
            
            # Lectura de registros de amps_phase_C
            amps_phase_C_Reg = client.read_holding_registers(0x104A, 1, 1)
            if not amps_phase_C_Reg.isError():
                amps_phase_C_Val = amps_phase_C_Reg.registers[0]
                data['amps_phase_C'] = amps_phase_C_Val
                print("Corriente C (A):", amps_phase_C_Val)
            else:
                print("Error de lectura (Corriente C):", amps_phase_C_Reg)
            
            # Lectura de registros de reactive_power_VAR
            reactive_power_VAR_Reg = client.read_holding_registers(0x1061, 1, 1)
            if not reactive_power_VAR_Reg.isError():
                reactive_power_VAR_Val = reactive_power_VAR_Reg.registers[0]
                data['reactive_power_VAR'] = reactive_power_VAR_Val
                print("VAR (VAR):", reactive_power_VAR_Val)
            else:
                print("Error de lectura (VAR):", reactive_power_VAR_Reg)

            # Lectura de registros de VAR_phase_A
            VAR_phase_A_Reg = client.read_holding_registers(0x1062, 1, 1)
            if not VAR_phase_A_Reg.isError():
                VAR_phase_A_Val = VAR_phase_A_Reg.registers[0]
                data['VAR_phase_A'] = VAR_phase_A_Val
                print("VAR_phase_A (VAR):", VAR_phase_A_Val)
            else:
                print("Error de lectura VAR_phase_A (VAR):", VAR_phase_A_Reg)

            # Lectura de registros de VAR_phase_B
            VAR_phase_B_Reg = client.read_holding_registers(0x1063, 1, 1)
            if not VAR_phase_B_Reg.isError():
                VAR_phase_B_Val = VAR_phase_B_Reg.registers[0]
                data['VAR_phase_B'] = VAR_phase_B_Val
                print("VAR_phase_B (VAR):", VAR_phase_B_Val)
            else:
                print("Error de lectura VAR_phase_B (VAR):", VAR_phase_B_Reg)

            # Lectura de registros de VAR_phase_C
            VAR_phase_C_Reg = client.read_holding_registers(0x1064, 1, 1)
            if not VAR_phase_C_Reg.isError():
                VAR_phase_C_Val = VAR_phase_C_Reg.registers[0]
                data['VAR_phase_C'] = VAR_phase_C_Val
                print("VAR_phase_C (VAR):", VAR_phase_C_Val)
            else:
                print("Error de lectura VAR_phase_C (VAR):", VAR_phase_C_Reg)
                                
            # Lectura de registros de total_real_power
            total_real_power_Reg = client.read_holding_registers(0x1057, 1, 1)
            if not total_real_power_Reg.isError():
                total_real_power_Val = total_real_power_Reg.registers[0]
                data['total_real_power'] = total_real_power_Val
                print("Power (kW):", total_real_power_Val)
            else:
                print("Error de lectura (kW):", total_real_power_Reg)
            
            # Lectura de registros de power_factor
            power_factor_Reg = client.read_holding_registers(0x1066, 1, 1)
            if not power_factor_Reg.isError():
                power_factor_Val = power_factor_Reg.registers[0]
                data['power_factor'] = power_factor_Val
                print("Power Factor (PF):", power_factor_Val)
            else:
                print("Error de lectura (PF):", power_factor_Reg)

            # Lectura de registros de pf_phase_A
            pf_phase_A_Reg = client.read_holding_registers(0x1067, 1, 1)
            if not pf_phase_A_Reg.isError():
                pf_phase_A_Val = pf_phase_A_Reg.registers[0]
                data['pf_phase_A'] = pf_phase_A_Val
                print("pf_phase_A (PF):", pf_phase_A_Val)
            else:
                print("Error de lectura pf_phase_A (PF):", pf_phase_A_Reg)

            # Lectura de registros de pf_phase_B
            pf_phase_B_Reg = client.read_holding_registers(0x1068, 1, 1)
            if not pf_phase_B_Reg.isError():
                pf_phase_B_Val = pf_phase_B_Reg.registers[0]
                data['pf_phase_B'] = pf_phase_B_Val
                print("pf_phase_B (PF):", pf_phase_B_Val)
            else:
                print("Error de lectura pf_phase_B (PF):", pf_phase_B_Reg)

            # Lectura de registros de pf_phase_C
            pf_phase_C_Reg = client.read_holding_registers(0x1069, 1, 1)
            if not pf_phase_C_Reg.isError():
                pf_phase_C_Val = pf_phase_C_Reg.registers[0]
                data['pf_phase_C'] = pf_phase_C_Val
                print("pf_phase_C (PF):", pf_phase_C_Val)
            else:
                print("Error de lectura pf_phase_C (PF):", pf_phase_C_Reg)

            # Lectura de registros de total_real_energy_exported
            total_real_energy_exported_H_Reg = client.read_holding_registers(0x106B, 1, 1)
            total_real_energy_exported_L_Reg = client.read_holding_registers(0x106C, 1, 1)
            if not total_real_energy_exported_L_Reg.isError():
                total_real_energy_exported_H_Val = total_real_energy_exported_H_Reg.registers[0]
                total_real_energy_exported_L_Val = total_real_energy_exported_L_Reg.registers[0]
                data['total_real_energy_exported'] = total_real_energy_exported_H_Val+total_real_energy_exported_L_Val
                print("total_real_energy_exported (Wh):", total_real_energy_exported_H_Val+total_real_energy_exported_L_Val)
            else:
                print("Error de lectura total_real_energy_exported (Wh):", total_real_energy_exported_H_Val+total_real_energy_exported_L_Val)

            # Lectura de registros de total_real_energy_exported_phase_A
            total_real_energy_exported_phase_A_H_Reg = client.read_holding_registers(0x106D, 1, 1)
            total_real_energy_exported_phase_A_L_Reg = client.read_holding_registers(0x106E, 1, 1)
            if not total_real_energy_exported_phase_A_L_Reg.isError():
                total_real_energy_exported_phase_A_H_Val = total_real_energy_exported_phase_A_H_Reg.registers[0]
                total_real_energy_exported_phase_A_L_Val = total_real_energy_exported_phase_A_L_Reg.registers[0]
                data['total_real_energy_exported_phase_A'] = total_real_energy_exported_phase_A_H_Val+total_real_energy_exported_phase_A_L_Val
                print("total_real_energy_exported_phase_A (Wh):", total_real_energy_exported_phase_A_H_Val+total_real_energy_exported_phase_A_L_Val)
            else:
                print("Error de lectura total_real_energy_exported_phase_A (Wh):", total_real_energy_exported_phase_A_H_Val+total_real_energy_exported_phase_A_L_Val)

            # Lectura de registros de total_real_energy_exported_phase_B
            total_real_energy_exported_phase_B_H_Reg = client.read_holding_registers(0x106F, 1, 1)
            total_real_energy_exported_phase_B_L_Reg = client.read_holding_registers(0x1070, 1, 1)
            if not total_real_energy_exported_phase_B_L_Reg.isError():
                total_real_energy_exported_phase_B_H_Val = total_real_energy_exported_phase_B_H_Reg.registers[0]
                total_real_energy_exported_phase_B_L_Val = total_real_energy_exported_phase_B_L_Reg.registers[0]
                data['total_real_energy_exported_phase_B'] = total_real_energy_exported_phase_B_H_Val+total_real_energy_exported_phase_B_L_Val
                print("total_real_energy_exported_phase_B (Wh):", total_real_energy_exported_phase_B_H_Val+total_real_energy_exported_phase_B_L_Val)
            else:
                print("Error de lectura total_real_energy_exported_phase_B (Wh):", total_real_energy_exported_phase_B_H_Val+total_real_energy_exported_phase_B_L_Val)

            # Lectura de registros de total_real_energy_exported_phase_C
            total_real_energy_exported_phase_C_H_Reg = client.read_holding_registers(0x1071, 1, 1)
            total_real_energy_exported_phase_C_L_Reg = client.read_holding_registers(0x1072, 1, 1)
            if not total_real_energy_exported_phase_C_L_Reg.isError():
                total_real_energy_exported_phase_C_H_Val = total_real_energy_exported_phase_C_H_Reg.registers[0]
                total_real_energy_exported_phase_C_L_Val = total_real_energy_exported_phase_C_L_Reg.registers[0]
                data['total_real_energy_exported_phase_C'] = total_real_energy_exported_phase_C_H_Val+total_real_energy_exported_phase_C_L_Val
                print("total_real_energy_exported_phase_C (Wh):", total_real_energy_exported_phase_C_H_Val+total_real_energy_exported_phase_C_L_Val)
            else:
                print("Error de lectura total_real_energy_exported_phase_C (Wh):", total_real_energy_exported_phase_C_H_Val+total_real_energy_exported_phase_C_L_Val)
            
            # Lectura de registros de total_real_energy_imported
            total_real_energy_imported_H_Reg = client.read_holding_registers(0x1073, 1, 1)
            total_real_energy_imported_L_Reg = client.read_holding_registers(0x1074, 1, 1)
            if not total_real_energy_imported_L_Reg.isError():
                total_real_energy_imported_H_Val = total_real_energy_imported_H_Reg.registers[0]
                total_real_energy_imported_L_Val = total_real_energy_imported_L_Reg.registers[0]
                data['total_real_energy_imported'] = total_real_energy_imported_H_Val+total_real_energy_imported_L_Val
                print("total_real_energy_imported (Wh):", total_real_energy_imported_H_Val+total_real_energy_imported_L_Val)
            else:
                print("Error de lectura total_real_energy_imported (Wh):", total_real_energy_imported_H_Val+total_real_energy_imported_L_Val)

            # Lectura de registros de total_real_energy_imported_phase_A
            total_real_energy_imported_phase_A_H_Reg = client.read_holding_registers(0x1075, 1, 1)
            total_real_energy_imported_phase_A_L_Reg = client.read_holding_registers(0x1076, 1, 1)
            if not total_real_energy_imported_phase_A_L_Reg.isError():
                total_real_energy_imported_phase_A_H_Val = total_real_energy_imported_phase_A_H_Reg.registers[0]
                total_real_energy_imported_phase_A_L_Val = total_real_energy_imported_phase_A_L_Reg.registers[0]
                data['total_real_energy_imported_phase_A'] = total_real_energy_imported_phase_A_H_Val+total_real_energy_imported_phase_A_L_Val
                print("total_real_energy_imported_phase_A (Wh):", total_real_energy_imported_phase_A_H_Val+total_real_energy_imported_phase_A_L_Val)
            else:
                print("Error de lectura total_real_energy_imported_phase_A (Wh):", total_real_energy_imported_phase_A_H_Val+total_real_energy_imported_phase_A_L_Val)

            # Lectura de registros de total_real_energy_imported_phase_B
            total_real_energy_imported_phase_B_H_Reg = client.read_holding_registers(0x1077, 1, 1)
            total_real_energy_imported_phase_B_L_Reg = client.read_holding_registers(0x1078, 1, 1)
            if not total_real_energy_imported_phase_B_L_Reg.isError():
                total_real_energy_imported_phase_B_H_Val = total_real_energy_imported_phase_B_H_Reg.registers[0]
                total_real_energy_imported_phase_B_L_Val = total_real_energy_imported_phase_B_L_Reg.registers[0]
                data['total_real_energy_imported_phase_B'] = total_real_energy_imported_phase_B_H_Val+total_real_energy_imported_phase_B_L_Val
                print("total_real_energy_imported_phase_B (Wh):", total_real_energy_imported_phase_B_H_Val+total_real_energy_imported_phase_B_L_Val)
            else:
                print("Error de lectura total_real_energy_imported_phase_B (Wh):", total_real_energy_imported_phase_B_H_Val+total_real_energy_imported_phase_B_L_Val)

            # Lectura de registros de total_real_energy_imported_phase_C
            total_real_energy_imported_phase_C_H_Reg = client.read_holding_registers(0x1079, 1, 1)
            total_real_energy_imported_phase_C_L_Reg = client.read_holding_registers(0x107A, 1, 1)
            if not total_real_energy_imported_phase_C_L_Reg.isError():
                total_real_energy_imported_phase_C_H_Val = total_real_energy_imported_phase_C_H_Reg.registers[0]
                total_real_energy_imported_phase_C_L_Val = total_real_energy_imported_phase_C_L_Reg.registers[0]
                data['total_real_energy_imported_phase_C'] = total_real_energy_imported_phase_C_H_Val+total_real_energy_imported_phase_C_L_Val
                print("total_real_energy_imported_phase_C (Wh):", total_real_energy_imported_phase_C_H_Val+total_real_energy_imported_phase_C_L_Val)
            else:
                print("Error de lectura total_real_energy_imported_phase_C (Wh):", total_real_energy_imported_phase_C_H_Val+total_real_energy_imported_phase_C_L_Val)

            # Lectura de registros de total_VA_hours_exported
            total_VA_hours_exported_H_Reg = client.read_holding_registers(0x107C, 1, 1)
            total_VA_hours_exported_L_Reg = client.read_holding_registers(0x107D, 1, 1)
            if not total_VA_hours_exported_L_Reg.isError():
                total_VA_hours_exported_H_Val = total_VA_hours_exported_H_Reg.registers[0]
                total_VA_hours_exported_L_Val = total_VA_hours_exported_L_Reg.registers[0]
                data['total_VA_hours_exported'] = total_VA_hours_exported_H_Val+total_VA_hours_exported_L_Val
                print("total_VA_hours_exported (VAh):", total_VA_hours_exported_H_Val+total_VA_hours_exported_L_Val)
            else:
                print("Error de lectura total_VA_hours_exported (VAh):", total_VA_hours_exported_H_Val+total_VA_hours_exported_L_Val)
                
            # Lectura de registros de total_VA_hours_exported_phase_A
            total_VA_hours_exported_phase_A_H_Reg = client.read_holding_registers(0x107E, 1, 1)
            total_VA_hours_exported_phase_A_L_Reg = client.read_holding_registers(0x107F, 1, 1)
            if not total_VA_hours_exported_phase_A_L_Reg.isError():
                total_VA_hours_exported_phase_A_H_Val = total_VA_hours_exported_phase_A_H_Reg.registers[0]
                total_VA_hours_exported_phase_A_L_Val = total_VA_hours_exported_phase_A_L_Reg.registers[0]
                data['total_VA_hours_exported_phase_A'] = total_VA_hours_exported_phase_A_H_Val+total_VA_hours_exported_phase_A_L_Val
                print("total_VA_hours_exported_phase_A (VAh):", total_VA_hours_exported_phase_A_H_Val+total_VA_hours_exported_phase_A_L_Val)
            else:
                print("Error de lectura total_VA_hours_exported_phase_A (VAh):", total_VA_hours_exported_phase_A_H_Val+total_VA_hours_exported_phase_A_L_Val)

            # Lectura de registros de total_VA_hours_exported_phase_B
            total_VA_hours_exported_phase_B_H_Reg = client.read_holding_registers(0x1080, 1, 1)
            total_VA_hours_exported_phase_B_L_Reg = client.read_holding_registers(0x1081, 1, 1)
            if not total_VA_hours_exported_phase_B_L_Reg.isError():
                total_VA_hours_exported_phase_B_H_Val = total_VA_hours_exported_phase_B_H_Reg.registers[0]
                total_VA_hours_exported_phase_B_L_Val = total_VA_hours_exported_phase_B_L_Reg.registers[0]
                data['total_VA_hours_exported_phase_B'] = total_VA_hours_exported_phase_B_H_Val+total_VA_hours_exported_phase_B_L_Val
                print("total_VA_hours_exported_phase_B (VAh):", total_VA_hours_exported_phase_B_H_Val+total_VA_hours_exported_phase_B_L_Val)
            else:
                print("Error de lectura total_VA_hours_exported_phase_B (VAh):", total_VA_hours_exported_phase_B_H_Val+total_VA_hours_exported_phase_B_L_Val)

            # Lectura de registros de total_VA_hours_exported_phase_C
            total_VA_hours_exported_phase_C_H_Reg = client.read_holding_registers(0x1082, 1, 1)
            total_VA_hours_exported_phase_C_L_Reg = client.read_holding_registers(0x1083, 1, 1)
            if not total_VA_hours_exported_phase_C_L_Reg.isError():
                total_VA_hours_exported_phase_C_H_Val = total_VA_hours_exported_phase_C_H_Reg.registers[0]
                total_VA_hours_exported_phase_C_L_Val = total_VA_hours_exported_phase_C_L_Reg.registers[0]
                data['total_VA_hours_exported_phase_C'] = total_VA_hours_exported_phase_C_H_Val+total_VA_hours_exported_phase_C_L_Val
                print("total_VA_hours_exported_phase_C (VAh):", total_VA_hours_exported_phase_C_H_Val+total_VA_hours_exported_phase_C_L_Val)
            else:
                print("Error de lectura total_VA_hours_exported_phase_C (VAh):", total_VA_hours_exported_phase_C_H_Val+total_VA_hours_exported_phase_C_L_Val)
                
           # Lectura de registros de total_VA_hours_imported
            total_VA_hours_imported_H_Reg = client.read_holding_registers(0x1084, 1, 1)
            total_VA_hours_imported_L_Reg = client.read_holding_registers(0x1085, 1, 1)
            if not total_VA_hours_imported_L_Reg.isError():
                total_VA_hours_imported_H_Val = total_VA_hours_imported_H_Reg.registers[0]
                total_VA_hours_imported_L_Val = total_VA_hours_imported_L_Reg.registers[0]
                data['total_VA_hours_imported'] = total_VA_hours_imported_H_Val+total_VA_hours_imported_L_Val
                print("total_VA_hours_imported (VAh):", total_VA_hours_imported_H_Val+total_VA_hours_imported_L_Val)
            else:
                print("Error de lectura total_VA_hours_imported (VAh):", total_VA_hours_imported_H_Val+total_VA_hours_imported_L_Val)

            # Lectura de registros de total_VA_hours_imported_phase_A
            total_VA_hours_imported_phase_A_H_Reg = client.read_holding_registers(0x1086, 1, 1)
            total_VA_hours_imported_phase_A_L_Reg = client.read_holding_registers(0x1087, 1, 1)
            if not total_VA_hours_imported_phase_A_L_Reg.isError():
                total_VA_hours_imported_phase_A_H_Val = total_VA_hours_imported_phase_A_H_Reg.registers[0]
                total_VA_hours_imported_phase_A_L_Val = total_VA_hours_imported_phase_A_L_Reg.registers[0]
                data['total_VA_hours_imported_phase_A'] = total_VA_hours_imported_phase_A_H_Val+total_VA_hours_imported_phase_A_L_Val
                print("total_VA_hours_imported_phase_A (VAh):", total_VA_hours_imported_phase_A_H_Val+total_VA_hours_imported_phase_A_L_Val)
            else:
                print("Error de lectura total_VA_hours_imported_phase_A (VAh):", total_VA_hours_imported_phase_A_H_Val+total_VA_hours_imported_phase_A_L_Val)

            # Lectura de registros de total_VA_hours_imported_phase_B
            total_VA_hours_imported_phase_B_H_Reg = client.read_holding_registers(0x1088, 1, 1)
            total_VA_hours_imported_phase_B_L_Reg = client.read_holding_registers(0x1089, 1, 1)
            if not total_VA_hours_imported_phase_B_L_Reg.isError():
                total_VA_hours_imported_phase_B_H_Val = total_VA_hours_imported_phase_B_H_Reg.registers[0]
                total_VA_hours_imported_phase_B_L_Val = total_VA_hours_imported_phase_B_L_Reg.registers[0]
                data['total_VA_hours_imported_phase_B'] = total_VA_hours_imported_phase_B_H_Val+total_VA_hours_imported_phase_B_L_Val
                print("total_VA_hours_imported_phase_B (VAh):", total_VA_hours_imported_phase_B_H_Val+total_VA_hours_imported_phase_B_L_Val)
            else:
                print("Error de lectura total_VA_hours_imported_phase_B (VAh):", total_VA_hours_imported_phase_B_H_Val+total_VA_hours_imported_phase_B_L_Val)

            # Lectura de registros de total_VA_hours_imported_phase_C
            total_VA_hours_imported_phase_C_H_Reg = client.read_holding_registers(0x108A, 1, 1)
            total_VA_hours_imported_phase_C_L_Reg = client.read_holding_registers(0x108B, 1, 1)
            if not total_VA_hours_imported_phase_C_L_Reg.isError():
                total_VA_hours_imported_phase_C_H_Val = total_VA_hours_imported_phase_C_H_Reg.registers[0]
                total_VA_hours_imported_phase_C_L_Val = total_VA_hours_imported_phase_C_L_Reg.registers[0]
                data['total_VA_hours_imported_phase_C'] = total_VA_hours_imported_phase_C_H_Val+total_VA_hours_imported_phase_C_L_Val
                print("total_VA_hours_imported_phase_C (VAh):", total_VA_hours_imported_phase_C_H_Val+total_VA_hours_imported_phase_C_L_Val)
            else:
                print("Error de lectura total_VA_hours_imported_phase_C (VAh):", total_VA_hours_imported_phase_C_H_Val+total_VA_hours_imported_phase_C_L_Val)

            # Lectura de registros de total_VAR_hours_imported_Q1
            total_VAR_hours_imported_Q1_H_Reg = client.read_holding_registers(0x108D, 1, 1)
            total_VAR_hours_imported_Q1_L_Reg = client.read_holding_registers(0x108E, 1, 1)
            if not total_VAR_hours_imported_Q1_L_Reg.isError():
                total_VAR_hours_imported_Q1_H_Val = total_VAR_hours_imported_Q1_H_Reg.registers[0]
                total_VAR_hours_imported_Q1_L_Val = total_VAR_hours_imported_Q1_L_Reg.registers[0]
                data['total_VAR_hours_imported_Q1'] = total_VAR_hours_imported_Q1_H_Val+total_VAR_hours_imported_Q1_L_Val
                print("total_VAR_hours_imported_Q1 (varh):", total_VAR_hours_imported_Q1_H_Val+total_VAR_hours_imported_Q1_L_Val)
            else:
                print("Error de lectura total_VAR_hours_imported_Q1 (varh):", total_VAR_hours_imported_Q1_H_Val+total_VAR_hours_imported_Q1_L_Val)

            # Lectura de registros de total_VAR_hours_imported_Q1_phase_A
            total_VAR_hours_imported_Q1_phase_A_H_Reg = client.read_holding_registers(0x108F, 1, 1)
            total_VAR_hours_imported_Q1_phase_A_L_Reg = client.read_holding_registers(0x1090, 1, 1)
            if not total_VAR_hours_imported_Q1_phase_A_L_Reg.isError():
                total_VAR_hours_imported_Q1_phase_A_H_Val = total_VAR_hours_imported_Q1_phase_A_H_Reg.registers[0]
                total_VAR_hours_imported_Q1_phase_A_L_Val = total_VAR_hours_imported_Q1_phase_A_L_Reg.registers[0]
                data['total_VAR_hours_imported_Q1_phase_A'] = total_VAR_hours_imported_Q1_phase_A_H_Val+total_VAR_hours_imported_Q1_phase_A_L_Val
                print("total_VAR_hours_imported_Q1_phase_A (varh):", total_VAR_hours_imported_Q1_phase_A_H_Val+total_VAR_hours_imported_Q1_phase_A_L_Val)
            else:
                print("Error de lectura total_VAR_hours_imported_Q1_phase_A (varh):", total_VAR_hours_imported_Q1_phase_A_H_Val+total_VAR_hours_imported_Q1_phase_A_L_Val)

            # Lectura de registros de total_VAR_hours_imported_Q1_phase_B
            total_VAR_hours_imported_Q1_phase_B_H_Reg = client.read_holding_registers(0x1091, 1, 1)
            total_VAR_hours_imported_Q1_phase_B_L_Reg = client.read_holding_registers(0x1092, 1, 1)
            if not total_VAR_hours_imported_Q1_phase_B_L_Reg.isError():
                total_VAR_hours_imported_Q1_phase_B_H_Val = total_VAR_hours_imported_Q1_phase_B_H_Reg.registers[0]
                total_VAR_hours_imported_Q1_phase_B_L_Val = total_VAR_hours_imported_Q1_phase_B_L_Reg.registers[0]
                data['total_VAR_hours_imported_Q1_phase_B'] = total_VAR_hours_imported_Q1_phase_B_H_Val+total_VAR_hours_imported_Q1_phase_B_L_Val
                print("total_VAR_hours_imported_Q1_phase_B (varh):", total_VAR_hours_imported_Q1_phase_B_H_Val+total_VAR_hours_imported_Q1_phase_B_L_Val)
            else:
                print("Error de lectura total_VAR_hours_imported_Q1_phase_B (varh):", total_VAR_hours_imported_Q1_phase_B_H_Val+total_VAR_hours_imported_Q1_phase_B_L_Val)
                
            # Lectura de registros de total_VAR_hours_imported_Q1_phase_C
            total_VAR_hours_imported_Q1_phase_C_H_Reg = client.read_holding_registers(0x1093, 1, 1)
            total_VAR_hours_imported_Q1_phase_C_L_Reg = client.read_holding_registers(0x1094, 1, 1)
            if not total_VAR_hours_imported_Q1_phase_C_L_Reg.isError():
                total_VAR_hours_imported_Q1_phase_C_H_Val = total_VAR_hours_imported_Q1_phase_C_H_Reg.registers[0]
                total_VAR_hours_imported_Q1_phase_C_L_Val = total_VAR_hours_imported_Q1_phase_C_L_Reg.registers[0]
                data['total_VAR_hours_imported_Q1_phase_C'] = total_VAR_hours_imported_Q1_phase_C_H_Val+total_VAR_hours_imported_Q1_phase_C_L_Val
                print("total_VAR_hours_imported_Q1_phase_C (varh):", total_VAR_hours_imported_Q1_phase_C_H_Val+total_VAR_hours_imported_Q1_phase_C_L_Val)
            else:
                print("Error de lectura total_VAR_hours_imported_Q1_phase_C (varh):", total_VAR_hours_imported_Q1_phase_C_H_Val+total_VAR_hours_imported_Q1_phase_C_L_Val)

            # TimeStamp
            dt = datetime.utcnow()
            data["timestamp"] = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            print("Timestamp: ", data["timestamp"])
        
        except Exception as e:
            print("Exception:", e)
        finally:
            client.close()
            
        # Almacenamiento Local
        PROJECT_DIR = Path(__file__).parent
        storage_path = PROJECT_DIR/'meter_data.json'
        
        # Verificar si el archivo existe
        if not os.path.isfile(storage_path):
            with open(storage_path, 'w') as f:
                json.dump([], f)
        
        # Leer el archivo existente
        with open(storage_path, 'r') as f:
            file_data = json.load(f)
            
        # Añadir nuevos registros
        file_data.append(data)
        
        # Escribir de nuevo en el archivo con los datos actualizados
        with open(storage_path, 'w') as f:
            json.dump(file_data, f, indent=4)
        #upload(storage_path,SN_Val)
        # # Añadir registros a Firebase DB
        # direction = 'lecturas/' + SN1_Val
        # db_path = db.reference(direction)
        # db_path.push(data)
    
    else:
        print("Error de conexión con el medidor")

# Ejecución del código

