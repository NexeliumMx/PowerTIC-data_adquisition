import psycopg2
try:
    conn_new = psycopg2.connect(
        user = "citus",
        host="c-powertic-datastorage.epyggvp2kmwak7.postgres.cosmos.azure.com",
        database="powerticapp",
        password="D8bPCJtLY8mkead",  # luis: Tono2002 //Arturo: 2705
        port=5432
    )
except Exception as e:
    print("Error: ", e)