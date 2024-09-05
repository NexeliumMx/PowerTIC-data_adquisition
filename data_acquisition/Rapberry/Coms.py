from datetime import datetime
from pymodbus.client import ModbusSerialClient
import time
import json
from pathlib import Path
import psycopg2
import os
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
serialnumb=''
def meter_param():
    # Constantes
    SETTINGS_DIR = Path(__file__).parent
    tempquery = SETTINGS_DIR / 'tempquery.txt'
            
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT parameter_description, modbus_address, register_number,setup FROM public.modbusqueries")
        rows = cursor.fetchall()
        settings = {}  # Inicializar configuración antes del bloque try
        forquery='('
        forqueryVal='('
        start=True
        if client.connect():
            print("Conexión exitosa")
            try:
                # Adquisición de configuración
                for row in rows:       
                    if row[3]==True: 

                        #Debug
                        #print(row)
                        #print(row[0])
                        #print(row[1])
                        #print(row[1][0])                            
                        
                        if isinstance(row[1][0], list):
                        
                            #Debug
                            #print(row)
                            #print(row[0])
                            #print(row[1])
                            #print(row[1][0]) 
                            parameter = row[0]
                            regs = row[2]
                            set_val = ""  # Inicializar set_val para cada parámetro
                            for modbus_address in row[1][0]:
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
                            if start!=True:
                                    forquery+=","
                                    forqueryVal+=","
                            start=False
                            forquery+=parameter
                            forqueryVal+='\''+str(set_val)+'\''
                        else:
                        
                            #Debug
                            #print(row)
                            #print(row[0])
                            #print(row[1])
                            #print(row[1][0]) 
                            parameter = row[0]
                            modbus_address = row[1][0]
                            regs = row[2]
                            set_val = ""  # Inicializar set_val para cada parámetro
                            # Data acquisition for single address
                            result = client.read_holding_registers(modbus_address, 1)
                            if not result.isError():
                                set_val = result.registers[0]
                                settings[parameter] = set_val
                                print(f"{parameter}: {set_val}")
                                if start!=True:
                                    forquery+=","
                                    forqueryVal+=","
                                start=False
                                forquery+=parameter
                                forqueryVal+='\''+str(set_val)+'\''
                            else:
                                print(f"Error de lectura {parameter} en {modbus_address}", result)       
            except Exception as e:
                print("Exception:", e)
            finally:
                client.close()
            # Almacenamiento local de configuración
            if not os.path.exists(r'vals/temp.txt'):
                f=open(r"vals/temp.txt","x")
            else:
                f=os.remove(r"vals/temp.txt")
                f=open(r"vals/temp.txt","x")
            forquery+=', registeryear,locations_locationid)'
            forqueryVal+=',\''+str(time.ctime(time.time()))+'\',0)'
            print(forquery)
            print(forqueryVal)
            f.write('insert into public.meters '+forquery+'values'+forqueryVal)
        else:
            print("Error de conexión con el medidor")
    
    print(settings.get("serial_number", "serial_number not found"))
    
    return settings.get('serial_number')


def reading_meter(sn):
    # Constantes
    PROJECT_DIR = Path(__file__).parent
    METER_DATA_PATH = PROJECT_DIR / 'meter_data.json'
    # Asegurar que el archivo de datos del medidor existe
    METER_DATA_PATH.touch(exist_ok=True)
    data = {}
    # Extracting Modbus addresses from the CSV
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT parameter_description, modbus_address, register_number,indb FROM public.modbusqueries")
        rows = cursor.fetchall()
        #print(rows)
        address = []
        forquery='('
        forqueryVal='('
        start=True
        if client.connect():
            try:        
                for row in rows:
                    if row[3]==True:
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
                            if start!=True:
                                    forquery+=","
                                    forqueryVal+=","
                            start=False
                            forquery+=parameter
                            forqueryVal+=str(meas_val)
                        else:
                            parameter = row[0]
                            modbus_address = row[1]
                            # Data acquisition for a single address
                            meas = client.read_holding_registers(modbus_address, 1)
                            if not meas.isError():
                                meas_val = meas.registers[0]
                                data[parameter] = meas_val
                                print(f"{parameter}: {meas_val}")
                                if start!=True:
                                    forquery+=","
                                    forqueryVal+=","
                                start=False
                                forquery+=parameter
                                forqueryVal+=str(meas_val)
                            else:
                                print(f"Error de lectura {parameter} en {modbus_address}", meas)
            except Exception as e:
                print("Exception:", e)
            finally:
                client.close()
                forquery+=', Timestamp,serial_number)'
                timestamp=str(time.time())
                forqueryVal+=','+timestamp+',\''+str(sn)+'\')'
                print(forquery)
                print(forqueryVal)
                if not os.path.exists(r'vals/temp.txt'):
                    f=open(r"vals/temp.txt","x")
                else:
                    f=os.remove(r"vals/temp.txt")
                    f=open(r"vals/temp.txt","x")
                f.write('insert into public.measurements '+forquery+' values'+forqueryVal)
            
                return METER_DATA_PATH
            
        else:
            print("Error de conexión con el medidor")

print(meter_param())
print(reading_meter(meter_param()))