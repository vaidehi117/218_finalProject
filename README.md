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