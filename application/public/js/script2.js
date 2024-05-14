$(document).ready(function () {
    load_recents();
    load_initial_data();

    function load_data(query, category) {
        $.ajax({
            method: "GET",
            url: "/searchingPost",
            data: { query: query, category: category },
            success: function (data) {
                $('#result').html(data.htmlresponse);
            }
        });
    }

    $('#searchForm').submit(function (event) {
        event.preventDefault(); // Prevent form submission
        var category = $('#category').val();
        var searchText = $('#searchText').val();
        // Perform search using AJAX and update search results
        // Your AJAX request and result handling code here
    });

    $('#searchButton').click(function (event) {
        event.preventDefault(); // Prevent form submission
        var category = $('#category').val();
        var searchText = $('#searchText').val();
        // Perform search using AJAX and update search results
        // Your AJAX request and result handling code here

        triggerAnimations();
        load_data(searchText, category);
    });

    $('#price-r').change(function () {
        var sortBy = $(this).val();
        console.log("Sorting by:", sortBy); // Debugging
        sortItems(sortBy, 'Price');
    });

    $('#rentalprice-r').change(function () {
        var sortBy = $(this).val();
        console.log("Sorting by:", sortBy); // Debugging
        sortItems(sortBy, 'RentalPrice');
    });

    function sortItems(sortOrder, sortType) {
        var items = $('.recent-area').get();
        items.sort(function (a, b) {
            var aText = $(a).find('.description:contains("' + sortType + '")').text().split(': ')[1].trim();
            var bText = $(b).find('.description:contains("' + sortType + '")').text().split(': ')[1].trim();

            var valA = aText === "Not Available" ? (sortOrder === 'LowHigh' ? Infinity : -Infinity) : parseFloat(aText);
            var valB = bText === "Not Available" ? (sortOrder === 'LowHigh' ? Infinity : -Infinity) : parseFloat(bText);

            if (sortOrder === 'LowHigh') {
                return valA - valB;
            } else {
                return valB - valA;
            }
        });
        $('#display-range').empty().append(items);
    }

    function load_initial_data() {
        $.ajax({
            method: "GET",
            url: "/searchingPost",
            success: function (data) {
                $('#result').html(data.htmlresponse);
                $('#numResultsFound').hide();
            }
        });
    }

    function load_recents() {
        $.ajax({
            method: "GET",
            url: "/ajaxlivesearch",
            success: function (data) {
                $('#recent').html(data.htmlresponse);
            }
        });
    }

    function isIndexPage() {
        return window.location.pathname.endsWith("index.html");
    }

    function redirectToIndex(category, searchText) {
        var searchURL = "index.html?category=" + encodeURIComponent(category) + "&searchText=" + encodeURIComponent(searchText);
        window.location.href = searchURL;
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

    function triggerAnimations() {
        $('#recent-area').fadeOut(500, function() {
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
});

function adjustFooterMarginTop(num) {
    var marginsize = num !== undefined ? 30 + num : 30;
    $('#footer').css('margin-top', marginsize + 'px');
}

function adjustMainContentHeight() {
    var itemCount = $('.item-container').length;
    var itemHeight = $('.item-container').outerHeight(true);
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
