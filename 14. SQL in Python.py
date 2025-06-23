import psycopg2

conn = psycopg2.connect(
    dbname="demo_class",
    user="postgres",
    password="Rabindra",
    host="localhost",
    port=5432,
)

cur = conn.cursor()

QUERY = """
UPDATE student
SET addreess = 'Kathmandu'
WHERE roll_no = 7;
"""

cur.execute(QUERY)
# db_result = cur.fetchall()
conn.commit()

# print(db_result)
