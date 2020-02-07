function submit_search(e) {
    $.post(
        '/search/',
        $(this).serialize(),
        function(data){ $('.tweets').html(data); }
    );
    e.preventDefault();
}

$('#search-form').submit(submit_search);