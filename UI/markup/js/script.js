function cancelEdit() {
    window.location = "/";
}

function cancelEditPlatform() {
    window.location = "/platforms";
}

function showDeleteConfirm() {
    $("#deleteConfirm").addClass("text-danger").removeClass("hidden");
}

function hideDeleteConfirm() {
    $("#deleteConfirm").addClass("hidden").removeClass("text-danger");
}

function deleteGame() {
    window.location = "/deletegame?gameid=" + $("#id").val();
}

function deletePlatform() {
    window.location = "/deleteplatform?platformid=" + $("#id").val();
}

function deleteHardware() {
    window.location = "/deletehardware?hardwareid=" + $("#id").val();
}

function editGame(game_id) {
    window.location = "/editgame?gameid=" + game_id;
}

function editHardware(hardware_id) {
    window.location = "/edithardware?hardwareid=" + hardware_id;
}

function editPlatform(id) {
    window.location = "/editplatform?platformid=" + id
}

function addSuggestedPlatform(name, description) {
    window.location = "/addplatform?name=" + name + "&description=" + description
}