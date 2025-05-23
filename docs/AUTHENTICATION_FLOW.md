# Authentication Flow

## User Registration Flow

```
1. User visits /register
2. User fills registration form
   ├── Username (3-64 chars, unique)
   ├── Email (valid format, unique)
   ├── Password (min 6 chars)
   └── Confirm Password (must match)
3. Form validation (client & server-side)
4. Check username/email uniqueness
5. Hash password using Werkzeug
6. Save user to database
7. Redirect to login page
8. Flash success message
```

## User Login Flow

```
1. User visits /login
2. User enters credentials
   ├── Email
   └── Password
3. Server validates credentials
4. Check password hash
5. If valid:
   ├── Create user session (Flask-Login)
   ├── Redirect to dashboard
   └── Flash welcome message
6. If invalid:
   ├── Show error message
   └── Return to login form
```

## User Logout Flow

```
1. User clicks logout
2. Server destroys session
3. Flask-Login logs out user
4. Redirect to home page
5. Flash logout message
```

## Session Management

### Flask-Login Integration
- Uses Flask-Login for session management
- Sessions stored server-side
- User ID stored in session cookie
- Automatic login state checking

### Protected Routes
```python
@login_required
def protected_route():
    # Only accessible to authenticated users
    pass
```

### User Loading
```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

## Security Features

1. **Password Hashing**: Werkzeug PBKDF2 with salt
2. **CSRF Protection**: Flask-WTF tokens
3. **Session Security**: Secure session cookies
4. **Input Validation**: Server-side form validation
5. **Authorization**: Route-level access control

## Authentication Sequence Diagram

```
User                 Browser              Server              Database
 |                     |                    |                    |
 |-- Registration ---->|                    |                    |
 |                     |-- POST /register ->|                    |
 |                     |                    |-- Validate form -->|
 |                     |                    |-- Hash password -->|
 |                     |                    |-- Save user ------>|
 |                     |<-- Redirect -------|<-- Success --------|
 |<-- Success msg -----|                    |                    |
 |                     |                    |                    |
 |-- Login ----------->|                    |                    |
 |                     |-- POST /login ---->|                    |
 |                     |                    |-- Check user ----->|
 |                     |                    |<-- User data ------|
 |                     |                    |-- Verify password->|
 |                     |                    |-- Create session ->|
 |                     |<-- Set cookie -----|                    |
 |<-- Dashboard -------|<-- Redirect -------|                    |
```