function cancelEdit() {
    window.location = "/";
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
