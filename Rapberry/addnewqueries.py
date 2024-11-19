import pandas as pd
import psycopg2

# Connect to local PostgreSQL
local_conn = psycopg2.connect(
    user="luis.sanchez@nexelium.com.mx",
    host="nexelium-pg.postgres.database.azure.com",
    database="PowerTick",
    password="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCIsImtpZCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCJ9.eyJhdWQiOiJodHRwczovL29zc3JkYm1zLWFhZC5kYXRhYmFzZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzBjMDM2M2RiLTgzN2UtNDE1NC1iYmMwLWZlMWM1ZGI5ZDRlNy8iLCJpYXQiOjE3MzEzNjU0MjksIm5iZiI6MTczMTM2NTQyOSwiZXhwIjoxNzMxMzY5NDA2LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFlBQUFBMDM2Yjk3a1VSaWlYYnJpb0xEaFJ4Q0tTd1lIQUhnWUdsc3kzZDN0Sys4clVHZDg0VFBTYXJMdytxRnp6bWZuK01Ib29Wb2crOG5tcHRRVjJoS1NLZmNrMmtSeWVwbU9HZGxyVDhXRERROUk9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjA0YjA3Nzk1LThkZGItNDYxYS1iYmVlLTAyZjllMWJmN2I0NiIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiU8OhbmNoZXogSXNsYXMiLCJnaXZlbl9uYW1lIjoiTHVpcyBBbnRvbmlvIiwiZ3JvdXBzIjpbIjVlZjEyNDc2LWI3MTQtNGNmZi05MzVlLWUzNWNlNmFlNjlhNCIsIjQyMGFiZmRmLTRlMzItNDcxZi1iYzMxLTE0YzNhZDZkNmY5OSIsImViNjk3OWVkLTc4MzMtNGQwNy04OTM0LWQxNzk0NWViNzA3ZiIsImQ0OWM3N2VkLTIyMjEtNDZiNy1hZTcxLWUzZTUyMmUxYzFkZCJdLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyODA2OjEwN2U6Zjo5YWUxOmQ0YWE6OTNlOTpmNGZkOjZlOWQiLCJuYW1lIjoiTHVpcyBBbnRvbmlvIFPDoW5jaGV6IElzbGFzIiwib2lkIjoiNDcxNGMyMDUtZDRmMS00MWY0LTlkN2ItZjRlODViOWNhNzEyIiwicHVpZCI6IjEwMDMyMDAzREVGNzZEMTUiLCJyaCI6IjEuQVdNQjIyTURESDZEVkVHN3dQNGNYYm5VNTFEWVBCTGYyYjFBbE5YSjhIdF9vZ05qQVJKakFRLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6Im1NSExqQ0NVRWNjeUZDUHl2d3NDLVZqXzJEZ3FYNloxT0J3d0lSMUlpU1kiLCJ0aWQiOiIwYzAzNjNkYi04MzdlLTQxNTQtYmJjMC1mZTFjNWRiOWQ0ZTciLCJ1bmlxdWVfbmFtZSI6Imx1aXMuc2FuY2hlekBuZXhlbGl1bS5jb20ubXgiLCJ1cG4iOiJsdWlzLnNhbmNoZXpAbmV4ZWxpdW0uY29tLm14IiwidXRpIjoiN2dYUUZEMVBtMHlGblo4aVpRS1BBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjEgMjYifQ.FLwD5FMJ9cqP-JZ1cUnigFJ28gXGTs_Oj7Wlf6d8TVpZyWqseJsfdnalWnh4IlMzif49DiEWg8x4aiRGZcuJnsOlJ_L1FUCbdMlq41904CHkvrezVP-w1FyP8Es6OBVfKr_Zh7wxcj0ylNjHrDA5hVZaemyzx89DbiVCx5hA_yEPci1fP_aUaw3MZXb6_c0vthXgPpWtE74tFZLea7OZd0vwtkU2G9j9hfCsjQ_RXmUgiWIVm5EzfLiAYkAVoAKwMBr1gP9oTEOE5wMxZXiG6C65vWHfLiwTdpPIQj66zrF_1ZkZoyMdTVImGt95GMwWSh0DMZCKSB2aaKwGc_zhjQ",  # Replace with your actual password
    port=5432
)

# Read the Excel file into a DataFrame
df = pd.read_csv('/Users/luissanchez/MICO/PowerTIC/Rapberry/modbusrtu_commands.csv')
print(df)
# Extract column names from the DataFrame
column_names = df.columns.tolist()
print(column_names)

# Prepare placeholders for the SQL query
placeholders = ", ".join(["%s"] * len(column_names))

# Create the INSERT query
insert_query = f'INSERT INTO public.modbusrtu_commands({", ".join(column_names)}) VALUES ({placeholders})'

# Iterate over DataFrame rows
with local_conn.cursor() as cursor:
    for index, row in df.iterrows():
        #modbus_address = column_names.index('modbus_address')
        #print(row[modbus_address])
        
        row_data = tuple(row)  # Convert row to a tuple for insertion
        print("Executing query for row:", row_data)
        
        # Execute the insert query using parameterized queries

        cursor.execute(insert_query, row_data)

    # Commit the transaction
    local_conn.commit()

# Close the connection
local_conn.close()