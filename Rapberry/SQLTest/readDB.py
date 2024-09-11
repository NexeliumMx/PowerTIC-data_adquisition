import psycopg2

# Create a new PostgreSQL client connection
try:
    conn = psycopg2.connect(
        user="postgres",
        host="localhost",
        database="Acurev1313_ModbusAddress",
        password="Tono2002",  # luis: Tono2002 //Arturo: 2705
        port=5432
    )
    print('Connected to the database.')

    # Function to print parameter descriptions from a specified table
    def print_parameter_descriptions(table_name):
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT parameter_description, modbus_address, register_number FROM {table_name}")
            rows = cursor.fetchall()
            print(f"\nParameter Descriptions and Modbus Addresses from {table_name}")
            for row in rows:
                if isinstance(row[1], list):
                    print(f"Description: {row[0]} - Modbus Address: {row[1][0]} - Number of registers: {row[2]}")
                else:
                    print(f"Description: {row[0]} - Modbus Address: {row[1]} - Number of registers: {row[2]}")

    # Print parameter descriptions from both tables
    print_parameter_descriptions('readings_addresses')
    print_parameter_descriptions('device_info_addresses')

except Exception as error:
    print(f"Error executing query: {error}")

finally:
    # Close the connection
    if conn:
        conn.close()
        print('Connection closed.')
