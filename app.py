import sys
from src.exception import CustomException
import streamlit as st
from src.Db.connection import DatabaseConnection
from src.logger import logging
from src.Db.pages import crud_operations, home_page
from src.Db.pages.crud_operations import Features
from src.Dash_Board.dash_functionality import Load_data
from matplotlib import pyplot as plt
import plotly.express as px
import pandas as pd



def main():
    # Create a database connection instance
    try:
        db_connection = DatabaseConnection(
            host_name="localhost",
            user_name="root",
            user_password="vijay1311",
            database_name="Retail_Store"
        )
        db_connection.create_connection()  # Establish the connection once
        logging.info("Database connection is created successfully")

        # Create Features object with the database connection
        features = Features(db_connection)
        logging.info("Connection was established for features")
        refresh_data=Load_data(db_connection)

        # Sidebar Navigation
        st.sidebar.title("Navigation")
        page = st.sidebar.radio(
            "Choose a Page", 
            ["Home", "CRUD Operations", "Prediction Models", "Interactive Dashboard", "LLM Interaction"]
        )

        # Display the selected page
        if page == "Home":
            home_page.show_home_page()  # Call the function to display the home page

        elif page == "CRUD Operations":
            operation = st.sidebar.radio("Select CRUD Operation", ["ADD", "Search", "Update", "Delete"])

            if operation == "ADD":
                try:
                    st.title("Add The Items")
                    features.add_items()  # Use the features object to handle adding items
                   # last_transaction = features.fetch_last_transaction()
                    #st.write("Last Transaction:", last_transaction)
                except Exception as e:
                    st.error("An error occurred while adding items.")
                    logging.error(f"Error in ADD operation: {str(e)}")
                    raise CustomException(e,sys)

            elif operation == "Search":
                try:
                   st.title("Search the items")
                   features.search()
                # Add logic for searching items here
                except Exception as e:
                    st.error("An Eror was occured while searching")
                    logging.error("Erorr was occuring while searching")
                    raise CustomException(e,sys)
                

            elif operation == "Update":
                st.title("Update the items")
                st.subheader("Update Items - Feature Coming Soon!")
                st.write("The functionality to update items will be available shortly. Stay tuned for updates!")

                # Add logic for updating items here

            elif operation == "Delete":
                st.title("Delete the Item")
                st.subheader("Update and Delete Features - Coming Soon!")
                st.write("The functionalities to update and delete items will be available soon. Stay tuned for further updates!")

                # Add logic for deleting items here

        elif page == "Prediction Models":
            st.title("Prediction Models")
            st.write("""
    ### Sales and Trend Prediction Models

    In this section, we provide machine learning models that are designed to predict sales and trends based on historical data and various input features. These models utilize advanced algorithms to offer insights into future sales performance and trends.

    - **Sales Prediction Model**: Predicts future sales based on features such as work year, experience level, employment type, and other relevant factors. By inputting these variables, the model can help businesses forecast sales, manage resources, and plan strategies accordingly.
    
    - **Trend Prediction Model**: Provides predictions about upcoming trends in sales, customer behavior, and market dynamics. It analyzes patterns in historical data to make data-driven predictions, helping businesses stay ahead of trends and optimize their operations.

    ### Key Features:
    - **Interactive Input**: Users can provide real-time input, such as work year, experience level, employment type, etc., and get instant predictions.
    - **Accuracy**: The models are continuously improved to ensure accurate predictions based on the latest trends and data.
    - **Future Updates**: We are actively working on enhancing the prediction models. In the near future, we will integrate additional features and refine the models to make them more robust and reliable.
    
    ### How to Use:
    - **Step 1**: Enter the required input fields such as work year, experience level, employment type, etc.
    - **Step 2**: Click the **Predict Sales** button to get an instant prediction for future sales or trends.
    - **Step 3**: Stay tuned for further updates that will improve the accuracy and usability of these models.

    ### Upcoming Updates:
    - **Feature Expansion**: We plan to include more input parameters such as product categories, marketing spend, and external factors like seasonality to improve prediction accuracy.
    - **Model Optimization**: We are working on optimizing the algorithms to handle larger datasets and provide more reliable predictions.
    - **User Feedback**: We will be incorporating user feedback to further refine the models and make them more user-centric.

    ### Why Choose Our Prediction Models?
    These models are built using state-of-the-art machine learning algorithms and are tailored to provide actionable insights that can help businesses plan better and make informed decisions.
    
    Stay tuned as we continue to improve and expand our machine learning models for more precise and dynamic predictions!

    """)

            # Add prediction model code here

        elif page == "Interactive Dashboard":
            st.title("Interactive Dashboard")
            st.subheader("Navigate Through the 'Trends' and 'Visualization' Features")

            
            data = None
            

    # Add a refresh button in the sidebar
            refresh_button = st.sidebar.button("Refresh Data", key="refresh")

            if refresh_button:
                st.write("Refreshing the dashboard...")
                try:
            # Fetch updated data and save it to a CSV
                    data = refresh_data.save_data()  
                    st.success("Data refreshed successfully!")
                    st.info("Click 'Visualization' to view the trends.")
                    
                except Exception as e:
                    st.error(f"Error refreshing data: {e}")
                    data = None

    # Visualization button
  

# Assuming vis_button is a Streamlit button or trigger for the action
            vis_button = st.sidebar.button("Visualization", key="visualization")

# Check if the button is clicked
            if vis_button:
                if data is  None:
                    try:
            # Load the data from the saved CSV if not already loaded
                        data = pd.read_csv("D:/end_to_end/ml/retail_store/transactions.csv") 
                        st.success("Data loaded successfully for visualization!")

            
            
            # Display the filtered data
                        st.write("Latest Transection",data.tail(1))

                        st.write("Displaying Day-by-Day Sales")

                        # Ensure the 'Date' column is in datetime format
                        data['Date'] = pd.to_datetime(data['Date'])

                        # Group data by day and sum the Total_Amount
                        daily_sales = data.groupby('Date')['Total_Amount'].sum().reset_index()
                        fig = px.line(daily_sales, x='Date', y='Total_Amount', title='Daily Sales Over Time', markers=True)

                        st.plotly_chart(fig, use_container_width=True)

                        st.write("Displaying Total Income by Product Category")

                        # Group data by Product_Category and sum the Total_Amount
                        category_sales = data.groupby('Product_Category')['Total_Amount'].sum().reset_index()

                        # Plot the total income by product category using Plotly

                        fig = px.line(
                        category_sales, 
                        x='Product_Category', 
                        y='Total_Amount', 
                        title='Total Income by Product Category', 
                        markers=True
                        )

                        st.plotly_chart(fig, use_container_width=True)

                        st.markdown("""
                        ### Feature Update Coming Soon 🚀

                        We’re excited to share that a **Custom Filter** feature will soon be added to the Interactive Dashboard! This upcoming update will enable you to refine and analyze data more effectively by applying specific filters based on your preferences.

                        #### What to Expect:
                        - **Age Range Filtering**: Focus on data for a selected age range.
                        - **Category Selection**: Choose relevant product categories for targeted analysis.
                        - **Gender-Based Filtering**: Analyze data by specific demographics.

                        #### Why This Update?
                        This enhancement is aimed at providing:
                        - **Better Insights**: Narrow down data to what matters most.
                        - **Improved Usability**: Simplify your data exploration process.
                        - **Future Flexibility**: Customize your dashboard experience like never before.

                        Stay tuned for this exciting update, and let us know if there are specific filters you’d love to see added! 🎉
                    """)

                    except Exception as e:
                            st.error(f"Error loading data for visualization: {e}")
                            data = None

              
                            

               
                
            
          

        elif page == "LLM Interaction":
            st.title("LLM Interaction")
            st.subheader("This feature update comeing Soon")
            st.write("""
    ### Interact with the Database using Natural Language Queries

    Welcome to the **LLM Interaction** page, where you can interact with our database using natural language queries. The system leverages a **Large Language Model (LLM)** to understand your questions and provide meaningful responses by querying the database or performing specific tasks.

    This feature allows you to:
    - **Ask questions** about the data stored in the database, such as retrieving specific records or aggregates.
    - **Request insights** based on your data, such as sales trends, predictions, and analysis.
    - **Receive personalized responses**, making it easier to understand complex data without needing to know SQL or programming languages.

    ### How It Works:
    - Simply type your **query** in the text box below (e.g., "Show me the sales data for January 2024" or "What were the top-selling products last month?").
    - The system will use a **powerful LLM** to translate your query into an appropriate database command or action.
    - Based on your request, you will either get **data** retrieved from the database or receive **insights** generated from machine learning models (e.g., sales predictions).

    ### Key Features:
    - **Natural Language Understanding**: The system is capable of interpreting complex questions in plain English (or any language the model supports).
    - **Database Querying**: Queries like "Show me the top 5 products with the highest sales" or "What was the average sales in Q1?" will be processed directly.
    - **Sales Prediction**: In addition to querying data, you can ask for predictions like "Predict the sales for next month".
    - **Customizable**: Over time, the system will get more accurate and tailored to your specific needs based on the interactions and feedback.

    ### Example Queries:
    - "What were the total sales for 2023?"
    - "Show me sales data for Product X in January."
    - "Can you predict next month's sales?"
    - "What are the average sales for each region?"

    ### Next Steps:
    Enter a question in the text box below and see how the system translates your natural language input into meaningful results.

    """)
            # Add LLM interaction code here

    except Exception as e:
        st.error("Failed to initialize the application due to a database connection error.")
        logging.error(f"Database connection error: {str(e)}")
    
    finally:
        # Ensure the database connection is closed when the app exits
        if 'db_connection' in locals() and db_connection.connection:
            db_connection.close_connection()
            logging.info("Database connection closed successfully.")

if __name__ == "__main__":
    main()
