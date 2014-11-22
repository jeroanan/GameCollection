function cancelEdit() {
    window.location = "/";
}

function cancelEditPlatform() {
    window.location = "/platforms";
}

function showDeleteConfirm() {
    document.getElementById("deleteConfirm").className="text-danger";
}

function hideDeleteConfirm() {
    document.getElementById("deleteConfirm").className="hidden";
}

function doDelete() {
    var gameId = document.getElementById("id").value;
    window.location = "/deletegame?gameid=" + gameId;
}

function deletePlatform() {
    var gameId = document.getElementById("id").value;
    window.location = "/deleteplatform?platformid=" + gameId;
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