import psycopg2
try:
    table = "locations"
    conn = psycopg2.connect(
        user = "superadmin",
        host="powerticpgtest1.postgres.database.azure.com",
        database="powerticapp",
        password="vafja6-hexpem-javdyN",  # luis: Tono2002 //Arturo: 2705
        port=5432
    )
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM powertic.{table};")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

    conn_new = psycopg2.connect(
        user = "citus",
        host="c-powertic-datastorage.epyggvp2kmwak7.postgres.cosmos.azure.com",
        database="powerticapp",
        password="D8bPCJtLY8mkead",  # luis: Tono2002 //Arturo: 2705
        port=5432
    )

    with conn_new.cursor() as cursor:
        columns_str = ", ".join(column_names)
        placeholders = ", ".join(["%s"] * len(column_names))
        insert_query = f"INSERT INTO powertic.{table} ({columns_str}) VALUES ({placeholders})"

        for row in rows:
            cursor.execute(insert_query,row)
        
        conn_new.commit()
        
        cursor. execute(f"SELECT * FROM powertic.{table};")
        inserted_rows = cursor.fetchall()
        print(f"Inserted rows into {table}: ")
        for inserted_row in inserted_rows:
            print(inserted_row)

except Exception as e:
    print("Error: ", e)

finally:
    conn.close()
    conn_new.close()
        