# SimpleBlog - Flask Blog Application

## Overview

SimpleBlog is a Flask-based blog application that allows users to create accounts, write blog posts, and interact with other users through comments. The application provides full CRUD functionality for posts and comments, with user authentication to protect content.

## User Preferences

```
Preferred communication style: Simple, everyday language.
```

## System Architecture

SimpleBlog follows a monolithic architecture built with Flask. The application uses:

- **Backend Framework**: Flask (Python)
- **Database**: SQLAlchemy ORM with SQLite (development) / Postgres (production)
- **Authentication**: Flask-Login for session-based authentication
- **Forms**: Flask-WTF for form handling and validation
- **Frontend**: HTML templates with Jinja2, Bootstrap for styling, and JavaScript for client-side enhancements

The application is structured using the MVC (Model-View-Controller) pattern:
- **Models**: SQLAlchemy models defining the database schema
- **Views**: Jinja2 templates for rendering HTML
- **Controllers**: Flask routes handling requests and business logic

## Key Components

### 1. Models (`models.py`)

The application uses SQLAlchemy with three main models:

- **User**: Handles user authentication and profile information
  - Fields: id, username, email, password_hash, created_at
  - Relationships: posts (one-to-many), comments (one-to-many)

- **Post**: Represents blog posts
  - Fields: id, title, content, created_at, updated_at, user_id
  - Relationships: author (many-to-one), comments (one-to-many)

- **Comment**: Represents user comments on posts
  - Fields: id, content, created_at, user_id, post_id
  - Relationships: author (many-to-one), post (many-to-one)

### 2. Views (`templates/`)

The application includes the following templates:
- `base.html`: Base template with common layout elements
- `index.html`: Home page showing latest posts
- `register.html`: User registration form
- `login.html`: User login form
- `dashboard.html`: User dashboard for managing posts
- `create_post.html`: Form for creating new posts
- `edit_post.html`: Form for editing existing posts
- `post_detail.html`: Detailed view of a post with comments
- `error.html`: Error page for handling exceptions

### 3. Controllers (`routes.py`)

The routes handle various user actions:
- User authentication (register, login, logout)
- Post management (create, read, update, delete)
- Comment management (create, delete)
- Dashboard view for user's posts

### 4. Forms (`forms.py`)

WTForms-based forms with validation:
- `RegistrationForm`: User registration with field validation
- `LoginForm`: User login
- `PostForm`: Creating and editing blog posts
- `CommentForm`: Adding comments to posts

### 5. Static Files

- `css/style.css`: Custom CSS styles
- `js/main.js`: Core JavaScript functionality
- `js/posts.js`: Post-specific functionality (deletion)
- `js/comments.js`: Comment-specific functionality

## Data Flow

1. **User Authentication**:
   - User registers with username, email, and password
   - Passwords are hashed before storage using werkzeug.security
   - Flask-Login manages user sessions and authentication state

2. **Post Creation Flow**:
   - Authenticated user creates a post via form
   - Server validates input and creates database entry
   - User is redirected to the new post or dashboard

3. **Comment Flow**:
   - User views a post and adds a comment
   - Comment is stored with references to both post and author
   - Page refreshes to show the new comment

4. **Dashboard Flow**:
   - User views their dashboard to see all their posts
   - Posts can be managed (edited, deleted) from this view

## External Dependencies

The application relies on several external libraries:

1. **Flask**: Core web framework
2. **SQLAlchemy (Flask-SQLAlchemy)**: ORM for database operations
3. **Flask-Login**: User session management
4. **Flask-WTF**: Form handling and CSRF protection
5. **Werkzeug**: Utilities including password hashing
6. **Bootstrap**: CSS framework for styling (loaded via CDN)
7. **Gunicorn**: WSGI HTTP server for production deployment

## Database Schema

The database uses a relational structure with three main tables:

1. **User**:
   - Primary key: id (integer)
   - Unique fields: username, email
   - Password stored as hash
   - Timestamps for creation

2. **Post**:
   - Primary key: id (integer)
   - Foreign key: user_id references User
   - Fields for title, content
   - Timestamps for creation and updates

3. **Comment**:
   - Primary key: id (integer)
   - Foreign keys: user_id references User, post_id references Post
   - Content field
   - Timestamp for creation

## Deployment Strategy

The application is configured for deployment on Replit with:

1. **Database**: 
   - Development: SQLite for simplicity
   - Production: Configured to use PostgreSQL via DATABASE_URL environment variable

2. **Web Server**:
   - Development: Flask's built-in server
   - Production: Gunicorn WSGI server

3. **Environment Variables**:
   - SESSION_SECRET: For Flask secret key (fallback to dev_secret_key)
   - DATABASE_URL: Database connection string

4. **Replit Configuration**:
   - Python 3.11 environment
   - Gunicorn for production serving
   - Deployment target configured for autoscaling
   - ProxyFix middleware for proper handling of HTTPS

## Getting Started

1. No setup is needed as the database automatically initializes on first run
2. Register a new user account to get started
3. After logging in, you can create posts from your dashboard
4. All users can view posts and add comments
5. Users can only edit or delete their own posts and comments