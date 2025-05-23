# CSU CCIS Blog - Project Documentation

## Project Overview

### Purpose
The CSU CCIS Blog is a web application designed for the College of Computing and Information Sciences community to share knowledge, experiences, and insights. This platform enables students, faculty, and staff to create, share, and discuss blog posts in a collaborative environment.

### Chosen Tech Stack
- **Backend Framework**: Flask (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5
- **Authentication**: Flask-Login for session-based authentication
- **Forms**: Flask-WTF for form handling and validation
- **Web Server**: Gunicorn (Production)
- **Deployment**: Replit Platform

### High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (HTML/CSS/JS) │◄──►│   (Flask)       │◄──►│   (PostgreSQL)  │
│   Bootstrap     │    │   SQLAlchemy    │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌─────────────────┐              │
         └─────────────►│  Authentication │◄─────────────┘
                        │  (Flask-Login)  │
                        └─────────────────┘
```

## Features

### Core Functionality
1. **User Authentication**: Registration, login, logout, session management
2. **Blog Post Management**: Create, read, update, delete (CRUD) operations
3. **Comment System**: Users can comment on posts
4. **User Dashboard**: Personal post management interface
5. **Responsive Design**: Mobile-friendly interface with CSU CCIS branding

### Authentication Features
- Secure password hashing using Werkzeug
- Session-based authentication with Flask-Login
- User registration with email validation
- Login/logout functionality
- Protected routes requiring authentication

### CRUD Operations
1. **Posts**: Full CRUD functionality for blog posts
2. **Comments**: Create and delete comments on posts
3. **User Management**: User registration and profile management

## Technical Requirements Met

✅ **Frontend**: Responsive UI with Bootstrap, client-side JavaScript for interactivity  
✅ **Backend**: RESTful routing with Flask, business logic implementation  
✅ **Database**: Proper schema design with relationships and data persistence  
✅ **Authentication**: Complete signup, signin, signout workflow  
✅ **Two CRUD Modules**: Posts and Comments with full functionality  

## Project Structure

```
csu-ccis-blog/
├── app.py                 # Flask application configuration
├── main.py               # Application entry point
├── models.py             # Database models
├── routes.py             # Application routes
├── forms.py              # WTForms form definitions
├── utils.py              # Utility functions
├── templates/            # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── create_post.html
│   ├── edit_post.html
│   ├── post_detail.html
│   └── error.html
├── static/               # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── main.js
│   │   ├── posts.js
│   │   └── comments.js
│   └── images/
│       └── csu-ccis-logo.svg
└── docs/                 # Documentation
    ├── ERD.md
    ├── API_SPEC.md
    ├── SETUP_GUIDE.md
    └── USAGE_GUIDE.md
```

## Development Team
- **Framework**: Individual/Team Project
- **Timeline**: 21 calendar days
- **Institution**: Colorado State University, College of Computing and Information Sciences

## License
Educational use for CSU CCIS coursework.