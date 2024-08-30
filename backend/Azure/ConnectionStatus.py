# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(ConnectionStatus) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints
import logging
import psycopg2
import os
import json

def main(event: func.EventGridEvent):
    logging.info('EventGridEvent received: %s', event.get_json())
    
    # Extract necessary data from the event
    event_data = event.get_json()
    device_id = event_data['data']['deviceId']
    event_time = event_data['eventTime']
    data = json.dumps(event_data['data'])
    
    conn = psycopg2.connect(
        user="superadmin",
        host="powerticpgtest1.postgres.database.azure.com",
        database="powerticapp",
        password="vafja6-hexpem-javdyN",  # Replace with your actual password
        port=5432
    )
    
    try:
        with conn.cursor() as cursor:
            # Insert event data into the PostgreSQL table
            insert_query = """
            INSERT INTO telemetry_data (device_id, event_time, data)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (device_id, event_time, data))
            conn.commit()
            logging.info('Data inserted successfully')
    
    except Exception as e:
        logging.error('Error inserting data into PostgreSQL: %s', str(e))
        conn.rollback()
    
    finally:
        conn.close()