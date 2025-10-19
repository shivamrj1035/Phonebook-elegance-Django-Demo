# Authentication Setup Guide

This document outlines the steps to add user authentication (Sign Up, Sign In, and Sign Out) to the Django phonebook application.

## 1. Create an `accounts` App

To keep the authentication logic separate, we create a new Django app called `accounts`.

```bash
python manage.py startapp accounts
```

## 2. Configure `settings.py`

Add the new `accounts` app to the `INSTALLED_APPS` list in `phonebook_project/settings.py`.

```python
INSTALLED_APPS = [
    # ... other apps
    "phonebook",
    "accounts",
]
```

## 3. Implement Sign-Up

### a. Create the Sign-Up View

Create a file `accounts/views.py` and add the following code to handle user registration:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
```

### b. Create the Sign-Up Template

Create a new directory `templates/accounts` and inside it, create a file named `signup.html`:

```html
{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-center">Sign Up</h3>
                </div>
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        {{ form.as_p }}
                        <button type="submit" class="btn btn-primary btn-block">Sign Up</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## 4. Implement Sign-In and Sign-Out

### a. Create the Sign-In Template

In the `templates/accounts` directory, create a file named `login.html`:

```html
{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h3 class="text-center">Login</h3>
                </div>
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        {{ form.as_p }}
                        <button type="submit" class="btn btn-primary btn-block">Login</button>
                    </form>
                    <p class="text-center mt-3">Don't have an account? <a href="{% url 'signup' %}">Sign up</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### b. Configure URLS

Create a file `accounts/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

Update the main `phonebook_project/urls.py` to include the `accounts` URLs and Django's built-in `LoginView` and `LogoutView`:

```python
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("phonebook.urls")),
    path("accounts/", include("accounts.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
```

## 5. Update the Base Template

Modify `templates/base.html` to show the correct authentication links in the navigation bar:

```html
<div class="navbar-nav ms-auto">
    {% if user.is_authenticated %}
        <span class="navbar-text me-2">Logged in as {{ user.username }}</span>
        <a class="nav-link" href="{% url 'logout' %}">
            <i class="fas fa-sign-out-alt"></i> Sign Out
        </a>
    {% else %}
        <a class="nav-link" href="{% url 'login' %}">
            <i class="fas fa-sign-in-alt"></i> Sign In
        </a>
        <a class="nav-link" href="{% url 'signup' %}">
            <i class="fas fa-user-plus"></i> Sign Up
        </a>
    {% endif %}
</div>
```

## 6. Secure the Phonebook Views

### a. Associate Contacts with Users

Update the `Contact` model in `phonebook/models.py` to include a `ForeignKey` to the `User` model:

```python
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ... other fields
```

### b. Update Views to be User-Specific

Modify the views in `phonebook/views.py` to only show contacts belonging to the currently logged-in user. Also, protect all views with the `@login_required` decorator.

```python
from django.contrib.auth.decorators import login_required

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    # ...

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user)
    # ...

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            # ...
    # ...

# ... and so on for the other views.
```

## 7. Database Migrations

After modifying the `Contact` model, you need to create and apply database migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

This completes the implementation of the sign-up, sign-in, and sign-out functionality.
