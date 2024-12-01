import mysql.connector
from mysql.connector import Error


class InsertData:
    @staticmethod
    def dummy_data(host_name, user_name, password, db_name, table_name):
        connection = None  # Initialize connection to None
        try:
            # Establish the connection
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=password,
                database=db_name
            )

            if connection.is_connected():
                cursor = connection.cursor()
                
                # Insert query for the Transactions table
                insert_query = f"""
                INSERT INTO `{table_name}` 
                (Transaction_ID, Date, Customer_ID, Gender, Age, Product_Category, Quantity, Price_per_Unit, Total_Amount) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                # Dummy data to insert (Ensure Price_per_Unit and Total_Amount are decimals)
                data = [
                    (1, '2023-11-24', 1, 'Male', 34, 'Beauty', 3, 50.00, 150.00),
                    (2, '2023-02-27', 2, 'Female', 26, 'Clothing', 2, 500.00, 1000.00),
                    (3, '2023-01-13', 3, 'Male', 50, 'Electronics', 1, 30.00, 30.00),
                    (4, '2023-05-21', 4, 'Male', 37, 'Clothing', 1, 500.00, 500.00),
                    (5, '2023-05-06', 5, 'Male', 30, 'Beauty', 2, 50.00, 100.00),
                    (6, '2023-04-25', 6, 'Female', 45, 'Beauty', 1, 30.00, 30.00)
                ]

                # Insert each row of data
                cursor.executemany(insert_query, data)
                connection.commit()  # Commit changes to the database
                print("Data inserted successfully.")

        except Error as e:
            print("Error occurred when inserting data:", e)

        finally:
            if connection is not None and connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")

# Usage example
InsertData.dummy_data(
    host_name="localhost",
    user_name="root",
    password="vijay1311",
    db_name="retail_store",
    table_name="transactions"
)
