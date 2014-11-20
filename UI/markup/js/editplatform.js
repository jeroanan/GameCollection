function cancelEdit() {
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
    window.location = "/deleteplatform?platformid=" + gameId;
}
