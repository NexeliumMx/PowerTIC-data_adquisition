import psycopg2
try:
    table = "measurements"
    conn = psycopg2.connect(
        user = "citus",
        host="c-powertic-datastorage.epyggvp2kmwak7.postgres.cosmos.azure.com",
        database="powerticapp",
        password="D8bPCJtLY8mkead",  # luis: Tono2002 //Arturo: 2705
        port=5432

    )
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM powertic.{table};")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        print("Column names: ", column_names)

    conn_new = psycopg2.connect(
        user = "superadmin",
        host="powertic.postgres.database.azure.com",
        database="postgres",
        password="vafja6-hexpem-javdyN",  # luis: Tono2002 //Arturo: 2705
        port=5432

    )

    with conn_new.cursor() as cursor:
        columns_str = ", ".join(column_names)
        placeholders = ", ".join(["%s"] * len(column_names))
        insert_query = f"INSERT INTO powertic.{table} ({columns_str}) VALUES ({placeholders})"

        for row in rows:
            print("row = ", row)
            row = list(row)
            print("Row is type: ", type(row))
            
            """modbus_address = column_names.index('modbus_address')
            print("modbus address index: ", modbus_address)
            print("modbus address value: ",row[modbus_address])
            replace_add = str(row[modbus_address])
            print("New Modbus address: ", replace_add, type(replace_add))
            row[modbus_address] = replace_add
            print("replaced modbusquery: ",row[modbus_address], type(row[modbus_address]))
            print("executing query for: ", row)"""

            cursor.execute(insert_query,row)
        
        conn_new.commit()
        
        cursor.execute(f"SELECT * FROM powertic.{table};")
        inserted_rows = cursor.fetchall()
        print(f"Inserted rows into {table}: ")
        for inserted_row in inserted_rows:
            print(inserted_row)

except Exception as e:
    print("Error: ", e)

        