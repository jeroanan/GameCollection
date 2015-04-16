function login() {
    hideValidationMessages();
    return loginPageAjax("/signin");
}

function loginDone(data) {
	 if (data == false) return;

	 if (data=="True") {
		  showValidationSuccess("Login successful.");
		  setTimeout(function() {navigate("/")}, 2000);
		  setLoginText();
	 } else {
		  showValidationFailure("Login failed.");
	 }	 
}

function newUser() {
    hideValidationMessages();
    return loginPageAjax("/signup");
}

function newUserDone(data) {
    if (data == false) return;

    if (data=="True") {
        showValidationSuccess("Signed up successfully")
		  setLoginText();
    } else {
        showValidationFailure("Error encountered while signing up")
    }
}

function loginPageAjax(url) {
    if (!validateLoginForm()) {
		  var def = new $.Deferred();
		  def.resolve(false);
		  return def;

	 }
    return $.ajax({
        url: url,
        type: "POST",
        data: {
            userid: $("#userid").val(),
            password: $("#password").val()
        }
    });
}

$(function() {
	 $("#login").on("click", function() {login().done(loginDone);return false;});
	 $("#newuser").on("click", function() {newUser().done(newUserDone);});
});