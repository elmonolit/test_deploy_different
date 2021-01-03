$(document).ready(function () {
    $("h3").hover(function () { //tag
            $(this).css('color', 'red');
        },
        function () {
            $(this).css('color', 'blue');
        });
    $("#search_bar").keyup( function(){
        var query;
        query = $(this).val();
        $.get('/search/', {search_bar: query}, function(data){
            $('#search_list').html(data);
            });
        });
})