function cancelEdit() {
    window.history.back();
}

function cancelEditPlatform() {
    navigate("/platforms");
}

function showDeleteConfirm() {
    $("#deleteConfirm").fadeIn();
}

function hideDeleteConfirm() {
    $("#deleteConfirm").fadeOut();
}

function deleteGame() {
    var j = {
        gameid: $("#id").val()
    };

    $.ajax({
        url: "/deletegame",
        data: j,
        success: deletionSuccessful(),
        error: deletionFailed()
    });
}

function deletePlatform() {
    var j = {
            id: $("#id").val()
    };

    $.ajax({
        url: "/deleteplatform",
        data: j,
        success: deletionSuccessful,
        error: deletionFailed
    });
}

function deletionSuccessful() {
    showValidationSuccess("Deletion successful");
    setTimeout(function() {
        hideValidationSuccess();
        window.history.back();
    }, 3000)
}

function deletionFailed() {
    showValidationFailure("Deletion failed");
}
function deleteHardware() {
    navigate("/deletehardware?hardwareid=" + $("#id").val());
}

function editGame(id) {
    navigate("/editgame?gameid=" + id);
}

function editHardware(id) {
    navigate("/edithardware?hardwareid=" + id);
}

function editPlatform(id) {
    navigate("/editplatform?platformid=" + id);
}

function addSuggestedPlatform(name, description) {
    navigate("/addplatform?name=" + name + "&description=" + description);
}

function deleteGenre(id) {
    navigate("/deletegenre?genreid=" + id)
}

function navigate(url) {
    window.location = url;
}

function updateGame() {

    var j = {
        id: $("#id").val(),
        title: $("#title").val(),
        platform: $("#platform").val(),
        numcopies: $("#numcopies").val(),
        numboxed: $("#numboxed").val(),
        nummanuals: $("#nummanuals").val(),
        datepurchased: $("#datepurchased").val(),
        approximatepurchaseddate: $("#approximatepurchaseddate").is(":checked"),
        notes: $("#notes").val()
    };

    if (!validateSaveGame(j)) return;

    $.ajax({
        url: "/updategame",
        data: j,
        success: saveSuccess,
        error: saveError
    });
}

function saveGame() {
    var j = {
        title: $("#title").val(),
        platform: $("#platform").val(),
        numcopies: $("#numcopies").val(),
        numboxed: $("#numboxed").val(),
        nummanuals: $("#nummanuals").val(),
        datepurchased: $("#datepurchased").val(),
        approximatepurchaseddate: $("#approximatepurchaseddate").is(":checked"),
        notes: $("#notes").val()
    };

    if (!validateSaveGame(j)) return;

    $.ajax({
        url: "/savegame",
        data: j,
        success: saveSuccess,
        error: saveError
    });
}

function validateSaveGame(j) {
    hideValidationFailure();

    var failureText = "";
    if (j.title=="") failureText = "Please enter a title";
    if (j.numcopies=="") failureText = appendText(failureText, "Please enter a number of copies");
    if (j.numboxed=="") failureText = appendText(failureText, "Please enter a number of boxes");
    if (j.nummanuals=="") failureText = appendText(failureText, "Please enter a number of manuals");

    var validatedSuccessfully = failureText == "";

    if (!validatedSuccessfully) showValidationFailure(failureText);
    return validatedSuccessfully;
}

function saveHardware() {

    var j = {
        name: $("#name").val(),
        platform: $("#platform").val(),
        numowned: $("#numowned").val(),
        numboxed: $("#numboxed").val(),
        notes: $("#notes").val()
    };

    if (!validateSaveHardware(j)) return;
    $.ajax({
        url: "/savehardware",
        data: j,
        success: saveSuccess,
        error: saveError
    })
}

function validateSaveHardware(j) {
    hideValidationFailure();

    var failureText = "";
    if (j.name == "") failureText = "Please enter a name";
    if (j.numowned == "") failureText = appendText(failureText, "Please enter number owned");
    if (j.numboxed == "") failureText = appendText(failureText, "Please enter number boxed");

    var validationSuccessful = failureText == "";
    if (!validationSuccessful) showValidationFailure(failureText);
    return validationSuccessful;
}

function appendText(t, a)
{
    if (t!="") t+="<br />";
    return t + a;
}

function updatePlatform() {
    var j = {
        id: $("#id").val(),
        name: $("#name").val(),
        description: $("#description").val()
    };
    $.ajax({
        url: "/updateplatform",
        data: j,
        success: saveSuccess,
        error: saveError
    })
}

function saveSuccess()
{
    showValidationSuccess("Save Successful");
    setTimeout(function() {
        hideValidationSuccess();
        window.history.back();
    }, 3000)
}

function saveError()
{
    showValidationFailure("Save Failed!");
}

function showValidationFailure(failureText)
{
    showValidationMessage($("#failure"), $("#failureText"), failureText);
}

function showValidationSuccess(successText)
{
    showValidationMessage($("#success"), $("#successText"), successText);
}

function showValidationMessage(box, boxTextCtrl, boxTextContent)
{
    box.fadeIn();
    boxTextCtrl.html(boxTextContent);
}

function hideValidationFailure()
{
    hideValidationBox($("#failure"), $("#failureText"));
}

function hideValidationSuccess()
{
    hideValidationBox($("#success"), $("#successText"));
}

function hideValidationBox(box, boxText)
{
    box.fadeOut(
    {
        complete: function() {
            boxText.html("");
        }
    })
}
