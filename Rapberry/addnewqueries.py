import pandas as pd
import psycopg2

# Connect to local PostgreSQL
local_conn = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="postgres",
    password="postgres",  # Replace with your actual password
    port=5432
)

# Read the Excel file
df = pd.read_excel('NewModbusQueries.xlsx')

# Get column names
column_names = df.columns.tolist()
print(column_names)

# Construct the insert query
placeholders = ", ".join(["%s"] * len(column_names))
insert_query = f'INSERT INTO public.modbusqueries ({", ".join(column_names)}) VALUES ({placeholders})'

# Loop through rows and process data
with local_conn.cursor() as cursor:
    for index, row in df.iterrows():
        row_data = list(row)

        # Handle modbus_address if it's a list or int
        modbus_address_index = column_names.index('modbus_address')
        
        if isinstance(row_data[modbus_address_index], list):
            row_data[modbus_address_index] = '{' + ','.join(map(str, row_data[modbus_address_index])) + '}'
        elif isinstance(row_data[modbus_address_index], int):
            row_data[modbus_address_index] = '{' + str(row_data[modbus_address_index]) + '}'

        # Convert row data to tuple for cursor execution
        row_data_tuple = tuple(row_data)
        
        # Execute the insert query
        cursor.execute(insert_query, row_data_tuple)

    # Commit the transaction
    local_conn.commit()

# Close the connection
local_conn.close()