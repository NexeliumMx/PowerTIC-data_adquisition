import psycopg2# Connect to local PostgreSQL

local_conn = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="postgres",
    password="postgres",  # Replace with your actual password
    port=5432
)

# Fetch data from Azure PostgreSQL
with local_conn.cursor() as cursor:
    cursor.execute("SELECT * FROM powertic.modbusqueries;")
    rows = cursor.fetchall()
    
    # Fetch column names
    column_names = [desc[0] for desc in cursor.description]
    print(column_names)

    column_str = ", ".join(column_names)
    placeholders = ", ".join(["%s"] * len(column_names))
    insert_query = f'INSERT INTO powertic.modusqueries({column_names}) VALUES ('
    for row in rows:
        row = list(row)
        modbus_address_index = column_names.index('modbus_address')
        strq =''
        