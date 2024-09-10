import azure.functions as func
import logging
import json
import psycopg2

app = func.FunctionApp()

@app.function_name(name="eventgridtrigger")
@app.event_grid_trigger(arg_name="event")
def test_function(event: func.EventGridEvent):

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info('Python EventGrid trigger processed an event: %s', result)

@app.route(route="InfoUploadAPI", auth_level=func.AuthLevel.ANONYMOUS)
def InfoUploadAPI(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.params.get('data')
    if not data:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            data = req_body.get('data')

    if data:
        conn = psycopg2.connect(
            user="superadmin",
            host="powerticpgtest1.postgres.database.azure.com",
            database="powerticapp",
            password="vafja6-hexpem-javdyN",  # luis: Tono2002 //Arturo: 2705
            port=5432
        )

        with conn.cursor() as cursor:
            print(data)
            column_names = data[0]
            print(column_names)
            # Prepare the SQL INSERT statement with placeholders for parameters
            columns_str = ", ".join(column_names)
            placeholders = ", ".join(["%s"] * len(column_names))
            print(columns_str)
            print(placeholders)
            insert_query = f"INSERT INTO powertic.locationsbackup ({columns_str}) VALUES ({placeholders})"

            # Insert each row into the locationsbackup table
            for row in data:
                cursor.execute(insert_query, row)
            
            conn.commit()  # Commit the transaction to the database
        return func.HttpResponse(f"Hello, {data}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. But there is no data receieved",
             status_code=200
        )