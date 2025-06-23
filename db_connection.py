import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Rabindra",
    host="localhost",
    port="5432",
)

cur = conn.cursor()

sutdent_data = [
    ('Ashmita', 'Kathmandu', 1),
    ('Bishal', 'Tillotama', 2),
    ('Rachita', 'Jhapa', 3),
]
SQL_QUERY = """
INSERT INTO student(student_name, address, course_id) 
VALUES (%s, %s, %s);
"""

cur.executemany(SQL_QUERY, sutdent_data)
# db_resuts = cur.fetchall()
conn.commit()
# print(db_resuts)
