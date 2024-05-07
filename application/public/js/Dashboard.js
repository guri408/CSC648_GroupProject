// Function to toggle the visibility of the Messages section
function toggleMessages() {
    var messages = document.getElementById("messagesContent");
    var listings = document.getElementById("listingsContent");
    var composeBtn = document.querySelector('.btn-compose');
    var btnMessages = document.querySelector('.btn-outline-primary');
    var btnListings = document.querySelector('.btn-outline-secondary');

    // Show Messages, hide Listings
    messages.style.display = "block";
    listings.style.display = "none";
    composeBtn.style.display = "block"; // Show compose button in messages
    btnMessages.classList.add('btn-active');
    btnListings.classList.remove('btn-active');
}

// Function to toggle the visibility of the Listings section
function toggleListings() {
    var messages = document.getElementById("messagesContent");
    var listings = document.getElementById("listingsContent");
    var composeBtn = document.querySelector('.btn-compose');
    var btnMessages = document.querySelector('.btn-outline-primary');
    var btnListings = document.querySelector('.btn-outline-secondary');

    // Hide Messages, show Listings
    listings.style.display = "block";
    messages.style.display = "none";
    composeBtn.style.display = "none"; // Hide compose button when listings are shown
    btnListings.classList.add('btn-active');
    btnMessages.classList.remove('btn-active');
}

// Event listener for DOM content loaded
document.addEventListener('DOMContentLoaded', function() {
    // Check if the URL hash matches '#messages'
    if (window.location.hash === "#messages") {
        toggleMessages();
    } else {
    // Default to showing messages if no hash or different hash
        toggleMessages();
    }
});

function updateMessageBadge() {
    const badge = document.getElementById('messageCount');
    const count = 1; // Placeholder for a fake message count, replace with dynamic value from server later
    
    if (count > 0) {
        badge.textContent = count; // Set the badge count
        badge.style.display = 'inline-block'; // Show the badge
    } else {
        badge.style.display = 'none'; // Hide the badge if count is 0
    }
}

// Call this function on page load
document.addEventListener('DOMContentLoaded', function() {
    updateMessageBadge(); // Update the badge based on the static count
});

