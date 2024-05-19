$(document).ready(function() {
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

        // Send AJAX request to fetch user listings
        $.ajax({
            url: '/userListings',  // Adjust URL as per your backend endpoint
            method: 'GET',
            success: function(response) {
                if (response.listings) {
                    var listingsContent = $('#userlistings-container');
                    listingsContent.empty();  // Clear any existing content

                    // Check if there are listings
                    if (response.listings.length === 0) {
                        listingsContent.append('<p>No listings found.</p>');
                    } else {
                        // Iterate over the listings and add them to the container
                        response.listings.forEach(function(listing) {
                            var listingHtml = `
                                <div class="recent-area">
                                    <p>${listing.ItemName}</p>
                                    <img src="${listing.PhotoPath}" class="recents" alt="${listing.ItemName}"/>
                                    <p class="description">${listing.PostDate }</p>
                                    <p class="description">Price: ${listing.Price}</p>
                                    <p class="description">Rental Price: ${listing.RentalPrice}</p>
                                    <p class="description">${listing.CategoryName}</p>
                                </div>
                            `;
                            listingsContent.append(listingHtml);
                        });
                    }
                    
                    // Show the listings content and hide the messages content
                    $('#userlistings-container').show();
                    $('#messagesContent').hide();
                } else {
                    console.error('Error fetching listings:', response.error);
                }
            },
            error: function(xhr, status, error) {
                console.error('AJAX error:', error);
            }
        });
    }

    // Check if the URL hash matches '#messages'
    if (window.location.hash === "#messages") {
        toggleMessages();
    } else {
        // Default to showing messages if no hash or different hash
        toggleMessages();
    }

    // Event listener for clicking the Messages button
    $('#toMessages').click(function() {
        toggleMessages();
    });

    // Event listener for clicking the Listings button
    $('#toListings').click(function() {
        toggleListings();
    });

    // Function to update message badge count
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

    // Update the badge based on the static count
    updateMessageBadge();
});
