import psycopg2
import json

# Connect to Azure PostgreSQL
azure_conn = psycopg2.connect(
    user="superadmin",
    host="powerticpgtest1.postgres.database.azure.com",
    database="powerticapp",
    password="vafja6-hexpem-javdyN",  # Replace with your actual password
    port=5432
)

# Fetch data from Azure PostgreSQL
with azure_conn.cursor() as cursor:
    cursor.execute("SELECT * FROM powertic.modbusqueries;")
    rows = cursor.fetchall()
    
    # Fetch column names
    column_names = [desc[0] for desc in cursor.description]

# Connect to local PostgreSQL
local_conn = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="postgres",
    password="postgres",  # Replace with your actual password
    port=5432
)

# Insert data into local PostgreSQL
with local_conn.cursor() as cursor:
    # Prepare the SQL INSERT statement with placeholders for parameters
    columns_str = ", ".join(column_names)
    placeholders = ", ".join(["%s"] * len(column_names))
    insert_query = f'INSERT INTO public.modbusqueries ({columns_str}) VALUES ('
    
    # Insert each row into the modbusqueries table
    for row in rows:
        row = list(row)  # Convert tuple to list to make it mutable
        modbus_address_index = column_names.index('modbus_address')  # Find the index of the modbus_address column
        strq=''
        # If modbus_address is a list, convert it to PostgreSQL array format
        if isinstance(row[modbus_address_index], list):
            # Convert list to PostgreSQL array literal
            row[modbus_address_index] ='ARRAY [' + ','.join(map(str, row[modbus_address_index])) +']'
            print(row[modbus_address_index])
        # If modbus_address is an integer, convert it to a single-element array
        elif isinstance(row[modbus_address_index], int):
            row[modbus_address_index] = '{' + str(row[modbus_address_index]) + '}'
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

    # Optional: Verify that the data has been inserted
    cursor.execute("SELECT * FROM public.modbusqueries;")
    inserted_rows = cursor.fetchall()
    print("Inserted rows into local PostgreSQL:")
    for inserted_row in inserted_rows:
        print(inserted_row)

# Close the connections
azure_conn.close()
local_conn.close()