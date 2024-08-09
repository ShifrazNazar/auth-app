from sqlite3 import connect

DB_PATH = "/Users/m2air16-256/Developer/Personal/auth-app.db"

def get_db_connection():
    conn = connect(DB_PATH)
    return conn
