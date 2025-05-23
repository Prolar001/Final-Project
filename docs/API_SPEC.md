# API Specification

## Authentication Endpoints

### Register User
- **Method**: POST
- **URL**: `/register`
- **Description**: Create a new user account
- **Request Body**: Form data
  ```
  username: string (3-64 characters)
  email: string (valid email)
  password: string (min 6 characters)
  confirm_password: string (must match password)
  ```
- **Response**: Redirect to login page on success
- **Errors**: 400 if validation fails

### Login User
- **Method**: POST
- **URL**: `/login`
- **Description**: Authenticate user and create session
- **Request Body**: Form data
  ```
  email: string
  password: string
  ```
- **Response**: Redirect to dashboard on success
- **Errors**: 401 if credentials invalid

### Logout User
- **Method**: GET
- **URL**: `/logout`
- **Description**: End user session
- **Authentication**: Required
- **Response**: Redirect to home page

## Post Management Endpoints

### Get All Posts
- **Method**: GET
- **URL**: `/`
- **Description**: Display paginated list of all posts
- **Query Parameters**:
  ```
  page: integer (default: 1)
  ```
- **Response**: HTML page with post list

### View Post Detail
- **Method**: GET
- **URL**: `/post/<int:post_id>`
- **Description**: Display single post with comments
- **Response**: HTML page with post details and comments

### Create Post
- **Method**: GET/POST
- **URL**: `/post/new`
- **Description**: Create new blog post
- **Authentication**: Required
- **Request Body** (POST): Form data
  ```
  title: string (3-128 characters)
  content: string (required)
  ```
- **Response**: Redirect to dashboard on success

### Edit Post
- **Method**: GET/POST
- **URL**: `/post/<int:post_id>/edit`
- **Description**: Edit existing post
- **Authentication**: Required (must be post author)
- **Request Body** (POST): Form data
  ```
  title: string (3-128 characters)
  content: string (required)
  ```
- **Response**: Redirect to post detail on success

### Delete Post
- **Method**: POST
- **URL**: `/post/<int:post_id>/delete`
- **Description**: Delete existing post
- **Authentication**: Required (must be post author)
- **Response**: JSON
  ```json
  {
    "success": true,
    "message": "Post deleted successfully"
  }
  ```

## Comment Management Endpoints

### Add Comment
- **Method**: POST
- **URL**: `/post/<int:post_id>/comment`
- **Description**: Add comment to post
- **Authentication**: Required
- **Request Body**: Form data
  ```
  content: string (required)
  ```
- **Response**: Redirect to post detail page

### Delete Comment
- **Method**: POST
- **URL**: `/comment/<int:comment_id>/delete`
- **Description**: Delete comment
- **Authentication**: Required (must be comment author or post author)
- **Response**: JSON
  ```json
  {
    "success": true,
    "message": "Comment deleted successfully"
  }
  ```

## Dashboard Endpoints

### User Dashboard
- **Method**: GET
- **URL**: `/dashboard`
- **Description**: Display user's posts management interface
- **Authentication**: Required
- **Response**: HTML page with user's posts

## API Endpoints (JSON)

### Get Posts API
- **Method**: GET
- **URL**: `/api/posts`
- **Description**: Get all posts as JSON
- **Response**: JSON array of posts
  ```json
  [
    {
      "id": 1,
      "title": "Post Title",
      "content": "Post content...",
      "created_at": "2025-05-23T18:00:00",
      "updated_at": "2025-05-23T18:00:00",
      "author": "username",
      "user_id": 1,
      "comment_count": 5
    }
  ]
  ```

### Get Single Post API
- **Method**: GET
- **URL**: `/api/posts/<int:post_id>`
- **Description**: Get specific post as JSON
- **Response**: JSON object with post details

### Get Post Comments API
- **Method**: GET
- **URL**: `/api/posts/<int:post_id>/comments`
- **Description**: Get all comments for a post
- **Response**: JSON array of comments
  ```json
  [
    {
      "id": 1,
      "content": "Comment content...",
      "created_at": "2025-05-23T18:00:00",
      "author": "username",
      "user_id": 1,
      "post_id": 1
    }
  ]
  ```

## Error Handling

### HTTP Status Codes
- **200**: Success
- **302**: Redirect (successful form submission)
- **400**: Bad Request (validation errors)
- **401**: Unauthorized (login required)
- **403**: Forbidden (insufficient permissions)
- **404**: Not Found (resource doesn't exist)
- **500**: Internal Server Error

### Error Response Format
```json
{
  "success": false,
  "message": "Error description"
}
```