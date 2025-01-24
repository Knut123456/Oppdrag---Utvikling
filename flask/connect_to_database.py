
import mysql.connector
from mysql.connector import Error
def connect_to_database_def(): #connecter til databasen 
    

    host= "10.100.10.142"
    user= "Oppdrag_UtviklingOppdrag_Utvikling"
    password=  "Oppdrag_UtviklingOppdrag_Utvikling" 
    database = "Oppdrag_UtviklingOppdrag_Utvikling"
    port = 3306
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
