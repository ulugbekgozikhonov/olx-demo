let currentSlide = 0;
const slides = document.querySelectorAll(".slide");

function changeSlide(direction) {
    const slider = document.querySelector(".slider");
    currentSlide = (currentSlide + direction + slides.length) % slides.length;

    // Slayderni yangi rasmga siljitish
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
}
