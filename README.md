# 218_finalProject

## Operations Testing 
This repository contains a Python-based test suite for validating the functionality of arithmetic operations including addition, subtraction, multiplication, and division.

--- 
## Test Coverage

**Functions Tested:**
1. Addition (add):
Positive and negative integers
Floats
Edge case: Adding zero
![Alt text](<Screenshot from 2024-12-19 20-49-07.png>)

**Subtraction (subtract):**
Positive and negative integers
Floats
Edge case: Subtracting zero
![Alt text](<Screenshot from 2024-12-19 20-49-15.png>)

**Multiplication (multiply):**
Positive and negative integers
Floats
Edge case: Multiplying by zero
![Alt text](<Screenshot from 2024-12-19 20-49-19.png>)

**Division (divide):**
Positive and negative integers
Floats
Edge case: Division by zero (raises a ValueError)
![Alt text](<Screenshot from 2024-12-19 20-49-29.png>)

--- 

## FastAPI Testing Framework
A robust testing framework for FastAPI applications with PostgreSQL database integration, featuring end-to-end testing capabilities using Playwright.

## Features
- PostgreSQL database integration with SQLAlchemy
- Comprehensive pytest fixtures for database testing
- End-to-end testing support using Playwright
- Automated FastAPI server management for testing
- Faker integration for generating test data
- Secure password handling with Passlib and bcrypt

## Database Fixtures
- engine: Creates SQLAlchemy engine for test database
- SessionLocal: Provides session factory for database operations
- db_session: Creates isolated database sessions for each test
- setup_database: Handles database schema creation and cleanup
- test_user: Creates a test user with fake data

## Usage Examples
**Database Testing**
```
pythonCopydef test_create_user(db_session, test_user):
    assert test_user.id is not None
    assert test_user.email is not None
    # Add more assertions as needed
```
--- 
## Python Calculator Testing
A comprehensive testing suite for a calculator application using pytest, demonstrating best practices in Python testing including parameterized testing and type hinting.

## Features
- Basic arithmetic operations (add, subtract, multiply, divide)
- Comprehensive test coverage with pytest
- Type-annotated test functions
- Parameterized tests for multiple test cases
- Error handling for division by zero

## Example Test Code
```
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    result = add(a, b)
    assert result == expected
```

--- 
## Calculator API
A robust FastAPI-based calculator service with database integration for calculation history tracking. Features comprehensive testing using pytest, SQLAlchemy for database operations, and FastAPI's TestClient for API testing.

## Features
- RESTful API endpoints for basic arithmetic operations
- Database integration for user management and calculation history
- Comprehensive test coverage
- Type-safe operations
- Error handling for edge cases (e.g., division by zero)

## Technical Stack
- FastAPI
- SQLAlchemy
- pytest
- PostgreSQL
- Pydantic

1. API Tests
```
def test_add_api(client):
    response = client.post('/add', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.json()['result'] == 15
```
2. Database Tests
```
def test_insert_calculation(test_user, db_session):
    calculation = Calculation(
        user_id=test_user.id,
        type='addition',
        value_a=1,
        value_b=2
    )
    db_session.add(calculation)
    db_session.commit()
    
    assert calculation in test_user.calculations
```
## Usage Example 
```
import requests

# Addition example
response = requests.post('http://localhost:8000/add', json={'a': 10, 'b': 5})
print(response.json())  # {'result': 15}
```
