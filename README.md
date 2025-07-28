# Django Web Development Bootcamp

Welcome to our Django learning journey! This repository documents our step-by-step process of learning Django web development from scratch, assuming no prior knowledge.

## What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It follows the "batteries-included" philosophy, providing many built-in features for common web development tasks.

## Project Structure

```
web_bootcamp/
├── mybootcampsite/          # Main Django project directory
│   ├── settings.py          # Project configuration
│   ├── urls.py             # URL routing for the entire project
│   ├── wsgi.py             # Web Server Gateway Interface
│   └── asgi.py             # Asynchronous Server Gateway Interface
├── bootcamp_lessons/        # Django app for our learning exercises
│   ├── models.py           # Database models
│   ├── views.py            # View functions/classes
│   ├── urls.py             # URL patterns for this app
│   ├── admin.py            # Admin interface configuration
│   └── migrations/         # Database migration files
├── myenv/                  # Virtual environment (isolated Python environment)
├── db.sqlite3              # SQLite database file
├── manage.py               # Django's command-line utility
└── .gitignore              # Files to ignore in version control
```

## Key Django Concepts We're Learning

### 1. **Project vs Apps**
- **Project**: The entire Django application (mybootcampsite)
- **App**: A component within the project that handles specific functionality (bootcamp_lessons)

### 2. **MVT Pattern** (Model-View-Template)
- **Models**: Define data structure and database interactions
- **Views**: Handle business logic and user requests
- **Templates**: HTML files that define how data is presented

### 3. **URL Routing**
- Maps URLs to specific view functions
- Allows clean, user-friendly URLs

## Getting Started

### Prerequisites
- Python 3.x installed on your system
- Basic understanding of Python (helpful but not required)

### Setup Instructions

1. **Navigate to the project directory**
   ```bash
   cd /home/obote/Desktop/web_bootcamp
   ```

2. **Activate the virtual environment**
   ```bash
   source myenv/bin/activate
   ```

3. **Run the development server**
   ```bash
   python manage.py runserver
   ```

4. **Open your browser and visit**
   ```
   http://127.0.0.1:8000/
   ```

### Common Django Commands

```bash
# Start the development server
python manage.py runserver

# Create database migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Open Django shell for testing
python manage.py shell

# Create a new Django app
python manage.py startapp app_name
```

## Learning Path

### Phase 1: Basics ✅
- [x] Set up Django project and virtual environment
- [x] Understand project structure
- [x] Create first Django app (bootcamp_lessons)

### Phase 2: Views and URLs (In Progress)
- [ ] Create simple views
- [ ] Set up URL routing
- [ ] Understand HTTP requests and responses

### Phase 3: Templates
- [ ] Create HTML templates
- [ ] Use Django template language
- [ ] Static files (CSS, JavaScript, images)

### Phase 4: Models and Database
- [ ] Define models
- [ ] Database migrations
- [ ] Django ORM (Object-Relational Mapping)

### Phase 5: Forms
- [ ] Create and handle forms
- [ ] Form validation
- [ ] CSRF protection

### Phase 6: Admin Interface
- [ ] Set up Django admin
- [ ] Customize admin interface
- [ ] User authentication

### Phase 7: Advanced Topics
- [ ] User authentication and authorization
- [ ] File uploads
- [ ] Email functionality
- [ ] Deployment basics

## Resources

- [Official Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)

## Notes

- Always activate the virtual environment before working on the project
- The SQLite database (db.sqlite3) is included for development purposes
- Static files and migrations are ignored in version control as per .gitignore

## Next Steps

1. Create your first view in `bootcamp_lessons/views.py`
2. Set up URL routing in `bootcamp_lessons/urls.py`
3. Create a simple HTML template
4. Test everything works by running the development server

---

*This README will be updated as we progress through our Django learning journey!*