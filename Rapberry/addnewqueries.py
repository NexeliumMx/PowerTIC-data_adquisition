import pandas as pd
import psycopg2

# Connect to local PostgreSQL
local_conn = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="postgres",
    password="postgres",  # Replace with your actual password
    port=5432
)


df = pd.read_excel('NewModbusQueries.xlsx')

column_names= df.columns.tolist()
print(column_names)

for index, row in df.iterrows():
    print(row.tolist())

with local_conn.cursor() as cursor:
    placeholders = ", ".join(["%s"] * len(column_names))
    insert_query = f'INSERT INTO powertic.modbusqueries({str(column_names).replace("[","").replace("]","").replace("'","\"")}) VALUES ('
    for index, row in df.iterrows():
        row = list(row)
        strq=''
        modbus_address = column_names.index('modbus_address')
        print("Index: ",modbus_address)
        if isinstance(row[modbus_address],list):
            row[modbus_address] = 'ARRAY [' + ','.join(map(str,row(modbus_address)))+']'
            print(row[modbus_address])
        elif isinstance(row[modbus_address], int):
            row[modbus_address] = '{'+ str(row[modbus_address]) + '}'
        for i in range(0,len(row)):
            if isinstance(row[i],int):
                strq+=str(row[i])
            else:
                strq+='\''+str(row[i])
            if i!=len(row)-1:
                if isinstance(row[i],int) | isinstance(row[i],list):
                    strq+=','
                else:
                    strq+='\','
            else:
                if isinstance(row[i],int)| isinstance(row[i],list):
                    strq+=')'
                else:
                    strq+='\')'
        # Execute the insert query
        print(insert_query+strq)
        print(row)
        cursor.execute((insert_query+strq))
    
    # Commit the transaction
    local_conn.commit()

local_conn.close()