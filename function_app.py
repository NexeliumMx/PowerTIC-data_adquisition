import azure.functions as func
import logging
import json
import psycopg2

app = func.FunctionApp()

@app.function_name(name="eventgridtrigger")
@app.event_grid_trigger(arg_name="event")
def test_function(event: func.EventGridEvent):
    # Parse the event grid data
    event_data = event.get_json()
    device_id = event_data.get('deviceId')
    event_time = event_data.get('eventTime')
    telemetry_data = event_data.get('body', {})  # Assuming telemetry data is in 'body'

    # Log the event
    result = json.dumps({
        'id': event.id,
        'data': event_data,
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })
    logging.info('Python EventGrid trigger processed an event: %s', result)

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        user="superadmin",
        host="powerticpgtest1.postgres.database.azure.com",
        database="powerticapp",
        password="vafja6-hexpem-javdyN",  # Your password
        port=5432
    )
    cursor = conn.cursor()

    try:
        # Insert the telemetry data into the database
        cursor.execute(
            """
            INSERT INTO telemetry_data (device_id, event_time, data)
            VALUES (%s, %s, %s)
            """,
            (device_id, event_time, json.dumps(telemetry_data))
        )
        conn.commit()
    except Exception as e:
        logging.error(f"Failed to insert data into PostgreSQL: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

    logging.info('Event processed and stored successfully')