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
}
const open_menu = ()=>{
    toggle_menu.classList.add("show-toggle-menu");
    menu_button.style.visibility="hidden";
    menu_close_button.style.visibility="visible";
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
        if(window.innerWidth < 1260) return;
        dropdown.classList.add("show-drop-menu");

        item.addEventListener("mouseout",()=>{
            if(window.innerWidth < 1260) return;
            dropdown.classList.remove("show-drop-menu");
        });
    });
    
    dropdown.addEventListener("mouseover",()=>{
        if(window.innerWidth < 1260) return;
        dropdown.classList.add("show-drop-menu");
    });

    dropdown.addEventListener("mouseout",()=>{
        if(window.innerWidth < 1260) return;
        dropdown.classList.remove("show-drop-menu");
    });
})
