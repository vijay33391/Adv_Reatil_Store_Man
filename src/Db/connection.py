import mysql.connector
from mysql.connector import Error
import sys
from src.logger import logging
from src.exception import CustomException

class DatabaseConnection:
    def __init__(self, host_name, user_name, user_password, database_name):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.database_name = database_name
        self.connection = None

    def create_connection(self):
        """
        Establishes a connection to the database and logs the result.
        """
        try:
            # Establishing the connection
            self.connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                password=self.user_password,
                database=self.database_name
            )
            
            # Check if the connection was successful
            if self.connection.is_connected():
                logging.info(f"Successfully connected to the database '{self.database_name}'")
            else:
                raise CustomException(f"Failed to connect to the database: {self.database_name}", sys)

        except Error as e:
            logging.error(f"An error occurred while connecting to the database: {str(e)}")
            raise CustomException(e, sys)

    def get_cursor(self):
        """
        Creates and returns a new cursor object if the connection is established.
        """
        if self.connection and self.connection.is_connected():
            return self.connection.cursor()
        else:
            raise CustomException("Connection is not established or has been closed.", sys)

    def commit(self):
        """
        Commits the current transaction to the database.
        """
        if self.connection and self.connection.is_connected():
            try:
                self.connection.commit()
                logging.info("Transaction committed successfully.")
            except Error as e:
                logging.error(f"Error while committing transaction: {str(e)}")
                raise CustomException(e, sys)
        else:
            raise CustomException("Connection is not established or has been closed.", sys)

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()  # Close the connection
            logging.info("Connection successfully closed.")
            self.connection = None
        else:
            logging.warning("Connection is already closed or not established.")
