$(document).ready(function(){
    //button of sidebar
    $('.toggler').on('click', function() {
        $('.ui.sidebar').sidebar('setting', 'transition', 'overlay').sidebar('toggle');
    });

    //button of close in message
    $('.message .close').on('click', function() {
        $(this).closest('.message').transition('fade');
    });

    //transition of card login and dashboard
    $('.ui.fluid.card.login').transition('zoom');
    $('.ui.segment.dashboard').transition('zoom');

    //animation of message's
    $('.ui.red.message').transition('shake');
    $('.ui.success.message').transition('tada');

    //accordion of menu in dashboard
    $('.ui.accordion').accordion();
});
