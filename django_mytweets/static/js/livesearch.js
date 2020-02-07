const user_input = $("#search-form")
const tweets_div = $('#results-content')
const endpoint = '/search/'
const delay_by_in_ms = 700
let scheduled_function = false

// Good tutorial: https://openfolder.sh/django-tutorial-as-you-type-search-with-ajax

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            // fade out the tweets_div, then:
            tweets_div.fadeTo('slow', 0).promise().then(() => {
                // replace the HTML contents
                tweets_div.html(response['search_results_html'])
                // fade-in the div with new contents
                tweets_div.fadeTo('slow', 1)
            })
        })
}

user_input.on('keyup', function () {

    const request_parameters = {
        query: $(this).val() // value of user_input: the HTML element with ID user-input
    }

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
