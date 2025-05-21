// posts.js - Functionality for blog posts

document.addEventListener('DOMContentLoaded', function() {
    // Handle post deletion
    setupPostDeletion();
});

function setupPostDeletion() {
    // Get post deletion modal elements
    const deletePostModal = document.getElementById('deletePostModal');
    const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
    
    if (!deletePostModal || !confirmDeleteBtn) return;
    
    const modal = new bootstrap.Modal(deletePostModal);
    let postIdToDelete = null;
    
    // Add event listeners to all delete post buttons
    document.querySelectorAll('.delete-post-btn').forEach(button => {
        button.addEventListener('click', function() {
            postIdToDelete = this.getAttribute('data-post-id') || 
                             this.closest('tr')?.getAttribute('data-post-id');
            
            if (postIdToDelete) {
                modal.show();
            } else {
                console.error('No post ID found for deletion');
            }
        });
    });
    
    // Handle confirm delete button click
    confirmDeleteBtn.addEventListener('click', function() {
        if (!postIdToDelete) {
            modal.hide();
            return;
        }
        
        fetch(`/post/${postIdToDelete}/delete`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
            },
            credentials: 'same-origin'
        })
        .then(handleFetchError)
        .then(data => {
            modal.hide();
            
            if (data.success) {
                // Handle successful deletion based on the current page
                const postElement = document.querySelector(`tr[data-post-id="${postIdToDelete}"]`) || 
                                     document.querySelector(`.card[data-post-id="${postIdToDelete}"]`);
                
                if (postElement) {
                    // If we're on the dashboard or a listing page, remove the post element
                    postElement.remove();
                    showNotification('Post deleted successfully.', 'success');
                } else {
                    // If we're on the post detail page, redirect to dashboard
                    window.location.href = '/dashboard';
                }
            } else {
                showNotification(data.message || 'Failed to delete post.', 'danger');
            }
        })
        .catch(error => {
            console.error('Error deleting post:', error);
            modal.hide();
            showNotification('An error occurred while deleting the post.', 'danger');
        });
    });
}
