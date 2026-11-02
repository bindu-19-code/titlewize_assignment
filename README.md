# Bookmark Management API

## Project Overview

The Bookmark Management API is a RESTful API developed using Python, Django, and Django REST Framework.

It allows authenticated users to create, view, update, and delete their bookmarks. Each user can access only their own bookmarks.

The API also supports tag-based filtering, pagination, URL validation, duplicate URL prevention, and bookmark statistics.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Requests
- python-dotenv

## Features

- Token-based and session-based authentication
- Create, retrieve, update, and delete bookmarks
- User-specific bookmark access
- Tag-based filtering
- Pagination with 10 bookmarks per page
- URL validation (HTTP and HTTPS)
- Prevention of duplicate URLs for the same user
- Bookmark statistics with count per tag
- Automated API tests using APITestCase
- API consumption using Python Requests

## Project Structure

```text
bookmark_project/
├── config/
├── bookmarks/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── test_api.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/titlewize_assignment.git
cd bookmark_project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the environment variable

Create a `.env` file in the project root directory and add:

```env
DJANGO_SECRET_KEY=your-secret-key
```

Replace `your-secret-key` with a newly generated Django secret key.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the instructions to create your username and password.

### 8. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

`http://127.0.0.1:8000/`

## API Endpoints

| HTTP Method | Endpoint                | Description                 |
| ----------- | ----------------------- | --------------------------- |
| POST        | `/api/token/`           | Obtain authentication token |
| GET         | `/api/bookmarks/`       | List user's bookmarks       |
| POST        | `/api/bookmarks/`       | Create a bookmark           |
| GET         | `/api/bookmarks/<id>/`  | Retrieve a bookmark         |
| PATCH       | `/api/bookmarks/<id>/`  | Partially update a bookmark |
| PUT         | `/api/bookmarks/<id>/`  | Update a bookmark           |
| DELETE      | `/api/bookmarks/<id>/`  | Delete a bookmark           |
| GET         | `/api/bookmarks/stats/` | Get bookmark counts per tag |

### Tag Filtering

Use the following query parameter to filter bookmarks:

```text
GET /api/bookmarks/?tag=Python
```

### Pagination

The API returns 10 bookmarks per page.

Example:

```text
GET /api/bookmarks/?page=2
```

## Authentication

The API uses token authentication.

Obtain a token by sending a POST request to:

```text
/api/token/
```

Provide your username and password.

For subsequent requests, include the token in the request header:

```text
Authorization: Token <your-token>
```

Session authentication is also supported through the Django REST Framework Browsable API.

## Running the API Consumption Script

The `test_api.py` script demonstrates how to consume the API using Python Requests.

Run:

```bash
python test_api.py
```

The script demonstrates authentication, bookmark creation, listing, tag filtering, and validation error handling.

## Running Automated Tests

Run the following command:

```bash
python manage.py test bookmarks
```

The tests cover user-specific bookmark access and duplicate URL validation.

## Author

**Bindu K Reddy**
