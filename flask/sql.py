from connect_to_database import connect_to_database_def
from dotenv import load_dotenv
import os
load_dotenv()
host = os.getenv("host")#DB_HOST
user = os.getenv("user")#DB_USER
password = os.getenv("password")#DB_PASSWORD
database = os.getenv("database")#DB_database_2
port = os.getenv("port")#port       
conn = connect_to_database_def(host, user, password, database, port)
create_table_query  = (
    """
    CREATE TABLE  IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(255) NOT NULL,
    )
    """
)
    