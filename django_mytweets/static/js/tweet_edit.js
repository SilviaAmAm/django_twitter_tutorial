function on_success_post_form(requested_data) {
    // Finding which HTML section will be updated
    var tweet_id_number = requested_data['tweet_id'];
    const tweet_container = $('#tweet-'+tweet_id_number);
    // Update the HTML with the edited tweet
    tweet_container.html(requested_data['tweet_html']);
}

function addSubmitHandler(element, tweet_id){
    element.submit( function posting_edit() {

        ajax_parameters = {
            type: $(this).attr('method'),
            url: window.location.pathname + tweet_id + "/",
            data: $(this).serialize(),
            success: on_success_post_form,
        };

        $.ajax(ajax_parameters);

        return false;
    });
}

function on_success_edit_tweet(requested_data) {
    // Finding which HTML section will be updated
    var tweet_id_number = requested_data['tweet_id'];
    const tweet_container = $('#tweet-'+tweet_id_number);
    // Update the HTML with the form sent by the server
    tweet_container.html(requested_data['edit_form_html']);

    // Add event handler to the post button
    addSubmitHandler($("#edit-form"), tweet_id_number)
}

function tweet_edit() {

    // 1. Get URL to which GET request will be sent
    var tweet_url = $(this).attr('href');
    var tweet_without_slash = tweet_url.slice(0,tweet_url.length-1);
    var idx_id = tweet_without_slash.lastIndexOf("/") + 1;
    var tweet_id = tweet_without_slash.slice(idx_id, tweet_without_slash.length);
    var view_url = tweet_without_slash.slice(0, idx_id);    // url for the user profile

    // 2. Data to be sent in the request
    const tweet_data = {id: tweet_id};

    // 3. Send GET request to the view function
    ajax_parameters = {
        type: 'GET',
        url: view_url,
        data: tweet_data,
        success: on_success_edit_tweet,
    };

    $.ajax(ajax_parameters);
    
    return false;
}

// Add event handler for clicking on Edit link near the tweets
const edit_link = $('.well a');
edit_link.click(tweet_edit);


