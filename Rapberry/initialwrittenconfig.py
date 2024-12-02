from modbus16bit import write_modbus
import json
import csv

def initialaddres(model,addrs):
    with open('modbusrtu_commands.csv',newline='') as csvfile:
        rows = csv.DictReader(csvfile) 
        #print(rows)
        table_name = {}
        table_name["table"] = "meters"
        settings = {}
        print("rows: ",rows)
        try:
            for row in rows: 
                  
                if row["model"]==model:
                    if row["setupWrite"] == "t":
                        setup = True
                    elif row["setupWrite"] == "f":
                        setup = False
                    
                    
                    if setup == True & row["address"]==True: 
                        print(row)
                        print(row["parameter"],row["modbus_address"])      
                        print(row["setupRead"],type(row["setupRead"]), bool(row["setupRead"]),type(bool(row["setupRead"])) )
                        print("--------------------------------------------------------------------------------")
                        print(row["model"]) 
                        print(model==row["model"])  
                        parameter = row['parameter_description']
                        
                        set_val = ""
                        
                        modbus_address = (row["modbus_address"])
                                                    
                        try:
                            result = write_modbus(1,row["write_command"],modbus_address,1,2,addrs)
                            print(result)
                        except ValueError:
                            print(f"Invalid address for {parameter}: {modbus_address}")
                            continue
                    print(f"Adquirido valor para {parameter}: {set_val}")
                             
        except Exception as e:
            print("Exception:", e)
def ctvtsetup(model,mbdadd,ct,vt):
    keys=("ct",'vt')
    values=dict.fromkeys(keys)
    values["ct"]=ct
    values["vt"]=vt
    with open('modbusrtu_commands.csv',newline='') as csvfile:
        rows = csv.DictReader(csvfile) 
        #print(rows)
        table_name = {}
        table_name["table"] = "meters"
        settings = {}
        print("rows: ",rows)
        try:
            for row in rows: 
               
                if row["model"]==model:
                    if row["setupWrite"] == "t":
                        setup = True
                    elif row["setupWrite"] == "f":
                        setup = False
                    
                    
                    if setup == True & (bool((row["address"]))!=1): 
                        print(row)
                        print(row["parameter"],row["modbus_address"])      
                        print("--------------------------------------------------------------------------------")
                        print(row["model"]) 
                        print(model==row["model"])    
                        print('vtsetup')
                        parameter = row['parameter']
                        
                        set_val = ""
                        
                        modbus_address = (row["modbus_address"])
                                                    
                        try:
                            result = write_modbus(mbdadd,row["write_command"],modbus_address,1,2,values[parameter])
                            print(result)
                            
                        except ValueError:
                            print(f"Invalid address for {parameter}: {modbus_address}")
                            continue
                    print(f"Adquirido valor para {parameter}: {set_val}")
                             
        except Exception as e:
            print("Exception:", e)
