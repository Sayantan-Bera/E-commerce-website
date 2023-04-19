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
const dropdowns = document.querySelectorAll(".drop-menu");
const header = document.querySelector(".header");
const header_first = document.querySelector(".header-first");
const search_input = document.querySelector(".search-input");
const content_body = document.querySelector(".content-body");
const close_menu = ()=>{
    toggle_menu.classList.remove("show-toggle-menu");
    menu_close_button.style.visibility="hidden";
    menu_button.style.visibility="visible";
    
    // background enabled
    content_body.classList.remove("blur-content");
    [...content_body.children].forEach((item)=>{
        item.classList.remove("disable");
    });
}
const open_menu = ()=>{
    toggle_menu.classList.add("show-toggle-menu");
    menu_button.style.visibility="hidden";
    menu_close_button.style.visibility="visible";

    // background disabled
    content_body.classList.add("blur-content");
    [...content_body.children].forEach((item)=>{
        item.classList.add("disable");
    });
};

menu_button.addEventListener("click", open_menu);
menu_close_button.addEventListener("click",close_menu);
content_body.addEventListener("click",close_menu);
header_first.addEventListener("click",close_menu);
search_input.addEventListener("click",close_menu);

onload = onresize = ()=>{
    let height_of_header = header.offsetHeight;
    let leftover_height = (window.innerHeight-height_of_header)+"px";
    toggle_menu.style.marginTop = height_of_header+"px";
    content_body.style.marginTop = height_of_header+"px";
    toggle_menu.style.height = leftover_height;
    if(window.innerWidth >= 1260)
    {
        // background enabled
        content_body.classList.remove("blur-content");
        [...content_body.children].forEach((item)=>{
            item.classList.remove("disable");
        });
    }
    else if(menu_button.style.visibility == "hidden")
    {
        // background disabled
        content_body.classList.add("blur-content");
        [...content_body.children].forEach((item)=>{
            item.classList.add("disable");
        });
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
        content_body.classList.add("blur-content");
    });

    item.addEventListener("mouseout",()=>{
        if(window.innerWidth < 1260 || item.classList.contains("no-dropdown")) return;
        dropdown.classList.remove("show-drop-menu");
        content_body.classList.remove("blur-content");
    });
    
    dropdown.addEventListener("mouseover",()=>{
        if(window.innerWidth < 1260 || item.classList.contains("no-dropdown")) return;
        dropdown.classList.add("show-drop-menu");
        content_body.classList.add("blur-content");
    });

    dropdown.addEventListener("mouseout",()=>{
        if(window.innerWidth < 1260 || item.classList.contains("no-dropdown")) return;
        dropdown.classList.remove("show-drop-menu");
        content_body.classList.remove("blur-content");
    });
})
