from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def requires_auth(f):
    """Decorator to check if user is authenticated before accessing a route."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def format_datetime(dt, format='%B %d, %Y at %I:%M %p'):
    """Format a datetime object to a readable string."""
    if dt:
        return dt.strftime(format)
    return ""
