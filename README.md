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
│   ├── models.py           # Database models (Lesson model)
│   ├── views.py            # View functions/classes
│   ├── urls.py             # URL patterns for this app
│   ├── admin.py            # Admin interface configuration
│   ├── forms.py            # Django forms (LessonForm)
│   ├── migrations/         # Database migration files
│   └── templates/bootcamp_lessons/  # HTML templates
│       ├── base.html       # Base layout template
│       ├── home.html       # Home page
│       ├── intro.html      # Django introduction
│       ├── get_started.html # Getting started guide
│       ├── lesson_list.html # List of all lessons
│       ├── lesson_detail.html # Individual lesson details
│       ├── lesson_form.html # Create/update lesson form
│       └── lesson_confirm_delete.html # Delete confirmation
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

### Phase 2: Views and URLs ✅
- [x] Create simple views (home, intro, get_started)
- [x] Set up URL routing
- [x] Understand HTTP requests and responses

### Phase 3: Templates ✅
- [x] Create HTML templates
- [x] Use Django template language
- [x] Template inheritance with base.html
- [x] Static CSS styling

### Phase 4: Models and Database ✅
- [x] Define models (Lesson model)
- [x] Database migrations
- [x] Django ORM (Object-Relational Mapping)

### Phase 5: Forms ✅
- [x] Create and handle forms (LessonForm)
- [x] Form validation
- [x] CSRF protection

### Phase 6: Admin Interface ✅
- [x] Set up Django admin
- [x] Register models with admin
- [x] Create superuser for admin access

### Phase 7: CRUD Operations ✅
- [x] Create lessons (lesson_create view)
- [x] Read lessons (lesson_list, lesson_detail views)
- [x] Update lessons (lesson_update view)
- [x] Delete lessons (lesson_delete view)

### Phase 8: Advanced Topics (Future)
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

## Current Features

- **Home Page**: Welcome page with navigation
- **Django Introduction**: Learn about Django framework
- **Getting Started Guide**: Step-by-step setup instructions
- **Lesson Management**: Full CRUD operations for lessons
- **Admin Interface**: Manage lessons through Django admin
- **Responsive Design**: Clean, modern styling

## How to Use

1. **View lessons**: Visit `/lessons/` to see all lessons
2. **Add lessons**: Use `/admin/` to add new lessons
3. **Edit lessons**: Click edit links on lesson detail pages
4. **Delete lessons**: Use delete confirmation pages

## Next Steps

- Add user authentication
- Implement lesson categories
- Add search functionality
- Deploy to production server

---

*This README will be updated as we progress through our Django learning journey!*