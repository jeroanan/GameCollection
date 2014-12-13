function cancelEdit() {
    navigate("/");
}

function cancelEditPlatform() {
    navigate("/platforms");
}

function showDeleteConfirm() {
    $("#deleteConfirm").addClass("text-danger").removeClass("hidden");
}

function hideDeleteConfirm() {
    $("#deleteConfirm").addClass("hidden").removeClass("text-danger");
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
