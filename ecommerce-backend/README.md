# eCommerce Backend Project

This project is an e-commerce backend built with Django, utilizing PostgreSQL as the database, JWT for user authentication, and Swagger/OpenAPI for API documentation. The application supports CRUD operations, filtering, sorting, pagination, and database optimization.

## Features

- **User Authentication**: Secure user registration and login using JWT.
- **Product Management**: Create, read, update, and delete products and categories.
- **Order Management**: Manage customer orders efficiently.
- **Shopping Cart**: Add, update, and remove items from the shopping cart.
- **API Documentation**: Automatically generated API documentation using Swagger/OpenAPI.
- **Database Optimization**: Efficient queries with filtering, sorting, and pagination.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt
- Docker (for containerization)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd ecommerce-backend
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Copy `.env.example` to `.env` and fill in the required variables.

5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the API Documentation**:
   Navigate to `http://localhost:8000/api/docs/` to view the Swagger documentation.

## Docker Setup

To run the application using Docker, use the following commands:

1. **Build the Docker Image**:
   ```bash
   docker-compose build
   ```

2. **Run the Docker Containers**:
   ```bash
   docker-compose up
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.