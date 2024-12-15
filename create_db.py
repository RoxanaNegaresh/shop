import mysql.connector

def create_db():
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root", 
        password=""  
    )

    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS shop")

    cursor.execute("USE shop")

    sql_dump = """
    -- SQL Dump from phpMyAdmin
    -- Insert the SQL code here
    """

    cursor.execute(sql_dump, multi=True)

    conn.commit()
    print("Database and tables created successfully!")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_db()
