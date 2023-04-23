(function($) {
	"use strict";
	var carousel = function() {
		$('.featured-carousel').owlCarousel({
	    loop: true,
	    autoplay: true,
	    margin:30,
	    animateOut: 'fadeOut',
	    animateIn: 'fadeIn',
	    nav:true,
	    dots: true,
	    autoplayHoverPause: false,
	    items: 1,
	    navText : ["<span class='ion-ios-arrow-back'></span>","<span class='ion-ios-arrow-forward'></span>"],
	    responsive:{
	      0:{
	        items:1
	      },
          400:{
            items:2
          },
	      600:{
	        items:3
	      },
	      1000:{
	        items:4
	      }
	    }
		});

	};
	carousel();
})(jQuery);

const menu_button = document.querySelector(".menu-button");
const menu_close_button = document.querySelector(".menu-close-button");
const toggle_menu = document.querySelector(".toggle-menu");
const dropdown_head = document.querySelectorAll(".dropdown-head");
const header = document.querySelector(".header");
const search_button = document.querySelector(".search-button");
const content_body = document.querySelector(".content-body");
const content_pseudo = document.createElement("style");
const disable_bg = `.content-body::before{
    position: absolute;
    z-index: 35;
    width: 100%;
    height: 100%;
    content: "";
    background-color: rgba(0, 0, 0, 0.349);
}`;
const enable_bg = `.content-body::before{
width: 0;
height: 0;
}`;

const open_menu = ()=>{
    toggle_menu.classList.add("show-toggle-menu");
    menu_button.style.visibility="hidden";
    menu_close_button.style.visibility="visible";

    // background disabled
    content_pseudo.innerHTML = disable_bg;
    search_button.classList.add("disable");
};
const close_menu = ()=>{
    toggle_menu.classList.remove("show-toggle-menu");
    menu_close_button.style.visibility="hidden";
    menu_button.style.visibility="visible";
    
    // background enabled
    content_pseudo.innerHTML = enable_bg;
    search_button.classList.remove("disable");
}

document.head.appendChild(content_pseudo);
menu_button.addEventListener("click", open_menu);
content_body.addEventListener("click",close_menu);
header.addEventListener("click",(e)=>{
    if(e.target == menu_button || e.target == menu_button.children[0]) return;
    close_menu();
});

onload = onresize = ()=>{
    let height_of_header = header.offsetHeight;
    let leftover_height = (window.innerHeight-height_of_header);
    
    content_body.style.marginTop = height_of_header+"px";
    if(content_body.offsetHeight <= leftover_height)
        content_body.style.height = leftover_height+"px";

    toggle_menu.style.marginTop = height_of_header+"px";
    toggle_menu.style.height = leftover_height+"px";

    if(window.innerWidth >= 1260)
    {
        // background enabled
        content_pseudo.innerHTML = enable_bg;
        search_button.classList.remove("disable");
    }
    else if(menu_button.style.visibility == "hidden")
    {
        // background disabled
        content_pseudo.innerHTML = disable_bg;
        search_button.classList.add("disable");
    }
};

dropdown_head.forEach((item)=>{
    const dropdown = item.parentElement.lastElementChild;

    item.addEventListener("click",()=>{
        if(dropdown.classList.contains("show-drop-menu"))
            dropdown.classList.remove("show-drop-menu");
        else
            dropdown.classList.add("show-drop-menu");
    });

    item.addEventListener("mouseover",()=>{
        if(window.innerWidth < 1260 || item.classList.contains("no-dropdown")) return;
        dropdown.classList.add("show-drop-menu");

        // disable content pseudo
        content_pseudo.innerHTML = disable_bg;
    });

    item.addEventListener("mouseout",()=>{
        if(window.innerWidth < 1260 || item.classList.contains("no-dropdown")) return;
        dropdown.classList.remove("show-drop-menu");

        // enable content pseudo
        content_pseudo.innerHTML = enable_bg;
    });
    
    dropdown.addEventListener("mouseover",()=>{
        if(window.innerWidth < 1260 || item.classList.contains("no-dropdown")) return;
        dropdown.classList.add("show-drop-menu");

        // disable content pseudo
        content_pseudo.innerHTML = disable_bg;
    });

    dropdown.addEventListener("mouseout",()=>{
        if(window.innerWidth < 1260 || item.classList.contains("no-dropdown")) return;
        dropdown.classList.remove("show-drop-menu");

        // enable content pseudo
        content_pseudo.innerHTML = enable_bg;
    });
})
