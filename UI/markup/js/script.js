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
        success: function() {
            showValidationSuccess("Deletion successful");
            setTimeout(function() {
                hideValidationSuccess();
                window.history.back();
            }, 3000)
        },
        error: function() {showValidationFailure("Deletion failed")}
    });
}

function deletePlatform() {
    navigate("/deleteplatform?platformid=" + $("#id").val());
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

    if (!validateSave(j)) return;

    $.ajax({
        url: "/updategame",
        data: j,
        success: saveSuccess,
        error: saveError
    });
}

function saveGame()
{
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


    if (!validateSave(j)) return;

    $.ajax({
        url: "/savegame",
        data: j,
        success: saveSuccess,
        error: saveError
    });
}

function validateSave(j)
{
    hideValidationFailure();

    function appendText(t, a)
    {
        if (t!="") t+="<br />";
        return t + a;
    }

    var failureText = "";
    if (j.title=="") failureText += "Please enter a title";
    if (j.numcopies=="") failureText = appendText(failureText, "Please enter a number of copies");
    if (j.numboxed=="") failureText = appendText(failureText, "Please enter a number of boxes");
    if (j.nummanuals=="") failureText = appendText(failureText, "Please enter a number of manuals");

    var validatedSuccessfully = failureText == "";

    if (!validatedSuccessfully) showValidationFailure(failureText);
    return validatedSuccessfully;
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
