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
const dropdown_head = document.querySelectorAll(".dropdown-head");
const dropdowns = document.querySelectorAll(".drop-menu");

dropdown_head.forEach((item)=>{
    const dropdown = item.parentElement.lastElementChild;

    item.addEventListener("click",()=>{
        if(dropdown.classList.contains("show-drop-menu"))
            dropdown.classList.remove("show-drop-menu");
        else
            dropdown.classList.add("show-drop-menu");
    });

    item.addEventListener("mouseover",()=>{
        if(window.innerWidth < 850) return;
        dropdown.classList.add("show-drop-menu");

        item.addEventListener("mouseout",()=>{
            if(window.innerWidth < 850) return;
            dropdown.classList.remove("show-drop-menu");
        });
    });
    
    dropdown.addEventListener("mouseover",()=>{
        if(window.innerWidth < 850) return;
        dropdown.classList.add("show-drop-menu");
    });

    dropdown.addEventListener("mouseout",()=>{
        if(window.innerWidth < 850) return;
        dropdown.classList.remove("show-drop-menu");
    });
})

menu_button.addEventListener("click", ()=>{
    toggle_menu.classList.add("show-toggle-menu");
    menu_button.style.visibility="hidden";
    menu_close_button.style.visibility="visible";
})

menu_close_button.addEventListener("click", ()=>{
    toggle_menu.classList.remove("show-toggle-menu");
    menu_close_button.style.visibility="hidden";
    menu_button.style.visibility="visible";
})
