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
    navigate("/deletegame?gameid=" + $("#id").val());
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

function editGenre(id) {
    navigate("/editgenre?genreid=" + id);
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

    $.ajax({
        url: "/savegame",
        data: j,
        success: saveSuccess,
        error: saveError
    });
}

function saveSuccess()
{
    $("#success").fadeIn();
    $("#successText").text("Save Successful");
    setTimeout(function() {
        $("#success").fadeOut();
        window.history.back();
    }, 3000)
}

function saveError()
{
    $("#failureText").text("Saved Failed!");
    $("#failure").fadeIn();
}
