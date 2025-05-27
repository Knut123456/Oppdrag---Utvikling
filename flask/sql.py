
from connect_to_database import connect_to_database_def

def sql_def():
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