import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.Db.connection import DatabaseConnection
import os
import sys
from datetime import datetime
import streamlit as st


class Load_data():

    def __init__(self, db_connection: DatabaseConnection): 
        self.db_connection = db_connection
        logging.info("For refresh, the data connection was established.")

    def refresh_data(self):
        """
        Fetches all data from the 'transactions' table.
        Returns:
            list: Rows of the 'transactions' table.
        Raises:
            CustomException: If an error occurs during data retrieval.
        """
        try:
            # Get a database cursor to execute queries
            cursor = self.db_connection.get_cursor()

            # SQL query to select all data from the transactions table
            select_query = "SELECT * FROM transactions"
            cursor.execute(select_query)

            # Fetch all rows from the table
            rows = cursor.fetchall()

            # Close the cursor after use
            cursor.close()
            return rows
        except Exception as e:
            # Log and raise a custom exception if an error occurs
            logging.error(f"Error occurred while refreshing data: {str(e)}")
            raise CustomException(e, sys)

    def save_data(self):
        """
        Creates a CSV file for the 'transactions' table. 
        If the file already exists, appends new transactions to the end.
        If the file does not exist, creates a new CSV file with all transactions.
        """
        try:
            # Step 1: Fetch the latest data from the 'transactions' table
            data = self.refresh_data()
            logging.info("Data fetched successfully for saving to CSV.")
            
            # Step 2: Define the file name and path
            file_name = "transactions.csv"
            file_path = os.path.join(os.getcwd(), file_name)

            # Step 3: Define column names for the DataFrame
            columns =["ID","Transaction_ID", "Date", "Customer_ID", "Gender", "Age", "Product_Category", "Quantity", "Price_per_Unit", "Total_Amount"]

            
            # Convert the fetched data into a DataFrame
            df = pd.DataFrame(data, columns=columns)

            if os.path.exists(file_path):
                # Step 4: If file exists, read the existing file
                existing_df = pd.read_csv(file_path)
                logging.info("Existing CSV file found. Appending new transactions.")
                
                # Step 5: Concatenate new data with existing data
                updated_df = pd.concat([existing_df, df], ignore_index=True)

                # Remove duplicate transactions based on 'TransactionID'
                updated_df.drop_duplicates(subset=['Transaction_ID'], keep='last', inplace=True)

                # Save the updated data back to the CSV
                updated_df.to_csv(file_path, index=False)
                logging.info("New transactions appended successfully.")
                st.title("Data Is Up To Date Know")
            else:
                # Step 6: If file does not exist, create it and save the data
                df.to_csv(file_path, index=False)
                logging.info("CSV file created and data saved successfully.")
        except Exception as e:
            # Step 7: Log any errors and raise a custom exception
            logging.error(f"Error occurred while saving data to CSV: {str(e)}")
            raise CustomException(e, sys)




class Visualization:
    def v_filters(self):
        try:
            # Load the data from the saved CSV if not already loaded
            data = pd.read_csv("D:/end_to_end/ml/retail_store/transactions.csv")
            st.success("Data loaded successfully for visualization!")

            # Data Cleaning
            data["Age"] = pd.to_numeric(data["Age"], errors='coerce')  # Ensure Age is numeric, handle errors
            data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  # Convert Date to datetime, handle errors
            data['Product_Category'].fillna('Unknown', inplace=True)
            data['Gender'].fillna('Unknown', inplace=True)
            data["Age"].fillna(0, inplace=True)

            # Sidebar Filters
            st.sidebar.header("Filter Options")
            age_filter = st.sidebar.slider("Select Age Range", min_value=0, max_value=100, value=(0, 100))
            category_filter = st.sidebar.multiselect(
                "Select Categories", 
                options=data['Product_Category'].unique(),
                default=data['Product_Category'].dropna().unique()
            )
            gender_filter = st.sidebar.multiselect(
                "Select Gender", 
                options=data['Gender'].unique(),
                default=data["Gender"].dropna().unique()
            )

            # Apply Filters to the Data
            filtered_data = data[
                (data['Age'].between(age_filter[0], age_filter[1])) &
                (data['Product_Category'].isin(category_filter)) &
                (data['Gender'].isin(gender_filter))
            ]

            # Save the filtered data to session state
            st.session_state.filtered_data = filtered_data

            # Display the filtered data
            st.subheader("Filtered Data")
            st.write(filtered_data)

        except FileNotFoundError:
            st.error("The specified CSV file was not found. Please check the file path.")
        except Exception as e:
            logging.info("Error occurred while applying filters.")
