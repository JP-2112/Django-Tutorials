# Django Tutorials - Online Store

A Django web application that demonstrates basic CRUD operations and template rendering for an online store.

## Features

- **Home Page**: Welcome page with navigation
- **About Page**: Information about the store
- **Contact Page**: Contact information with email, phone, and address
- **Products**: 
  - List all products with prices
  - View individual product details
  - Create new products with validation
  - Price validation (must be greater than zero)
- **Responsive Design**: Bootstrap-powered UI

## Project Structure

```
helloworld_project/
├── helloworld_project/     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pages/                  # Main Django app
│   ├── views.py           # View logic
│   ├── urls.py            # URL routing
│   ├── models.py          # Data models
│   └── templates/         # HTML templates
│       ├── pages/
│       │   ├── base.html
│       │   ├── home.html
│       │   ├── about.html
│       │   └── contact.html
│       └── products/
│           ├── index.html
│           ├── show.html
│           ├── create.html
│           └── success.html
└── manage.py
```

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/JP-2112/Django-Tutorials.git
cd Django-Tutorials
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Django:
```bash
pip install django
```

4. Run migrations (if any):
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000` in your browser

## Usage

### Navigation
- **Home**: Main landing page
- **About**: Information about the store
- **Products**: Browse all available products
- **Create Product**: Add new products to the store
- **Contact**: Store contact information

### Creating Products
1. Click "Create Product" in the navigation
2. Enter a product name (required)
3. Enter a price greater than zero (required)
4. Submit the form to see success confirmation

### Product Features
- Products with prices > $100 display names in red
- Invalid product IDs redirect to home page
- Form validation prevents empty fields and invalid prices

## Technologies Used

- **Django 4.2+**: Web framework
- **Bootstrap 5**: CSS framework for styling
- **Font Awesome**: Icons
- **HTML5/CSS3**: Frontend markup and styling

## Learning Objectives

This project demonstrates:
- Django URL routing and views
- Template inheritance and rendering
- Form handling and validation
- Class-based views
- Static files management
- Basic CRUD operations
- Input validation and error handling

## Author

Juan Pablo Corena

---

*This project is part of Django learning tutorials at EAFIT University.*
