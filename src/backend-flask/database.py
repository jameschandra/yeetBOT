import sqlite3
import os.path

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "tasks.db")
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""DROP TABLE tasks""")

create_tasks_query = """CREATE TABLE tasks (
    id integer PRIMARY KEY,
    tanggal date NOT NULL,
    matkul text NOT NULL,
    tugas text NOT NULL,
    topik text NOT NULL
);"""
cursor.execute(create_tasks_query)