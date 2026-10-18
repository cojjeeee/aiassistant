function updateOnlineStatus() {
    var offlineMessage = document.getElementById("offline-message");

    if (navigator.onLine) {
        offlineMessage.style.display = "none";
    } else {
        offlineMessage.style.display = "block";
    }
}

window.addEventListener("online", updateOnlineStatus);
window.addEventListener("offline", updateOnlineStatus);

updateOnlineStatus();