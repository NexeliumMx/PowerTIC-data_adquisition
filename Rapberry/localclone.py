import psycopg2

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
    cursor.execute("SELECT * FROM powertic.meters;")
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
    insert_query = f"INSERT INTO public.meters ({columns_str}) VALUES ({placeholders})"
    
    # Insert each row into the localtest table
    for row in rows:
        cursor.execute(insert_query, row)
    
    # Commit the transaction
    local_conn.commit()

    # Optional: Verify that the data has been inserted
    cursor.execute("SELECT * FROM public.meters;")
    inserted_rows = cursor.fetchall()
    print("Inserted rows into local PostgreSQL:")
    for inserted_row in inserted_rows:
        print(inserted_row)

# Close the connections
azure_conn.close()
local_conn.close()