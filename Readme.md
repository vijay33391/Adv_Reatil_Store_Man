# CRUD Application with MySQL and Python

## Project Overview
This project is a CRUD (Create, Read, Update, Delete) application built using Python and MySQL. It includes logging and custom exception handling to ensure robust error management. The application was successfully developed and tested in a local environment, but challenges were encountered while deploying it to the cloud.

## Features
- Perform CRUD operations using MySQL and Python.
- Implement logging for debugging and tracking events.
- Use custom exceptions for better error handling.
- Designed to work with a local MySQL database (future scope: migration to cloud database).

## Technologies Used
- **Programming Language:** Python
- **Database:** MySQL
- **Libraries:**
  - `mysql-connector-python` (for database interaction)
  - `logging` (for logging events and errors)
  - Custom exception handling

## Installation & Setup
### Prerequisites
Ensure that you have the following installed on your system:
- Python (3.x recommended)
- MySQL Server
- Required Python libraries (install using the command below):
  ```bash
  pip install mysql-connector-python
  ```

### Database Configuration
1. Create a MySQL database and user with appropriate privileges.
2. Update the database configuration in the Python script:
   ```python
   db_config = {
       'host': 'localhost',
       'user': 'your_username',
       'password': 'your_password',
       'database': 'your_database'
   }
   ```

### Running the Application
Execute the Python script to perform CRUD operations:
```bash
python app.py
```

## Logging & Custom Exceptions
- Logs are stored in `app.log` for debugging and tracking.
- Custom exceptions are implemented to handle specific errors gracefully.

## Deployment Challenge & Future Scope
The application works locally but encountered deployment challenges due to database connectivity issues when migrating to the cloud. Future steps include:
- Configuring a cloud-based MySQL service.
- Updating connection settings to support remote database access.
- Ensuring proper security configurations for cloud deployment.



---
This README provides a structured overview of the project and highlights deployment challenges. Let me know if you want any modifications!

