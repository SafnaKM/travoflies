var preloader=document.getElementById("pre-loader");
window.addEventListener("load",function(){
    preloader.style.display="none";
});
// responsive menu
const menuBtn= document.querySelector('.menu-btn');
const menu= document.querySelector('.menu');
    menuBtn.addEventListener("click",() =>{
        menuBtn.classList.toggle("active");
        menu.classList.toggle("active");
});
// video slider navigation

const btns = document.querySelectorAll(".nav-btn");
const slides = document.querySelectorAll(".video-slide");
const contents = document.querySelectorAll(".content");

let currentIndex = 0;
const slideInterval = 6000; // 5000ms = 5 seconds

const sliderNav = (index) => {
    btns.forEach((btn, i) => {
        btn.classList.toggle("active", i === index);
        slides[i].classList.toggle("active", i === index);
        contents[i].classList.toggle("active", i === index);
    });
    currentIndex = index;
};

const nextSlide = () => sliderNav((currentIndex + 1) % btns.length);

let autoPlay = setInterval(nextSlide, slideInterval);

btns.forEach((btn, i) => {
    btn.addEventListener("click", () => {
        sliderNav(i);
        clearInterval(autoPlay);
        autoPlay = setInterval(nextSlide, slideInterval);
    });
});
