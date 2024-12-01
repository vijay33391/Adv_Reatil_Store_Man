import sys
from src.Db.connection import DatabaseConnection
from src.logger import logging
from src.exception import CustomException
import streamlit as st
import pandas as pd
from datetime import datetime

class Features:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        logging.info("Features connection was established")

    def fetch_last_3_transactions(self):
        try:
            cursor = self.db_connection.get_cursor()  # Get a new cursor
            select_query = "SELECT * FROM transactions ORDER BY ID DESC LIMIT 3"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            cursor.close()  # Close the cursor after use
            return rows
        except Exception as e:
            logging.error(f"Error occurred while fetching the last 3 transactions: {str(e)}")
            raise CustomException(e,sys)

    def fetch_last_transaction(self):
        try:
            cursor = self.db_connection.get_cursor()  # Get a new cursor
            select_query = "SELECT * FROM transactions ORDER BY ID DESC LIMIT 1"
            cursor.execute(select_query)
            row = cursor.fetchone()
            cursor.close()  # Close the cursor after use
            return row
        except Exception as e:
            logging.error(f"Error occurred while fetching the last transaction: {str(e)}")
            raise CustomException(e,sys)

    def add_items(self):
        cursor = None
        results=None
        try:
            cursor = self.db_connection.get_cursor()  # Use get_cursor for consistency

            # Streamlit input fields for the user to enter transaction data
            transaction_id = st.number_input("Transaction ID", min_value=1)
            date = st.date_input("Date", value=datetime.today().date())
            customer_id = st.number_input("Customer ID", min_value=1)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            age = st.number_input("Age", min_value=0, max_value=100, step=1)
            product_category = st.selectbox("Poduct category",['Beauty',
            'Clothing',
            'Electronics',
            'Groceries',
            'Furniture',
            'Books',
            'Sports',
            'Toys',
            'Automotive',
            'Jewelry'])
            
            quantity = st.number_input("Quantity", min_value=1)
            price_per_unit = st.number_input("Price per Unit", min_value=0.01, format="%.2f")
            total_amount = quantity * price_per_unit

            # Display the total amount to the user
            st.write(f"Total Amount: {total_amount:.2f}")

            # Button to submit the transaction data
            if st.button("Submit"):
                insert_query = """
                INSERT INTO transactions 
                (Transaction_ID, Date, Customer_ID, Gender, Age, Product_Category, Quantity, Price_per_Unit, Total_Amount) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (
                    transaction_id,
                    date,
                    customer_id,
                    gender,
                    age,
                    product_category,
                    quantity,
                    price_per_unit,
                    total_amount
                ))

                # Commit the transaction to the database
                self.db_connection.commit()
                st.success("Transaction data inserted successfully!")
                
                logging.info("Insert Was Done")
                results=self.fetch_last_transaction()
            if results:
                # If result is a tuple, convert it into a DataFrame
                columns = ["ID","Transaction_ID", "Date", "Customer_ID", "Gender", "Age", "Product_Category", "Quantity", "Price_per_Unit", "Total_Amount"]
                df = pd.DataFrame([results], columns=columns)  # Wrap results in a list for DataFrame
                st.dataframe(df)


        except Exception as e:
            st.error(f"Error: {e}")
            logging.error(f"Error occurred while adding and displaying transactions: {str(e)}")
            raise CustomException(e,sys)
        finally:
            if cursor:
                cursor.close()  # Ensure the cursor is closed in all cases

    def search(self):
        try:
        # Initialize variables
            cursor = None
            results = None
        
        # Display input box and button
            searching_with_input = st.number_input("Enter The Transaction ID", step=1, min_value=0)
            search_button_pressed = st.button('SEARCH CUSTOMER')
        
        # Execute query only if button is pressed
            if search_button_pressed and searching_with_input:
            # Get the database cursor
                cursor = self.db_connection.get_cursor()
            
            # Prepare and execute the query
                query = "SELECT * FROM Transactions WHERE Transaction_ID = %s"
                cursor.execute(query, (searching_with_input,))
            
            # Fetch and display results
                results = cursor.fetchall()
            if results:
                columns = [desc[0] for desc in cursor.description]
                # Convert results to DataFrame
                df = pd.DataFrame(results, columns=columns)
                # Display the DataFrame in Streamlit
                st.dataframe(df)
            else:
                st.warning("No records found for the given Transaction ID Zero.")
        except Exception as e:
            st.error("An error occurred while searching for the customer.")
            logging.error(f"Error occurred while searching for the customer: {e}")
            raise CustomException(e, sys)
        finally:
        # Ensure the cursor is closed properly
            if cursor:
                cursor.close()
