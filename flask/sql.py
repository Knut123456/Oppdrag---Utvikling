import sys
from pathlib import Path
parent_div = Path(__file__).parent
sys.path.append(str(parent_div))
from connect_to_database import connect_to_database_def
from dotenv import load_dotenv, find_dotenv
import mysql
import os
def sql_def():
    """ env_path = Path('./.env')

    print("Using env file:", env_path.resolve())
    env_file = find_dotenv()
    print("Loading env file at:", env_file)
    
    load_dotenv(override=True)
    host = os.getenv("host")#DB_HOST
    user = os.getenv("user")#DB_USER
    password = os.getenv("password")#DB_PASSWORD
    database = os.getenv("database")#DB_database_2
    port = os.getenv("port")#port   
    print(f"{port=}, {host=}, {user=}, {password=}, {database=} ")
 """
    host= "10.100.10.142"
    user= "Oppdrag_UtviklingOppdrag_Utvikling"
    password=  "Oppdrag_UtviklingOppdrag_Utvikling" 
    database = "Oppdrag_UtviklingOppdrag_Utvikling"
    port = 3306

    #rint(f"{port=}, {host=}, {user=}, {password=}, {database=} ")

    conn = connect_to_database_def()
    print(conn)
    create_table_query_user  = (
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL, 
            email VARCHAR(100) NOT NULL,
            password VARCHAR(1000) NOT NULL,
            role VARCHAR(100)NOT NULL DEFAULT 'user' 
        )
        """
    )
    create_table_query_books = (
        """
        CREATE TABLE IF NOT EXISTS book (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Bok VARCHAR(50) NOT NULL,
            Kildespråk VARCHAR(50) NOT NULL,
            oversettelse VARCHAR(50) NOT NULL,
            kunde VARCHAR(50) NOT NULL
        )
        """
    )
    cur = conn.cursor()

    cur.execute(create_table_query_user)
    cur.execute(create_table_query_books)

    cur.close()
    
sql_def()