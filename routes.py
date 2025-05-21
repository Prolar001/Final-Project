import logging
from datetime import datetime
from flask import render_template, redirect, url_for, flash, request, jsonify, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import NotFound, Forbidden
from app import app, db
from models import User, Post, Comment
from forms import RegistrationForm, LoginForm, PostForm, CommentForm
from utils import format_datetime

# Register template filters
app.jinja_env.filters['format_datetime'] = format_datetime

@app.route('/')
def index():
    """Home page - shows latest posts."""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login page."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('You have been logged in successfully!', 'success')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Login failed. Please check your email and password.', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """Log user out and redirect to home page."""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard - shows user's posts and allows creating new ones."""
    posts = Post.query.filter_by(user_id=current_user.id).order_by(Post.created_at.desc()).all()
    return render_template('dashboard.html', posts=posts)

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def create_post():
    """Create a new blog post."""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_post.html', form=form, title='New Post')

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    """Show detailed view of a post with comments."""
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
    form = CommentForm()
    return render_template('post_detail.html', post=post, comments=comments, form=form)

@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    """Edit an existing blog post."""
    post = Post.query.get_or_404(post_id)
    
    # Check if the current user is the author of the post
    if post.user_id != current_user.id:
        flash('You cannot edit a post that is not yours.', 'danger')
        return redirect(url_for('post_detail', post_id=post_id))
    
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post_detail', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    
    return render_template('edit_post.html', form=form, post=post)

@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    """Delete a blog post."""
    post = Post.query.get_or_404(post_id)
    
    # Check if the current user is the author of the post
    if post.user_id != current_user.id:
        return jsonify({"success": False, "message": "You cannot delete a post that is not yours"}), 403
    
    db.session.delete(post)
    db.session.commit()
    return jsonify({"success": True, "message": "Post deleted successfully"})

@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    """Add a comment to a post."""
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            user_id=current_user.id,
            post_id=post_id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added!', 'success')
    
    return redirect(url_for('post_detail', post_id=post_id))

@app.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    """Delete a comment."""
    comment = Comment.query.get_or_404(comment_id)
    
    # Check if the current user is the author of the comment or the post
    post = Post.query.get(comment.post_id)
    if comment.user_id != current_user.id and post.user_id != current_user.id:
        return jsonify({"success": False, "message": "You cannot delete this comment"}), 403
    
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"success": True, "message": "Comment deleted successfully"})

@app.route('/api/posts')
def api_posts():
    """API endpoint to get all posts."""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([post.to_dict() for post in posts])

@app.route('/api/posts/<int:post_id>')
def api_post(post_id):
    """API endpoint to get a specific post."""
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())

@app.route('/api/posts/<int:post_id>/comments')
def api_post_comments(post_id):
    """API endpoint to get comments for a specific post."""
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.desc()).all()
    return jsonify([comment.to_dict() for comment in comments])

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('error.html', error_code=404, message="Page not found"), 404

@app.errorhandler(403)
def forbidden(e):
    """Handle 403 errors."""
    return render_template('error.html', error_code=403, message="Forbidden"), 403

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    logging.error(f"Server error: {e}")
    return render_template('error.html', error_code=500, message="Server error"), 500
