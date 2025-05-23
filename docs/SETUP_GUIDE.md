# Setup Guide

## Prerequisites

### Required Software
- **Python 3.11+**: Programming language runtime
- **PostgreSQL**: Database system (or SQLite for development)
- **Git**: Version control system
- **Web Browser**: For accessing the application

### Development Environment
- **Text Editor/IDE**: VS Code, PyCharm, or similar
- **Terminal/Command Prompt**: For running commands

## Installation Steps

### 1. Clone Repository
```bash
git clone <repository-url>
cd csu-ccis-blog
```

### 2. Python Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- flask
- flask-sqlalchemy
- flask-login
- flask-wtf
- wtforms
- email-validator
- werkzeug
- gunicorn
- psycopg2-binary
- sqlalchemy

### 4. Environment Variables

Create a `.env` file in the project root:
```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/csu_ccis_blog

# Flask Configuration
SESSION_SECRET=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# PostgreSQL Configuration (if using local database)
PGHOST=localhost
PGPORT=5432
PGUSER=your_username
PGPASSWORD=your_password
PGDATABASE=csu_ccis_blog
```

### 5. Database Setup

#### Option A: PostgreSQL (Recommended for Production)
```bash
# Install PostgreSQL
# Create database
createdb csu_ccis_blog

# The application will automatically create tables on first run
```

#### Option B: SQLite (Development Only)
```bash
# No additional setup required
# Database file will be created automatically
```

### 6. Initialize Database
```bash
# Run the application to create tables
python main.py
```

## Running the Application

### Development Mode
```bash
python main.py
```
The application will be available at: `http://localhost:5000`

### Production Mode (Gunicorn)
```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

## Environment Configuration

### Development Settings
- Debug mode enabled
- SQLite database (optional)
- Detailed error messages
- Auto-reload on code changes

### Production Settings
- Debug mode disabled
- PostgreSQL database
- Error logging
- Gunicorn WSGI server

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify PostgreSQL is running
   - Check DATABASE_URL configuration
   - Ensure database exists

2. **Module Import Errors**
   - Activate virtual environment
   - Install all dependencies: `pip install -r requirements.txt`

3. **Permission Errors**
   - Check file permissions
   - Run with appropriate user privileges

4. **Port Already in Use**
   - Change port in configuration
   - Kill existing process: `lsof -ti:5000 | xargs kill`

### Debug Steps
1. Check Python version: `python --version`
2. Verify virtual environment is active
3. Check installed packages: `pip list`
4. Review application logs
5. Test database connection

## Project Structure
```
csu-ccis-blog/
├── app.py                 # Flask app configuration
├── main.py               # Application entry point
├── models.py             # Database models
├── routes.py             # URL routes
├── forms.py              # Form definitions
├── utils.py              # Utility functions
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── templates/            # HTML templates
├── static/               # CSS, JS, images
└── docs/                 # Documentation
```