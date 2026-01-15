function openLogin() {
    document.getElementById("loginModal").style.display = "flex";
}

function closeLogin() {
    document.getElementById("loginModal").style.display = "none";
}

/* LOGIN FAKE */
function fakeLogin(event) {
    event.preventDefault(); // evita recargar
    window.location.href = "/dashboard";
}
