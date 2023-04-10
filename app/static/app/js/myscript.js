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
        if(window.innerWidth < 1000) return;
        dropdown.classList.add("show-drop-menu");

        item.addEventListener("mouseout",()=>{
            if(window.innerWidth < 1000) return;
            dropdown.classList.remove("show-drop-menu");
        });
    });
    
    dropdown.addEventListener("mouseover",()=>{
        if(window.innerWidth < 1000) return;
        dropdown.classList.add("show-drop-menu");
    });

    dropdown.addEventListener("mouseout",()=>{
        if(window.innerWidth < 1000) return;
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
