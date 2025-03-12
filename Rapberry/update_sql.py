import pandas as pd
import psycopg2
import json

# Connect to local PostgreSQL
local_conn = psycopg2.connect(
    user="luis.sanchez@nexelium.com.mx",
    host="nexelium-pg.postgres.database.azure.com",
    database="powertick",
    password="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImltaTBZMnowZFlLeEJ0dEFxS19UdDVoWUJUayIsImtpZCI6ImltaTBZMnowZFlLeEJ0dEFxS19UdDVoWUJUayJ9.eyJhdWQiOiJodHRwczovL29zc3JkYm1zLWFhZC5kYXRhYmFzZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzBjMDM2M2RiLTgzN2UtNDE1NC1iYmMwLWZlMWM1ZGI5ZDRlNy8iLCJpYXQiOjE3NDA1NDAyMzQsIm5iZiI6MTc0MDU0MDIzNCwiZXhwIjoxNzQwNTQ1MzQxLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFpBQUFBVGlwakpRRE5uQnNJSDAyQWMrVjBXdkdBOHJwdm1pbGVKQUd5NzRWbzZWeXdSaTJHam1yWEJJcmlMdVl5TXhQbkFUa2ZDVC9pdlVGdkE5RWs1WHFOWlphQkwySzMrRE03OEVHUVh3ektlMDg9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjA0YjA3Nzk1LThkZGItNDYxYS1iYmVlLTAyZjllMWJmN2I0NiIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiU8OhbmNoZXogSXNsYXMiLCJnaXZlbl9uYW1lIjoiTHVpcyBBbnRvbmlvIiwiZ3JvdXBzIjpbIjVlZjEyNDc2LWI3MTQtNGNmZi05MzVlLWUzNWNlNmFlNjlhNCIsImE2OGJjYmRkLTVkMWUtNGZiMC1iOGFkLTgwYjcwMzZiODVkYyIsIjQyMGFiZmRmLTRlMzItNDcxZi1iYzMxLTE0YzNhZDZkNmY5OSIsImViNjk3OWVkLTc4MzMtNGQwNy04OTM0LWQxNzk0NWViNzA3ZiIsImQ0OWM3N2VkLTIyMjEtNDZiNy1hZTcxLWUzZTUyMmUxYzFkZCJdLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyODA2OjJmMDo5MWEwOmQwYTc6ZjQ1Mzo2MjM5OjRiOTQ6MjMiLCJuYW1lIjoiTHVpcyBBbnRvbmlvIFPDoW5jaGV6IElzbGFzIiwib2lkIjoiNDcxNGMyMDUtZDRmMS00MWY0LTlkN2ItZjRlODViOWNhNzEyIiwicHVpZCI6IjEwMDMyMDAzREVGNzZEMTUiLCJyaCI6IjEuQVdNQjIyTURESDZEVkVHN3dQNGNYYm5VNTFEWVBCTGYyYjFBbE5YSjhIdF9vZ05qQVJKakFRLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInNpZCI6ImQ4ODFlZTI0LWMzNGYtNDZhNC1iYWJhLWQyOWIwYTY3ODkzMiIsInN1YiI6Im1NSExqQ0NVRWNjeUZDUHl2d3NDLVZqXzJEZ3FYNloxT0J3d0lSMUlpU1kiLCJ0aWQiOiIwYzAzNjNkYi04MzdlLTQxNTQtYmJjMC1mZTFjNWRiOWQ0ZTciLCJ1bmlxdWVfbmFtZSI6Imx1aXMuc2FuY2hlekBuZXhlbGl1bS5jb20ubXgiLCJ1cG4iOiJsdWlzLnNhbmNoZXpAbmV4ZWxpdW0uY29tLm14IiwidXRpIjoiUkhVYkU5UXoyMC13Z2poZ3pxOUZBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjEgMjgifQ.UM9_fy0FwoRngifryu-ctZaDnvkot2tHDmjqpuL0ZIjxHp11mmrpbEKrszI9jy7pToxWrMqMn7ye07ObtS0eN6OWFFGKpAIcEBtf0L2Rh6EhMmivBu-0iv4PUS7CZm-cHFMPDV2Al_L9jpYcjQwBpI_TdbMWssmS3lp6lEtYWl-ygTW0uFyg37-tw1SZm9xC8GPNfuBboGldcdYCQSrQ37D7Bu2kBv-dTY4GiGhSyyF0VSxH3cQ5MtNIeQcZjaSybQYexvU1Qx9EdKH9EJDWf9KkqcwmqKP99mCGe1CqGmv8dyJs-X4gGmGK1icg6xHP_5SQWdCRLpqlvOkgnjL8Ww",  # Replace with your actual password
    port=5432
)

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/luissanchez/Library/CloudStorage/OneDrive-NexeliumTechnologicalSolutionsSAdeCV/Documents - PowerTIC Project/Modelo CFE/periodos_horarios_final.csv')

# Function to format time ranges as proper JSON
def format_time_ranges(value):
    if value == '{null}':
        return None
    if isinstance(value, str) and value.startswith('{{') and value.endswith('}}'):
        # Convert string representation of time ranges to proper JSON array
        ranges = value.strip('{}').split('},{')
        time_ranges = []
        for time_range in ranges:
            times = time_range.strip('{"}').split('","')
            time_ranges.append(times)
        return json.dumps(time_ranges)
    return value

# Process DataFrame
for column in df.columns:
    if df[column].dtype == object:  # Only process string columns
        df[column] = df[column].apply(lambda x: x.strip('"') if isinstance(x, str) else x)
        if 'lunes_viernes' in column or 'sabado' in column or 'domingo_festivo' in column:
            df[column] = df[column].apply(format_time_ranges)

# Extract column names from the DataFrame
column_names = df.columns.tolist()

# Prepare placeholders for the SQL query
placeholders = ", ".join(["%s"] * len(column_names))

# Create the INSERT query
insert_query = f'INSERT INTO dev.periodos_horarios({", ".join(column_names)}) VALUES ({placeholders})'

# Iterate over DataFrame rows
with local_conn.cursor() as cursor:
    for index, row in df.iterrows():
        row_data = tuple(row)
        print("Executing query for row:", row_data)
        cursor.execute(insert_query, row_data)

    # Commit the transaction
    local_conn.commit()

# Close the connection
local_conn.close()