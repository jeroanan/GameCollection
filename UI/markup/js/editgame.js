$(function() {
    var pickers = $(".picker");
	 var val = pickers.val();
    pickers.datepicker();
    pickers.datepicker("option", "dateFormat", "dd/mm/yy");
	 pickers.val(val);
})
