document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll(".carousel-slide");
    const dots = document.querySelectorAll(".dot");
    let currentIndex = 0;

    function showSlide(index) {
        slides.forEach(function (slide, i) {
            slide.classList.toggle("active", i === index);
            dots[i].classList.toggle("active", i === index);
        });
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    // Auto-play cada 5 segundos
    setInterval(nextSlide, 5000);

    // Click en los dots
    dots.forEach(function (dot, index) {
        dot.addEventListener("click", function () {
            currentIndex = index;
            showSlide(currentIndex);
        });
    });
});
