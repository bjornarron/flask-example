import psycopg2
import hashlib
import datetime


import sqlite3
import psycopg2
import hashlib
import datetime

sqlite_user_db_file_location = "database_file/users.db"
sqlite_note_db_file_location = "database_file/notes.db"
sqlite_image_db_file_location = "database_file/images.db"

postgres_host = 'localhost'
postgres_port = '5432'
postgres_database = 'flask_example'
postgres_user = 'postgres'
postgres_password = 'your_password'

def migrate_users():
    # Connect to SQLite database and retrieve user data
    sqlite_conn = sqlite3.connect(sqlite_user_db_file_location)
    sqlite_cursor = sqlite_conn.cursor()

    sqlite_cursor.execute("SELECT id, pw FROM users")
    user_data = sqlite_cursor.fetchall()

    # Connect to PostgreSQL database
    postgres_conn = psycopg2.connect(
        host=postgres_host,
        port=postgres_port,
        database=postgres_database,
        user=postgres_user,
        password=postgres_password
    )
    postgres_cursor = postgres_conn.cursor()

    # Migrate user data
    for user in user_data:
        id, pw = user
        hashed_pw = hashlib.sha256(pw.encode()).hexdigest()
        postgres_cursor.execute("INSERT INTO users (id, pw) VALUES (%s, %s)", (id.upper(), hashed_pw))

    # Commit changes and close connections
    postgres_conn.commit()
    postgres_conn.close()
    sqlite_conn.close()

if __name__ == "__main__":
    migrate_users()
