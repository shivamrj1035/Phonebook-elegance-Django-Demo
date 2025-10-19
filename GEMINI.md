# Gemini Code Assistant Context

## Project Overview

This is a Django-based phonebook web application that demonstrates CRUD (Create, Read, Update, Delete) operations. It allows users to manage a list of contacts. The project uses a standard Django MVT (Model-View-Template) architecture.

**Key Technologies:**

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, Bootstrap
*   **Database:** SQLite (default)

## Building and Running the Project

### 1. Install Dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

### 2. Run Database Migrations

This will create the necessary database tables.

```bash
python manage.py migrate
```

### 3. Create a Superuser (Optional)

This allows you to access the Django admin interface.

```bash
python manage.py createsuperuser
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.
The admin panel will be available at `http://127.0.0.1:8000/admin/`.

## Development Conventions

*   **Project Structure:** The project follows a standard Django layout, with a main project directory (`phonebook_project`) and a separate app directory for the phonebook functionality (`phonebook`).
*   **Models:** The data model is defined in `phonebook/models.py`. The primary model is `Contact`.
*   **Views:** The application logic is handled by function-based views in `phonebook/views.py`.
*   **Templates:** HTML templates are located in the `templates` directory, with app-specific templates in a subdirectory (`templates/phonebook`).
*   **Static Files:** CSS and other static assets are stored in the `static` directory.
*   **Forms:** Django forms are used for data validation and are defined in `phonebook/forms.py`.
*   **URL Routing:** URLs are mapped to views in `phonebook/urls.py` and included in the main `phonebook_project/urls.py`.
