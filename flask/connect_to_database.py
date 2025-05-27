from secret import MARIADB
import mysql.connector
from mysql.connector import Error
def connect_to_database_def(): #connecter til databasen 
    host= MARIADB["host"],
    user= MARIADB["user"],
    password=  MARIADB["password"],
    database = MARIADB["database"],
    port = MARIADB["port"],
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port 
        )
        if conn.is_connected():
            print(f"Connected to database, {database}")
            return conn
            
    except Error as e:
        print(f"Error while connecting to MariaDB: {e}")

    return None 
