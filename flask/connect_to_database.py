from secret import MARIADB
from mariadb import connect
import mysql.connector
from mysql.connector import Error
def connect_to_database_def(): #connecter til databasen 
    try:
        conn = connect(
            user=MARIADB['user'],
            password=MARIADB['password'],
            host=MARIADB['host'],
            port=MARIADB['port'],
            database=MARIADB['database']
        )
        if conn.is_connected():
            print("Connected to database")
            return conn
            
    except Error as e:
        print(f"Error while connecting to MariaDB: {e}")

    return None 
