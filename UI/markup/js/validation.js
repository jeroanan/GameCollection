function validateLoginForm() {
    var failureText = "";
    if ($("#userid").val() == "") failureText = "Please enter a user id";
    if ($("#password").val() == "") failureText = appendText(failureText, "Please enter a password");
    if (failureText !== "") showValidationFailure(failureText);
    return failureText == "";
}

function showValidationSuccess(successText) {
	 hideValidationFailure();
    showValidationMessage($("#success"), $("#successText"), successText);
}

function hideValidationMessages() {
	 hideValidationSuccess();
	 hideValidationFailure();
}

function hideValidationSuccess() {
    hideValidationBox($("#success"), $("#successText"));
}

function hideValidationFailure() {
    hideValidationBox($("#failure"), $("#failureText"));
}

function hideValidationBox(box, boxText) {
    box.fadeOut(
    {
        complete: function() {
            boxText.html("");
        }
    })
}

function showValidationFailure(failureText) {
    showValidationMessage($("#failure"), $("#failureText"), failureText);
}

function showValidationMessage(box, boxTextCtrl, boxTextContent) {
    box.fadeIn();
    boxTextCtrl.html(boxTextContent);
}
