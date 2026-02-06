Django Library Management System (Forms + APIs)
This project is a Django-based Library Management System that combines:

HTML templates + vanilla JS for the frontend
JSON-based POST/GET APIs (no frontend framework)
Django REST Framework + JWT authentication for login/register
It is clearly built as a learning project to understand how Django forms, class-based views, search APIs, and authentication work together.

Actual Project Structure (From ZIP)
mysite_fixed/
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
└── webapp/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    ├── migrations/
    ├── static/
    │   ├── auhtor.js
    │   ├── books.js
    │   ├── login.js
    │   └── pub.js
    └── templates/
        ├── base.html
        ├── home.html
        ├── login.html
        ├── author.html
        ├── book.html
        └── Publisher.html
Database Models
Author
fname
lname
email
Publisher
name
country
website
Book
title
publish_date
author → ManyToMany (Author)
publisher → ForeignKey (Publisher)
Frontend Pages (Templates)
URL	Template	Purpose
/	home.html	Landing page
/login/	login.html	Login page (JWT)
/author/	author.html	Add author + autocomplete
/publisher/	Publisher.html	Add publisher + search
/book/	book.html	Add book + search
All forms submit JSON using fetch(), not Django form POSTs.

API Endpoints (Exact Behavior)
➤ Author API
POST /api/author/

{
  "fname": "John",
  "lname": "Doe",
  "email": "john@gmail.com"
}
GET /api/author/?q=jo

If q.length < 3 → returns empty list

Autocomplete logic:

Priority results: names starting with query
Then general contains results
➤ Publisher API
POST /api/publisher/

{
  "name": "Penguin",
  "country": "USA",
  "website": "https://penguin.com"
}
GET /api/publisher/?q=pen

Case-insensitive search on publisher name
➤ Book Metadata API
GET /api/book-data/ Returns all authors and publishers for dropdowns:

{
  "author": [{"id":1,"fname":"John","lname":"Doe"}],
  "publisher": [{"id":1,"name":"Penguin"}]
}
➤ Book API
POST /api/book/

{
  "title": "Django Basics",
  "publish_date": "2025-01-01",
  "author": [1,2],
  "publisher": 1
}
GET /api/book/?q=pen

Searches by:

Author first name
Author last name
Publisher name
Uses Q objects + distinct()

Authentication (JWT)
Register
POST /api/register/

Login
POST /api/login/

{
  "username": "your_username",
  "password": "password"
}
For superUser/Admin use: use python manage.py createsuperuser

Response:

{
  "refresh": "...",
  "access": "...",
  "is_admin": false,
  "user": {"id":1,"username":"admin"}
}
Used libraries:

djangorestframework
djangorestframework-simplejwt
How Forms Work
CSRF is disabled using @csrf_exempt
HTML forms do not submit normally
JS files send JSON using fetch()
Django validates data using ModelForms
