import psycopg2

# PostgreSQL Init

connlocal= psycopg2.connect(
    user="postgres",
    host="localhost",
    database="powerTic",
    password="Tono2002",  # luis: Tono2002 //Arturo: 2705
    port=5432
)

with connlocal.cursor() as cursor:
    cursor.execute("SELECT * FROM powertic.locations;")
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
    print(rows)
    print(column_names)
    # Prepare the SQL INSERT statement with placeholders for parameters
    columns_str = ", ".join(column_names)
    placeholders = ", ".join(["%s"] * len(column_names))
    print(columns_str)
    print(placeholders)
    insert_query = f"INSERT INTO powertic.locationsbackup ({columns_str},mockid) VALUES ({placeholders},1234)"

    # Insert each row into the locationsbackup table
    for row in rows:
        cursor.execute(insert_query, row)
    
    conn.commit()  # Commit the transaction to the database
