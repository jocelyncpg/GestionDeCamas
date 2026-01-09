function showLogin() {
    window.location.href = "/login";
}
function openLogin() {
    document.getElementById("loginModal").style.display = "flex";
}

function closeLogin() {
    document.getElementById("loginModal").style.display = "none";
}

let currentSlide = 0;
const slides = document.querySelectorAll(".carousel-slide");
const dots = document.querySelectorAll(".dot");

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.toggle("active", i === index);
        dots[i].classList.toggle("active", i === index);
    });
    currentSlide = index;
}

setInterval(() => {
    let next = (currentSlide + 1) % slides.length;
    showSlide(next);
}, 5000);

dots.forEach((dot, index) => {
    dot.addEventListener("click", () => showSlide(index));
});
