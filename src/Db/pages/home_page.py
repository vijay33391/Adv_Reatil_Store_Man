# home_page.py

import streamlit as st

def show_home_page():
    st.title("Retail Store Management System")

    st.markdown("""
        Welcome to the **Retail Store Management System**, an all-in-one platform to streamline data management, 
        leverage advanced machine learning insights, and interact with your store data using natural language.

        ### Overview

        This system is designed to make managing your retail operations easier, with dedicated tools for CRUD operations, 
        predictive modeling, and interactive data exploration. With a simple yet powerful interface, our system allows 
        you to focus on key aspects of your business and make data-informed decisions effortlessly.

        - **Efficient Data Management (CRUD)**: A dedicated page allows you to easily add, search, update, and delete 
          data entries. With streamlined data management, you can keep your inventory, sales, and customer information organized and up to date.

        - **Machine Learning Predictions**: Access advanced machine learning models that generate predictions based on your 
          historical data, helping you make strategic decisions for inventory planning, sales forecasting, and customer segmentation.

        - **Interactive Dashboard**: Visualize key metrics and trends in a dynamic dashboard. The dashboard gives you a clear, 
          data-driven view of store performance, highlighting important insights like sales trends, seasonal demand patterns, and popular products.

        - **Natural Language Interaction with LLM**: Our system includes a language model (LLM) feature that lets you interact with 
          your database using natural language. Simply ask questions like, "What were the highest-selling items last quarter?" 
          or "Which products have the most stock left?" to get quick answers without writing any code.

        ### Key Features

        - **CRUD Operations**: A dedicated page for efficient Add, Search, Update, and Delete functions, allowing easy data management.
        - **Predictive Modeling**: Access machine learning models tailored for retail predictions, such as sales forecasting and customer trend analysis.
        - **Visual Dashboard**: A dashboard providing intuitive visualizations for sales, inventory, and customer trends to help you make data-informed decisions.
        - **LLM-based Data Interaction**: Use natural language queries to interact with your data and uncover insights without the need for technical skills.

        ### Getting Started

        Use the sidebar to navigate between sections:
        - **CRUD Operations**: Manage your store's data with efficient Create, Read, Update, and Delete functions.
        - **Prediction Models**: Leverage machine learning models to forecast sales and analyze customer trends.
        - **Interactive Dashboard**: Visualize performance metrics and trends for a quick overview of store health.
        - **LLM Interaction**: Ask questions and interact with your database in natural language to gain instant insights.

        This system equips you with the tools needed to manage retail data effectively, make strategic decisions, and 
        stay ahead in a dynamic retail landscape.
    """)
