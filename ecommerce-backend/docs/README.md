# README for the E-commerce Backend API

## Overview

This project is an e-commerce backend built with Django, utilizing PostgreSQL as the database, JWT for user authentication, and Swagger/OpenAPI for API documentation. The backend supports CRUD operations for products, categories, orders, and user authentication, along with features for filtering, sorting, and pagination.

## Features

- **User Authentication**: Secure user registration and login using JWT.
- **Product Management**: Create, read, update, and delete products with filtering and sorting capabilities.
- **Category Management**: Manage product categories with CRUD operations.
- **Order Management**: Handle customer orders with detailed tracking.
- **Shopping Cart**: Manage user shopping carts with the ability to add, remove, and update items.
- **API Documentation**: Automatically generated API documentation using Swagger/OpenAPI.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Docker (optional, for containerized setup)

### Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd ecommerce-backend
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database:

   - Create a new database for the project.
   - Update the `.env` file with your database credentials.

5. Run migrations to set up the database schema:

   ```
   python manage.py migrate
   ```

6. Create a superuser to access the Django admin:

   ```
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

### API Documentation

The API documentation is available at `/api/docs/` once the server is running. You can explore the available endpoints, request parameters, and response formats.

## Usage

- **Authentication**: Use the `/auth/login/` endpoint to obtain a JWT token for authenticated requests.
- **Products**: Access the `/products/` endpoint for product-related operations.
- **Categories**: Use the `/categories/` endpoint to manage product categories.
- **Orders**: Access the `/orders/` endpoint for order management.
- **Cart**: Use the `/cart/` endpoint to manage the shopping cart.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.