import psycopg2

# Create a new PostgreSQL client
connection = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="Acurev1313_ModbusAddress",
    password="Tono2002",
    port=5432
)

try:
    # Connect to the database
    cursor = connection.cursor()
    print('Connected to the database.')

    # Execute the query
    cursor.execute('SELECT parameter_description FROM readings_addresses')
    
    # Fetch all the results
    rows = cursor.fetchall()
    
    # Print all the parameter_description values
    for row in rows:
        print(row[0])

except Exception as error:
    print('Error executing query:', error)

finally:
    # Close the connection
    if connection:
        cursor.close()
        connection.close()
        print('Database connection closed.')
