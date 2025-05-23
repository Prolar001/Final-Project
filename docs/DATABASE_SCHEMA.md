# Database Schema Specifications

## Table Definitions

### User Table
```sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(256) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Fields:**
- `id`: Primary key, auto-incrementing integer
- `username`: Unique username, 3-64 characters
- `email`: Unique email address, valid email format
- `password_hash`: Hashed password using Werkzeug security
- `created_at`: Timestamp of account creation

### Post Table
```sql
CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(128) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);
```

**Fields:**
- `id`: Primary key, auto-incrementing integer
- `title`: Post title, 3-128 characters
- `content`: Post content, unlimited text
- `created_at`: Timestamp of post creation
- `updated_at`: Timestamp of last modification
- `user_id`: Foreign key referencing user.id

### Comment Table
```sql
CREATE TABLE comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES post(id) ON DELETE CASCADE
);
```

**Fields:**
- `id`: Primary key, auto-incrementing integer
- `content`: Comment content, unlimited text
- `created_at`: Timestamp of comment creation
- `updated_at`: Timestamp of last modification
- `user_id`: Foreign key referencing user.id
- `post_id`: Foreign key referencing post.id

## Relationships and Constraints

### Primary Keys
- All tables use auto-incrementing integer primary keys
- Ensures unique identification of each record

### Foreign Key Relationships
1. `post.user_id` → `user.id` (CASCADE DELETE)
2. `comment.user_id` → `user.id` (CASCADE DELETE)
3. `comment.post_id` → `post.id` (CASCADE DELETE)

### Unique Constraints
- `user.username`: Must be unique across all users
- `user.email`: Must be unique across all users

### Data Validation
- Username: 3-64 characters, alphanumeric
- Email: Valid email format required
- Password: Minimum 6 characters (hashed)
- Post title: 3-128 characters
- Content fields: Required, cannot be empty

### Indexes (Recommended)
```sql
CREATE INDEX idx_post_user_id ON post(user_id);
CREATE INDEX idx_comment_post_id ON comment(post_id);
CREATE INDEX idx_comment_user_id ON comment(user_id);
CREATE INDEX idx_post_created_at ON post(created_at);
```