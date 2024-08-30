import logging
import psycopg2
import os
from datetime import datetime

def main(event: list):
    # Database connection details from environment variables
    conn = psycopg2.connect(
        dbname=os.getenv('PGDATABASE'),
        user=os.getenv('PGUSER'),
        password=os.getenv('PGPASSWORD'),
        host=os.getenv('PGHOST'),
        port=os.getenv('PGPORT')
    )
    cursor = conn.cursor()

    # Process each message from the Event Hub
    for message in event:
        # Assuming the message is JSON and contains 'device_id' and 'data'
        device_id = message.get('device_id')
        data = message.get('data')

        # Insert data into PostgreSQL
        try:
            cursor.execute(
                "INSERT INTO telemetry_data (device_id, event_time, data) VALUES (%s, %s, %s)",
                (device_id, datetime.utcnow(), json.dumps(data))
            )
            conn.commit()
        except Exception as e:
            logging.error(f"Error inserting data: {e}")
            conn.rollback()

    cursor.close()
    conn.close()