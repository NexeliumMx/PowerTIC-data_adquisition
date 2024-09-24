import psycopg2
import psycopg2.extras
import os

# Retrieve credentials from environment variables (recommended for security)
LOCAL_DB_USER = os.getenv('LOCAL_DB_USER', 'postgres')
LOCAL_DB_PASSWORD = os.getenv('LOCAL_DB_PASSWORD', 'postgres')
LOCAL_DB_HOST = os.getenv('LOCAL_DB_HOST', 'localhost')
LOCAL_DB_NAME = os.getenv('LOCAL_DB_NAME', 'postgres')

REMOTE_DB_USER = os.getenv('REMOTE_DB_USER', 'superadmin')
REMOTE_DB_PASSWORD = os.getenv('REMOTE_DB_PASSWORD', 'vafja6-hexpem-javdyN')
REMOTE_DB_HOST = os.getenv('REMOTE_DB_HOST', 'powerticpgtest1.postgres.database.azure.com')
REMOTE_DB_NAME = os.getenv('REMOTE_DB_NAME', 'powerticapp')

try:
    # Connect to Local Database
    connlocal = psycopg2.connect(
        user=LOCAL_DB_USER,
        host=LOCAL_DB_HOST,
        database=LOCAL_DB_NAME,
        password=LOCAL_DB_PASSWORD,
        port=5432
    )

    # Connect to Remote Database
    conn = psycopg2.connect(
        user=REMOTE_DB_USER,
        host=REMOTE_DB_HOST,
        database=REMOTE_DB_NAME,
        password=REMOTE_DB_PASSWORD,
        port=5432
    )

    with connlocal.cursor() as cursor_local, conn.cursor() as cursor_remote:
        # Fetch data from local database
        cursor_local.execute("SELECT * FROM powertic.modbusqueries;")
        rows = cursor_local.fetchall()
        column_names = [desc[0] for desc in cursor_local.description]

        # Prepare the SQL INSERT statement
        columns_str = ", ".join(column_names)
        placeholders = ", ".join(["%s"] * len(column_names))
        insert_query = f"INSERT INTO powertic.modbusqueries ({columns_str}) VALUES ({placeholders})"

        # Insert data into the remote database
        for row in rows:
            row = list(row)  # Convert tuple to list to modify elements

            # Process row[10] if necessary
            if isinstance(row[10], list):
                # Convert Python list to PostgreSQL array literal
                row[10] = '{' + ','.join(map(str, row[10])) + '}'
            elif isinstance(row[10], str):
                # Replace brackets with braces if it's a string representation
                row[10] = row[10].replace("[", "{").replace("]", "}")
            else:
                # Handle other data types if necessary
                pass

            try:
                cursor_remote.execute(insert_query, row)
            except Exception as e:
                print(f"Error inserting row: {e}")
                conn.rollback()
                continue  # Skip this row and continue with the next

        conn.commit()  # Commit after all rows are processed

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close connections
    if 'connlocal' in locals():
        connlocal.close()
    if 'conn' in locals():
        conn.close()