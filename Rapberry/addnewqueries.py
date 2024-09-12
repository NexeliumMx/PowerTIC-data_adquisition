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

# Read the Excel file into a DataFrame
df = pd.read_excel('NewModbusQueries.xlsx')

# Extract column names from the DataFrame
column_names = df.columns.tolist()
print(column_names)

# Prepare placeholders for the SQL query
placeholders = ", ".join(["%s"] * len(column_names))

# Create the INSERT query
insert_query = f'INSERT INTO public.modbusqueries({", ".join(column_names)}) VALUES ({placeholders})'

# Iterate over DataFrame rows
with local_conn.cursor() as cursor:
    for index, row in df.iterrows():
        row_data = tuple(row)  # Convert row to a tuple for insertion
        print("Executing query for row:", row_data)
        
        # Execute the insert query using parameterized queries
        modbus_address = column_names.index('modbus_address')
        print(row[modbus_address])
        str(row[modbus_address]).replace("[","{").replace("]", "}")
        cursor.execute(insert_query, row_data)

    # Commit the transaction
    local_conn.commit()

# Close the connection
local_conn.close()