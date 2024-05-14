$(document).ready(function () {
    load_recents();
    load_initial_data();

    function load_data(query, category, priceRange, rentalPriceRange) {
        $.ajax({
            method: "GET",
            url: "/searchingPost",
            data: { query: query, category: category, price_range: priceRange, rental_price_range: rentalPriceRange },
            success: function (data) {
                $('#main-content').html(data.htmlresponse);
                console.log("Data loaded successfully.");
            },
            error: function(xhr, status, error) {
                console.error('Error during search:', error);
            }
        });
    }

    $('#searchForm').submit(function (event) {
        event.preventDefault(); // Prevent form submission
        var category = $('#category').val();
        var searchText = $('#searchText').val();
        var priceRange = $('#price-r').val();
        var rentalPriceRange = $('#rentalprice-r').val();
        load_data(searchText, category, priceRange, rentalPriceRange);
    });

    $('#searchButton').click(function (event) {
        event.preventDefault(); // Prevent form submission
        var category = $('#category').val();
        var searchText = $('#searchText').val();
        var priceRange = $('#price-r').val();
        var rentalPriceRange = $('#rentalprice-r').val();
        load_data(searchText, category, priceRange, rentalPriceRange);

        triggerAnimations();
    });

    $('#price-r, #rentalprice-r').change(function () {
        alert('Dropdown value changed');
        console.log('Dropdown value changed');
        var query = $('#searchText').val();
        var category = $('#category').val();
        var priceRange = $('#price-r').val();
        var rentalPriceRange = $('#rentalprice-r').val();

        console.log('Price Range selected:', priceRange);
        console.log('Rental Price Range selected:', rentalPriceRange);

        if (priceRange !== 'None') {
            sortItems(priceRange, 'Price');
        }

        if (rentalPriceRange !== 'None') {
            sortItems(rentalPriceRange, 'RentalPrice');
        }
    });

    function sortItems(sortOrder, sortType) {
        console.log('sortItems called with sortOrder:', sortOrder, 'sortType:', sortType);
        var items = $('.recent-area').get();
        console.log("Items before sorting:", items);

        items.sort(function (a, b) {
            var aText = $(a).find('.description:contains("' + sortType + '")').text().split(': ')[1].trim();
            var bText = $(b).find('.description:contains("' + sortType + '")').text().split(': ')[1].trim();

            console.log('Values to sort:', aText, bText);

            var valA = aText === "Not Available" ? (sortOrder === 'LowHigh' ? Infinity : -Infinity) : parseFloat(aText);
            var valB = bText === "Not Available" ? (sortOrder === 'LowHigh' ? Infinity : -Infinity) : parseFloat(bText);

            console.log('Parsed values:', valA, valB);

            return sortOrder === 'LowHigh' ? valA - valB : valB - valA;
        });

        console.log("Items after sorting:", items);

        $('#display-range').empty().append(items);
    }

    function load_initial_data() {
        $.ajax({
            method: "GET",
            url: "/searchingPost",
            success: function (data) {
                $('#result').html(data.htmlresponse);
                $('#numResultsFound').hide();
                console.log("Initial data loaded successfully.");
            },
            error: function(xhr, status, error) {
                console.error('Error loading initial data:', error);
            }
        });
    }

    function load_recents() {
        $.ajax({
            method: "GET",
            url: "/recentItemsPost",
            success: function (data) {
                $('#main-content').html(data);
                console.log("Recent items loaded successfully.");
            },
            error: function(xhr, status, error) {
                console.error('Error fetching recent items:', error);
            }
        });
    }

    function triggerAnimations() {
        $('#recent-area').fadeOut(500, function () {
            setTimeout(function () {
                $('.filters').addClass('show');
                $('#search-results').addClass('show');
                adjustFooterMarginTop(50);
            }, 500);
        });
    }

    adjustMainContentHeight();

    $(window).on('load resize', adjustMainContentHeight);
    setInterval(adjustMainContentHeight, 1);

    function adjustFooterMarginTop(num) {
        var marginsize = num !== undefined ? 30 + num : 30;
        $('#footer').css('margin-top', marginsize + 'px');
    }

    function adjustMainContentHeight() {
        var itemCount = $('.item-container').length;
        var itemHeight = $('.item-container').outerHeight(true);
        var newHeight;
        var windowWidth = window.innerWidth;
        if (windowWidth < 809) newHeight = itemCount * itemHeight;
        else if (windowWidth < 1098) newHeight = Math.ceil(itemCount / 2) * itemHeight;
        else if (windowWidth < 1387) newHeight = Math.ceil(itemCount / 3) * itemHeight;
        else if (windowWidth < 1676) newHeight = Math.ceil(itemCount / 4) * itemHeight;
        else newHeight = Math.ceil(itemCount / 5) * itemHeight;
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
});

