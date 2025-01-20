
def connect_to_database_def(database):
    from pathlib import Path
    import sys
    parent_div = Path(__file__).parent
    sys.path.append(str(parent_div))
    import mysql.connector
    from mysql.connector import Error
    from dotenv import load_dotenv
    import os

    # Load environment variables from .env file

    load_dotenv()
    if database == "trading_web_scraper":
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_database")
        port = os.getenv("port")

    elif database == "trading_web_scraper_usefull_info":
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_database_2")
        port = os.getenv("port")       

    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port 
        )
        if conn.is_connected():
           #print(f"Connected to database ,{database}")
            return conn
            
    except Error as e:
        print(f"Error while connecting to MariaDB: {e}")

    return None 

connect_to_database_def("trading_web_scraper")