import psycopg2
def uploadloc(path):
    conn = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="powerticapp",
    password="postgres",  # luis: Tono2002 //Arturo: 2705
    port=5432
)
    f=open(path,'r')
    q=f.read()
    query=conn.cursor()
    query.execute(q)
    conn.commit()
def uploadcloud(path):
    conn = psycopg2.connect(
    user="superadmin",
    host="powerticpgtest1.postgres.database.azure.com",
    database="powerticapp",
    password="vafja6-hexpem-javdyN",  # luis: Tono2002 //Arturo: 2705
    port=5432
)
 
    query=conn.cursor()
    query.execute(path)
    conn.commit()
