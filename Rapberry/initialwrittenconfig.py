from modbus16bit import write_modbus_multiple 
import json
import csv
#from decode_modbus import decode_modbus_response



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
                            result = write_modbus_multiple(1,row["write_command"],modbus_address,1,2,addrs)
                            #decode_modbus_response(response=result,slave_address=addrs,datatype='')
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
                print(row)
                if row["model"]==model:
                    if row["setupWrite"] == "t":
                        setup = True
                    elif row["setupWrite"] == "f":
                        setup = False
                    
                    print(row)
                              
                    print("--------------------------------------------------------------------------------")
                    print(row["model"]) 
                    print(model==row["model"])    
                    print('vtsetup')
                    parameter = row['parameter']
                    if setup == True & (bool((row["address"]))!=1): 
                        print(row)
                              
                        print("--------------------------------------------------------------------------------")
                        print(row["model"]) 
                        print(model==row["model"])    
                        print('vtsetup')
                        
                        
                        set_val = ""
                        
                        modbus_address = (row["modbus_address"])
                                                    
                        try:
                            result = write_modbus_multiple(mbdadd,row["write_command"],modbus_address,1,2,values[parameter])
                            print(result)
                            #decode_modbus_response(response=result,slave_address=addrs,datatype='')
                        except ValueError:
                            print(f"Invalid address for {parameter}: {modbus_address}")
                            continue
                    
                             
        except Exception as e:
            print("Exception:", e)
