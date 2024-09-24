import psycopg2

# PostgreSQL Init

connlocal= psycopg2.connect(
    user="postgres",
    host="localhost",
    database="postgres",
    password="postgres",  # luis: Tono2002 //Arturo: 2705
    port=5432
)

with connlocal.cursor() as cursor:
    cursor.execute("SELECT * FROM powertic.modbusqueries;")
    rows = cursor.fetchall()
    
    # Fetch column names
    column_names = [desc[0] for desc in cursor.description]
    

conn = psycopg2.connect(
    user="superadmin",
    host="powerticpgtest1.postgres.database.azure.com",
    database="powerticapp",
    password="vafja6-hexpem-javdyN",  # luis: Tono2002 //Arturo: 2705
    port=5432
)

with conn.cursor() as cursor:
    #print(rows)
    #print(column_names)
    # Prepare the SQL INSERT statement with placeholders for parameters
    columns_str = ", ".join(column_names)
    placeholders = ", ".join(["%s"] * len(column_names))
    print(columns_str)
    print(placeholders)
    insert_query = f"INSERT INTO powertic.modbusqueries ({columns_str}) VALUES ({placeholders})"

    # Insert each row into the locationsbackup table
    for row in rows:
        #print("Row is of type: ", type(row))
        #print(str(row[10]).replace("[","{").replace("]","}"))
        print("row[10] type: ", type(row[10]))
        new_value = str(row[10]).replace("[","{").replace("]","}")
        row = list(row)
        row[10] = new_value
        print("Modified row: ", row)
        cursor.execute(insert_query, row)
    
    conn.commit()  # Commit the transaction to the database
