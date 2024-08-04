from datetime import datetime
from pymodbus.client import ModbusSerialClient
import time
import json
import os
import firebase_admin
from firebase_admin import credentials, db

# Configuración de Firebase
access = credentials.Certificate('/home/pi/Desktop/COMS/project-mtpower-firebase-adminsdk-qrhzl-3ea32a0cc0.json')
firebase_admin.initialize_app(access, {
    'databaseURL': 'https://project-mtpower-default-rtdb.firebaseio.com/'
})

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
#id set
id_path = db.reference('ID/pasillo')
# Lectura de registros de Power Factor
while(1):
    SN1_Val=''
    if client.connect():
        SN1 = client.read_holding_registers(0x1034, 15, 1)
        if not SN1.isError():
            for i in SN1.registers:
                SN1_Val += chr((i&0b1111111100000000)>>8)+chr(i&0b0000000011111111)
            print("SN:", SN1_Val)
            break
        else:
   	 	    print("Error de lectura (SN):", SN1)
	 
id_path.set(SN1_Val)

def reading_meter():
    data = {}
    if client.connect():
        print("Conexión exitosa")
        
        try:
            # Lectura de registros de voltaje AN
            VAN_Reg = client.read_holding_registers(0x104D, 1, 1)
            if not VAN_Reg.isError():
                VAN_Val = VAN_Reg.registers[0]
                data['Voltage AN'] = VAN_Val
                print("Voltaje AN (V)", VAN_Val)
            else:
                print("Error de lectura (Voltaje AN)", VAN_Reg)
            
            # Lectura de registros de voltaje BN
            VBN_Reg = client.read_holding_registers(0x104E, 1, 1)
            if not VBN_Reg.isError():
                VBN_Val = VBN_Reg.registers[0]
                data['Voltage BN'] = VBN_Val
                print("Voltaje BN (V)", VBN_Val)
            else:
                print("Error de lectura (Voltaje BN)", VBN_Reg)
            
            # Lectura de registros de voltaje CN
            VCN_Reg = client.read_holding_registers(0x104F, 1, 1)
            if not VCN_Reg.isError():
                VCN_Val = VCN_Reg.registers[0]
                data['Voltage CN'] = VCN_Val
                print("Voltaje CN (V)", VCN_Val)
            else:
                print("Error de lectura (Voltaje CN)", VCN_Reg)
                
            # Lectura de registros de corriente A
            AA_Reg = client.read_holding_registers(0x1048, 1, 1)
            if not AA_Reg.isError():
                AA_Val = AA_Reg.registers[0]
                data['Current A'] = AA_Val
                print("Corriente A (A):", AA_Val)
            else:
                print("Error de lectura (Corriente A):", AA_Reg)
            
            # Lectura de registros de corriente B
            AB_Reg = client.read_holding_registers(0x1049, 1, 1)
            if not AB_Reg.isError():
                AB_Val = AB_Reg.registers[0]
                data['Current B'] = AB_Val
                print("Corriente B (A):", AB_Val)
            else:
                print("Error de lectura (Corriente B):", AB_Reg)
            
            # Lectura de registros de corriente C
            AC_Reg = client.read_holding_registers(0x104A, 1, 1)
            if not AC_Reg.isError():
                AC_Val = AC_Reg.registers[0]
                data['Current C'] = AC_Val
                print("Corriente C (A):", AC_Val)
            else:
                print("Error de lectura (Corriente C):", AC_Reg)
            
            # Lectura de registros de VAR
            VAR_Reg = client.read_holding_registers(0x1060, 1, 1)
            if not VAR_Reg.isError():
                VAR_Val = VAR_Reg.registers[0]
                data['VAR'] = VAR_Val
                print("VAR (VAR):", VAR_Val)
            else:
                print("Error de lectura (VAR):", VAR_Reg)
                
            # Lectura de registros de Total kW
            kW_Reg = client.read_holding_registers(0x1057, 1, 1)
            if not kW_Reg.isError():
                kW_Val = kW_Reg.registers[0]
                data['Power'] = kW_Val
                print("Power (kW):", kW_Val)
            else:
                print("Error de lectura (kW):", kW_Reg)
            
            # Lectura de registros de Power Factor
            PF_Reg = client.read_holding_registers(0x1066, 1, 1)
            if not PF_Reg.isError():
                PF_Val = PF_Reg.registers[0]
                data['PF'] = PF_Val
                print("Power Factor (PF):", PF_Val)
            else:
                print("Error de lectura (PF):", PF_Reg)
		
            # TimeStamp
            dt = datetime.now()
            data["Time"] = dt.strftime("%H:%M:%S")
            data["Date"] = dt.strftime("%Y-%m-%d")
            print("Date: ", dt.date())
            print("Time: ", dt.time())
		
        except Exception as e:
            print("Exception:", e)
        finally:
            client.close()
            
        # Almacenamiento Local
        storage_path = '/home/pi/Desktop/Data_Storage/meter_data.json'
        
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
            
        # Añadir registros a Firebase DB
        direction= 'lecturas/'+SN1_Val
        db_path = db.reference('lecturas/%s',str(SN1_Val))
        db_path.push(data)

    
    else:
        print("Error de conexión con el medidor")

# Ejecución del código
while True:
    reading_meter()
    time.sleep(300)  # Ejecutar cada 5 minutos
