$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

const menu_button = document.querySelector(".menu-button");
const menu_close_button = document.querySelector(".menu-close-button");
const toggle_menu = document.querySelector(".toggle-menu");

menu_button.addEventListener("click", ()=>{
    toggle_menu.style.visibility="visible";
    menu_button.style.visibility="hidden";
    menu_close_button.style.visibility="visible";
})

menu_close_button.addEventListener("click", ()=>{
    toggle_menu.style.visibility="hidden";
    menu_close_button.style.visibility="hidden";
    menu_button.style.visibility="visible";
})