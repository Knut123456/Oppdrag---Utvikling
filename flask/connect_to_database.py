from secret import MARIADB
from mariadb import connect
import mysql.connector
from mysql.connector import Error
def connect_to_database_def(): #connecter til databasen 
    try:
        conn = mysql.connector.connect(
            host=MARIADB["host"],
            user=MARIADB["user"],
            password=MARIADB["password"],
            database=MARIADB["database"],
            port=MARIADB["port"] 
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error while connecting to MariaDB: {e}")
    
    return None 
