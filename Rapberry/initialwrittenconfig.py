from modbus16bit import write_modbus
import json
import csv
def initialconfig(model):
    with open('Modbusqueries.csv',newline='') as csvfile:
        rows = csv.DictReader(csvfile) 
        #print(rows)
        table_name = {}
        table_name["table"] = "meters"
        settings = {}
        print("rows: ",rows)
        try:
            for row in rows: 
                print(row)
                print(row["parameter_description"],row["modbus_address"])      
                print(row["setup"],type(row["setup"]), bool(row["setup"]),type(bool(row["setup"])) )
                print("--------------------------------------------------------------------------------")
                print(row["model"]) 
                print(model==row["model"])    
                if True:
                    if row["setup"] == "t":
                        setup = True
                    elif row["setup"] == "f":
                        setup = False
                    
                    
                    if setup == True: 
                        
                        parameter = row['parameter_description']
                        
                        set_val = ""
                        
                        modbus_addresses = json.loads(row["modbus_address"])[0]
                        if isinstance(modbus_addresses, list):
                            for modbus_address in modbus_addresses:
                                
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
                            #print("Integer Modbus Address: ", modbus_address)
                            modbus_address = modbus_addresses
                            result = client.read_holding_registers(modbus_address, 1)
                            if not result.isError():
                                set_val = result.registers[0]
                                settings[f"{parameter}"] = set_val
                                print(f"{parameter}: {set_val}")
                            else:
                                print(f"Error de lectura {parameter} en {modbus_address}", result)       
        except Exception as e:
            print("Exception:", e)
    write_modbus(1,)
