# Flask API Documentation

## Overview
This project is a simple Flask-based API designed to demonstrate basic RESTful operations.

## Features
- Lightweight and easy to use.
- Supports CRUD operations.
- Built with Python and Flask.

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd Flask
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```bash
    python app.py
    ```
2. Access the API at `http://127.0.0.1:5000`.

## Endpoints
| Method | Endpoint       | Description          |
|--------|----------------|----------------------|
| GET    | `/items`       | Retrieve all items. |
| POST   | `/items`       | Create a new item.  |
| PUT    | `/items/<id>`  | Update an item.     |
| DELETE | `/items/<id>`  | Delete an item.     |
