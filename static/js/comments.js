// comments.js - Functionality for post comments

document.addEventListener('DOMContentLoaded', function() {
    // Handle comment deletion
    setupCommentDeletion();
});

function setupCommentDeletion() {
    // Get comment deletion modal elements
    const deleteCommentModal = document.getElementById('deleteCommentModal');
    const confirmDeleteCommentBtn = document.getElementById('confirmDeleteCommentBtn');
    
    if (!deleteCommentModal || !confirmDeleteCommentBtn) return;
    
    const modal = new bootstrap.Modal(deleteCommentModal);
    let commentIdToDelete = null;
    
    // Add event listeners to all delete comment buttons
    document.querySelectorAll('.delete-comment-btn').forEach(button => {
        button.addEventListener('click', function() {
            commentIdToDelete = this.closest('.comment-card').getAttribute('data-comment-id');
            
            if (commentIdToDelete) {
                modal.show();
            } else {
                console.error('No comment ID found for deletion');
            }
        });
    });
    
    // Handle confirm delete button click
    confirmDeleteCommentBtn.addEventListener('click', function() {
        if (!commentIdToDelete) {
            modal.hide();
            return;
        }
        
        fetch(`/comment/${commentIdToDelete}/delete`, {
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
                // Remove the comment element
                const commentElement = document.querySelector(`.comment-card[data-comment-id="${commentIdToDelete}"]`);
                if (commentElement) {
                    commentElement.remove();
                    
                    // Update comments count if present
                    const commentsCountElement = document.querySelector('.comments-count');
                    if (commentsCountElement) {
                        const currentCount = parseInt(commentsCountElement.textContent, 10);
                        if (!isNaN(currentCount)) {
                            commentsCountElement.textContent = currentCount - 1;
                        }
                    }
                    
                    showNotification('Comment deleted successfully.', 'success');
                }
            } else {
                showNotification(data.message || 'Failed to delete comment.', 'danger');
            }
        })
        .catch(error => {
            console.error('Error deleting comment:', error);
            modal.hide();
            showNotification('An error occurred while deleting the comment.', 'danger');
        });
    });
}
