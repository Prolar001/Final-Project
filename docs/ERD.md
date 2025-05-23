# Entity-Relationship Diagram (ERD)

## Database Schema Overview

The CSU CCIS Blog uses a relational database design with three main entities: Users, Posts, and Comments.

```
┌─────────────────┐    1    ∞ ┌─────────────────┐    1    ∞ ┌─────────────────┐
│      USER       │◄──────────│      POST       │◄──────────│    COMMENT      │
├─────────────────┤           ├─────────────────┤           ├─────────────────┤
│ id (PK)         │           │ id (PK)         │           │ id (PK)         │
│ username        │           │ title           │           │ content         │
│ email           │           │ content         │           │ created_at      │
│ password_hash   │           │ created_at      │           │ updated_at      │
│ created_at      │           │ updated_at      │           │ user_id (FK)    │
└─────────────────┘           │ user_id (FK)    │           │ post_id (FK)    │
                              └─────────────────┘           └─────────────────┘
```

## Relationships

1. **User → Posts**: One-to-Many
   - One user can create multiple posts
   - Each post belongs to exactly one user
   - Foreign Key: `post.user_id` references `user.id`

2. **Post → Comments**: One-to-Many
   - One post can have multiple comments
   - Each comment belongs to exactly one post
   - Foreign Key: `comment.post_id` references `post.id`

3. **User → Comments**: One-to-Many
   - One user can create multiple comments
   - Each comment belongs to exactly one user
   - Foreign Key: `comment.user_id` references `user.id`

## Database Constraints

- **Primary Keys**: Auto-incrementing integers for all entities
- **Unique Constraints**: username and email must be unique
- **NOT NULL Constraints**: All required fields must have values
- **Cascade Deletes**: When a user is deleted, their posts and comments are also deleted
- **Foreign Key Constraints**: Ensure referential integrity between tables