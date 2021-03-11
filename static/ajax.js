$(document).ready(function () {
    $("h3").hover(function () { //tag
            $(this).css('color', 'red');
        },
        function () {
            $(this).css('color', 'blue');
        });

    $("#search_bar").keyup( function(){
        var query;
        query = $(this).val();//.val() получает значения эдемента(input,select,textarea),(val(function()))
        $.get('/search/', {search_bar: query}, function(data){ //$.get(url,data,success,dataType)
            $('#search_list').html(data);// .html() - get the first element in html or insert smth in html
            });
        });
})