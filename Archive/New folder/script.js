// Function to handle search
$(document).ready(function () {
    load_recents();
    $('#searchForm').submit(function (event) {
        event.preventDefault(); // Prevent form submission
        var category = $('#category').val();
        var searchText = $('#searchText').val();
        // Perform search using AJAX and update search results
        // Your AJAX request and result handling code here
    });
    function load_recents() {
        $.ajax({
            method: "GET",
            url: "/ajaxlivesearch",
            success: function (data) {
                $('#recent').html(data.htmlresponse);
            }
        });
    }
    $('#dropdownBtn').click(function () {
        $('#dropdownContent').toggleClass('show');
    });

    $(document).click(function (e) {
        if (!$(e.target).closest('#dropdownBtn').length && !$(e.target).closest('#dropdownContent').length) {
            $('#dropdownContent').removeClass('show');
        }
    });
        
    $('#toMessages').click(function() {
        toggleElements("messages");
    });

    $('#toListings').click(function() {
        toggleElements("listings");
    });

    function toggleElements(selected) {
        const messageNum = document.querySelector(".message-num");
        const messageContainer = document.querySelector(".message-area");
        const listingNum = document.querySelector(".listing-num");
        const listingContainer = document.querySelector(".listing-area");

        if (selected === "messages") {
            messageNum.classList.add("message-num-show");
            messageContainer.classList.add("message-area-show");
            listingNum.classList.remove("listing-num-show");
            listingContainer.classList.remove("listing-area-show");
		    
	    $('#toMessages').addClass('active');
            $('#toListings').removeClass('active');
        } else if (selected === "listings") {
            messageNum.classList.remove("message-num-show");
            messageContainer.classList.remove("message-area-show");
            listingNum.classList.add("listing-num-show");
            listingContainer.classList.add("listing-area-show");
		    
	    $('#toListings').addClass('active');
            $('#toMessages').removeClass('active');
        }
    }
    $('#searchButton').click(function() {
        $('#recent-area').fadeOut(500, function() {
            setTimeout(function() {
                $('.filters').addClass('show');

                // Add class 'show' to search results with animation
                $('#search-results').addClass('show');
            }, 500);
        });
    });
});