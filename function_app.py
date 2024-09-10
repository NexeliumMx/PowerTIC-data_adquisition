import logging
import psycopg2
import azure.functions as func
import os

@app.route(route="InfoUploadAPI", auth_level=func.AuthLevel.ANONYMOUS)
def InfoUploadAPI(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.params.get('data')
    if not data:
        try:
            req_body = req.get_json()
            data = req_body.get('data')
        except ValueError:
            return func.HttpResponse(
                "Invalid JSON received.", 
                status_code=400
            )

    if data:
        try:
            conn = psycopg2.connect(
                user=os.getenv("DB_USER"),  # Use environment variables
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                password=os.getenv("DB_PASSWORD"),
                port=5432
            )

            with conn.cursor() as cursor:
                # Extract the column names from the first row
                column_names = data[0]
                columns_str = ", ".join(column_names)
                placeholders = ", ".join(["%s"] * len(column_names))
                
                insert_query = f"INSERT INTO powertic.locationsbackup ({columns_str}) VALUES ({placeholders})"

                # Insert each row into the locationsbackup table, skipping the first row
                for row in data[1:]:
                    cursor.execute(insert_query, row)
                
                conn.commit()  # Commit the transaction to the database

            return func.HttpResponse(
                f"Data successfully inserted: {len(data[1:])} rows", 
                status_code=200
            )

        except psycopg2.Error as e:
            logging.error(f"Database error: {e}")
            return func.HttpResponse(
                "Error inserting data into the database.", 
                status_code=500
            )
    else:
        return func.HttpResponse(
             "No data received.",
             status_code=400
        )