import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# API Endpoint and API Key
API_ENDPOINT = "https://api.groq.com/openai/v1"
API_KEY = os.getenv("API_KEY") 

# Define arithmetic functions for basic operations
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Handles division by zero."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Function to call the Groq API
def call_groq_function(prompt, functions, model="llama3-8b-8192"):
    """
    Sends a user prompt and function definitions to the Groq API.
    Returns the function name and arguments if the API calls a function.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",  # API authorization
        "Content-Type": "application/json",   # Ensure JSON format for the payload
    }

    payload = {
        "model": model,  # Specify the model to use
        "messages": [{"role": "user", "content": prompt}],  # User's input message
        "functions": functions,  # Define available functions
        "function_call": "auto",  # Let the model decide whether to call a function
    }

    try:
        # Send the POST request to the Groq API
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the JSON response

        # Check if the model called a function
        if "function_call" in data["choices"][0]["message"]:
            function_name = data["choices"][0]["message"]["function_call"]["name"]
            arguments = json.loads(data["choices"][0]["message"]["function_call"]["arguments"])
            return function_name, arguments

        return None, None  # No function call made

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")  # Print error if the request fails
        return None, None

# Main console application
def console_chat():
    """
    A console-based chat application that uses the Groq API
    to perform basic arithmetic operations.
    """
    print("Welcome to the Groq Function Chat!")
    print("You can ask the system to perform addition, subtraction, multiplication, or division.")
    print("Type 'exit' or 'quit' to end the session.")

    # Define the functions to be used with the Groq API
    functions = [
        {
            "name": "add",
            "description": "Add two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "The first number."},
                    "b": {"type": "number", "description": "The second number."}
                },
                "required": ["a", "b"]
            },
        },
        {
            "name": "subtract",
            "description": "Subtract two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "The first number."},
                    "b": {"type": "number", "description": "The second number."}
                },
                "required": ["a", "b"]
            },
        },
        {
            "name": "multiply",
            "description": "Multiply two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "The first number."},
                    "b": {"type": "number", "description": "The second number."}
                },
                "required": ["a", "b"]
            },
        },
        {
            "name": "divide",
            "description": "Divide two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "The first number."},
                    "b": {"type": "number", "description": "The second number."}
                },
                "required": ["a", "b"]
            },
        }
    ]

    # Start the chat loop
    while True:
        prompt = input("You: ")  # Get input from the user
        if prompt.lower() in ["exit", "quit"]:  # Exit condition
            print("Goodbye!")
            break

        # Call the Groq API to determine the function and arguments
        function_name, arguments = call_groq_function(prompt, functions)

        # If a function call was made, execute the corresponding function
        if function_name and arguments:
            if function_name == "add":
                result = add(arguments["a"], arguments["b"])
            elif function_name == "subtract":
                result = subtract(arguments["a"], arguments["b"])
            elif function_name == "multiply":
                result = multiply(arguments["a"], arguments["b"])
            elif function_name == "divide":
                result = divide(arguments["a"], arguments["b"])
            else:
                result = "Error: Unknown function called"

            print(f"Result: {result}")
        else:
            print("No function call was made or an error occurred.")

# Entry point of the script
if __name__ == "__main__":
    console_chat()
