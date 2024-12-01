import mysql.connector  # Import mysql.connector module
from mysql.connector import Error  # Import Error for exception handling

class CreateSchema:
    @staticmethod  # Make it a static method since it doesn't use instance variables
    def create_database(host_name, user_name, password, database_name):
        # Build the connection
        try:
            connection = mysql.connector.connect(
                host=host_name,  # Use `host` instead of `host_name`
                user=user_name,  # Use `user` instead of `user_name`
                password=password
            )
            # Create a Database
            if connection.is_connected():
                # Create cursor
                cursor = connection.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
                print(f"Database '{database_name}' created successfully")

        except Error as e:  # Catch the specific `Error` exception
            print("Problem encountered while creating the database:", e)
        
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("Successfully closed the database connection")

    @staticmethod
    def create_table(host_name, user_name, password, database_name):
        # Create the connection
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=password,
                database=database_name  # Specify the database
            )
            if connection.is_connected():
                cursor = connection.cursor()
                table_query = """ 
CREATE TABLE IF NOT EXISTS Transactions (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Transaction_ID INT,
    Date DATE,
    Customer_ID INT,
    Gender VARCHAR(20),
    Age INT,
    Product_Category VARCHAR(100),
    Quantity INT,
    Price_per_Unit DECIMAL(10, 2),
    Total_Amount DECIMAL(10, 2)
)
"""

                cursor.execute(table_query)
                print("Table 'Transactions' created successfully")
        
        except Error as e:
            print("Problem occurred while creating the table:", e)
        
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("Successfully closed the table connection")

# Parameters
host = "localhost"
user_name = "root"
password = "vijay1311"
database_name = "Retail_Store"

# Object instantiation and method calls
obj = CreateSchema()
obj.create_database(host, user_name, password, database_name)
obj.create_table(host, user_name, password, database_name)
