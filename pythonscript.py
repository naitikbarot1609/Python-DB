import mysql.connector
from mysql.connector import Error

def execute_sql_script(file_path, connection):
    """
    Execute an SQL script from a file.
    
    :param file_path: Path to the SQL script.
    :param connection: Active MySQL connection object.
    """
    try:
        cursor = connection.cursor()
        
        # Read the SQL script
        with open(file_path, 'r') as sql_file:
            sql_script = sql_file.read()
        
        # Split the script into individual SQL commands (statements)
        sql_commands = sql_script.split(';')
        
        # Execute each command
        for command in sql_commands:
            if command.strip():  # Execute non-empty commands
                cursor.execute(command)
        
        # Commit the changes
        connection.commit()
        print("Schema updated successfully!")
    
    except Error as e:
        print(f"Error while executing SQL script: {e}")
        connection.rollback()  # Roll back the changes in case of error
    
    finally:
        cursor.close()

def connect_and_execute():
    """
    Connect to the MySQL database and execute the SQL script for schema changes.
    """
    try:
        # Define your database connection parameters
        connection = mysql.connector.connect(
            host='naitik.mysql.database.azure.com',
            user='rootdb',
            password='qwerty@1234',
            database='db1'
        )
        
        if connection.is_connected():
            print("Successfully connected to the database")
            
            # Path to your SQL script
            sql_file_path = 'C:\\Users\\Lenovo\\Desktop\\data_automation\\Python-DB\\schema_changes_git.sql'
            
            # Execute the SQL script
            execute_sql_script(sql_file_path, connection)
    
    except Error as e:
        print(f"Error connecting to the database: {e}")
    
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connect_and_execute()
