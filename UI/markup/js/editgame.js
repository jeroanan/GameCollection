$(function() {
    var pickers = $(".picker");
    pickers.datepicker();
    pickers.datepicker("option", "dateFormat", "dd/mm/yy");
    pickers.datepicker("setDate", "{{game.date_purchased}}");
})
