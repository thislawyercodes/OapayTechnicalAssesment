# Customer Orders API

A simple Django REST API for managing customer orders.

## Features
- Create customers
- Create orders for customers
- Retrieve all orders for a specific customer
- PostgreSQL configured as the database
- Swagger API documentation setup

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/thislawyercodes/OapayTechnicalAssesment.git
cd OapayTechnicalAssesment
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root and set up your PostgreSQL database details:
```env
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/your_db_name
```

### 5. Apply Migrations
```sh
python manage.py migrate
```

### 6. Run the Development Server
```sh
python manage.py runserver
```

## API Endpoints
| Method | Endpoint | Description |
|--------|-------------------------|--------------------------------|
| POST | `/customers/` | Create a new customer |
| POST | `/orders/` | Create a new order |
| GET  | `/customers/{customer_id}/orders/` | Retrieve orders for a customer |

## Swagger Documentation
Once the server is running, visit:
```
http://127.0.0.1:8000/swagger/
```

## How to Test
### Running Unit Tests
To run unit tests, execute the following command:
```sh
python manage.py test
```
For more verbose output:
```sh
python manage.py test -v 2
```

### Testing API Endpoints with cURL
Create a customer:
```sh
curl -X POST http://127.0.0.1:8000/customers/ -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}'
```

Retrieve orders for a customer:
```sh
curl -X GET http://127.0.0.1:8000/customers/1/orders/
```

## Limitations
- **No Authentication**: Endpoints are not secured; any user can access them.
- **No Pagination**: Large datasets may impact performance.
- **Basic Error Handling**: Needs improvement for robustness.

## Contributing
Feel free to fork the repository and submit pull requests!

