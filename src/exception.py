import sys
from src.logger import logging

def get_detailed_error_message(error, error_context: sys):
    """
    Generate a detailed error message including the script file name and line number where the error occurred.
    """
    # Extract the traceback from the error context
    _, _, trace = error_context.exc_info()
    script_name = trace.tb_frame.f_code.co_filename  # Name of the script where the error occurred
    line_number = trace.tb_lineno  # Line number of the error
    # Create a detailed error message
    detailed_message = f"Error in script [{script_name}] at line [{line_number}]: {str(error)}"
    return detailed_message

class CustomException(Exception):
    def __init__(self, original_error, error_context: sys):
        """
        Initialize the custom exception with a detailed error message.
        """
        # Generate the detailed error message
        detailed_message = get_detailed_error_message(original_error, error_context)
        # Initialize the base Exception with the detailed message
        super().__init__(detailed_message)
        # Save the detailed message as an attribute for later use
        self.detailed_message = detailed_message

    def __str__(self):
        return self.detailed_message

'''# Example usage
if __name__ == "__main__":
    try:
        result = 1 / 0  # This will raise ZeroDivisionError
    except Exception as e:
        logging.info("A division by zero error occurred.")
        raise CustomException(e, sys)'''
