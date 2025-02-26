function markAsRead(button) {
    console.log('Button clicked'); // Confirm the function is triggered

    const checkboxContainer = button.nextElementSibling; // Get the checkbox container

    button.style.display = 'none';  // Hide the button
    checkboxContainer.style.display = 'block'; // Show the checkbox container

    const deleteButton = button.closest('td').nextElementSibling.querySelector('.delete-button'); // Get the delete button
    deleteButton.disabled = false; // Enable the delete button
    deleteButton.classList.add('active');
}

function deleteEnquiry(button) {
    const enquiryId = button.getAttribute('data-id'); // Get the enquiry ID from the button's data attribute

    if (confirm('Are you sure you want to delete this enquiry?')) {
        fetch(`/delete_enquiry/${enquiryId}/`, { // Adjust the URL according to your delete route
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for Django
            }
        })
        .then(response => {
            if (response.ok) {
                // Remove the row from the table
                const row = button.closest('tr');
                row.remove();
                alert('Enquiry deleted successfully.'); // Optional success message

                // Update serial numbers for the remaining rows
                updateSerialNumbers();

            } else {
                alert('Error deleting enquiry.'); // Optional error message
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while trying to delete the enquiry.'); // Optional error message
        });
    }
}

// Function to update serial numbers after deletion
function updateSerialNumbers() {
    const rows = document.querySelectorAll('.enquiry-count'); // Select all S.No cells
    rows.forEach((cell, index) => {
        cell.textContent = index + 1; // Update the S.No based on the new row index
    });
}

// Function to get CSRF token for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


