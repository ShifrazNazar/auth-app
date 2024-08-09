from sqlite3 import connect

DB_PATH = "/Users/m2air16-256/Developer/auth-app.db"

def initialize_database():
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    """
    with connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()

def get_db_connection():
    initialize_database()
    conn = connect(DB_PATH)
    return conn
