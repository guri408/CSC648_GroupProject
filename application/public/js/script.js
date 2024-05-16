$(document).ready(function() {
    // Load initial recent items
    $.ajax({
        url: '/recentItemsPost',
        method: 'GET',
        success: function(response) {
            $('#main-content').html(response);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching recent items:', error);
        }
    });

    // Handle search form submission
    $('#searchForm').on('submit', function(event) {
        event.preventDefault();
        performSearch();
    });

    // Attach filter handlers
    $('#price-r, #rentalprice-r').change(function() {
        performSearch();
    });

    function performSearch() {
        var query = $('#searchText').val();
        var category = $('#category').val();
        var priceRange = $('#price-r').val();
        var rentalPriceRange = $('#rentalprice-r').val();
        $.ajax({
            url: '/searchingPost',
            method: 'GET',
            data: { query: query, category: category, price_range: priceRange, rental_price_range: rentalPriceRange },
            success: function(response) {
                $('#main-content').html(response.htmlresponse);
                triggerAnimations();
            },
            error: function(xhr, status, error) {
                console.error('Error during search:', error);
            }
        });
    }

    function triggerAnimations() {
        $('#recent-area2').fadeOut(500, function() {
            setTimeout(function() {
                $('.filters').addClass('show');
                $('#search-results').addClass('show');
                adjustFooterMarginTop(50);
            }, 500);
        });
    }

    adjustMainContentHeight();

    $(window).on('load resize', function() {
        adjustMainContentHeight();
    });

    setInterval(adjustMainContentHeight, 1);

    $('#dropdownBtn').click(function() {
        $('#dropdownContent').toggleClass('show');
    });

    $(document).click(function(e) {
        if (!$(e.target).closest('#dropdownBtn').length && !$(e.target).closest('#dropdownContent').length) {
            $('#dropdownContent').removeClass('show');
        }
    });

    $('#toMessages').click(function() {
        toggleElements("messages");
        adjustMainContentHeightForMessages();
        adjustFooterMarginTop(30);
    });

    $('#toListings').click(function() {
        toggleElements("listings");
        adjustMainContentHeightForListings();
        adjustFooterMarginTop(30);
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

    $('.searchButton').click(function() {
        if (isIndexPage()) {
            event.preventDefault();
        }
        triggerAnimations();
    });

    function isIndexPage() {
        return window.location.pathname.endsWith("index.html");
    }

    function adjustFooterMarginTop(num) {
        var marginsize = num !== undefined ? 30 + num : 30;
        $('#footer').css('margin-top', marginsize + 'px');
    }

    function adjustMainContentHeight() {
        var itemCount = $('.recent-area').length;
        var itemHeight = $('.recent-area').outerHeight(true);
        var newHeight;

        var windowWidth = window.innerWidth;

        if (windowWidth < 809) {
            newHeight = itemCount * itemHeight;
        } else if (windowWidth < 1098) {
            newHeight = Math.ceil(itemCount / 2) * itemHeight;
        } else if (windowWidth < 1387) {
            newHeight = Math.ceil(itemCount / 3) * itemHeight;
        } else if (windowWidth < 1676) {
            newHeight = Math.ceil(itemCount / 4) * itemHeight;
        } else {
            newHeight = Math.ceil(itemCount / 5) * itemHeight;
        }

        $('.main-content').css('height', newHeight);
    }

    function adjustMainContentHeightForListings() {
        var listingCount = $('.listing-container').length;
        var listingNewHeight = listingCount * $('.listing-container').outerHeight(true);

        $('.main-content').css('height', listingNewHeight);
    }

    function adjustMainContentHeightForMessages() {
        var messageCount = $('.message-container').length;
        var messageNewHeight = messageCount * $('.message-container').outerHeight(true);

        $('.main-content').css('height', messageNewHeight);
    }

    window.addEventListener('resize', adjustMainContentHeight);
});
