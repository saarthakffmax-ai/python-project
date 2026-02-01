import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    database="testdb",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)

print("Connected successfully at", datetime.now())
conn.close()
