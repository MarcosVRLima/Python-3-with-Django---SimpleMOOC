$(document).ready(function(){
    //button of sidebar
    $('.toggler').on('click', function() {
        $('.ui.sidebar').sidebar('setting', 'transition', 'overlay').sidebar('toggle');
    });

    //button of close in message
    $('.message .close').on('click', function() {
        $(this).closest('.message').transition('fade');
    });
});
