import psycopg2
import random

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="python_lab",
    user="postgres",
    password="Rabindra",
    host="localhost",
    port="5432",
)

#### Write Data  ###
data = [("Alice", "alice@example.com"), ("Bob", "bob@example.com")]

cur = conn.cursor()
cur.executemany("INSERT INTO your_table (name, email) VALUES (%s, %s)", data)
conn.commit()

conn.close()
