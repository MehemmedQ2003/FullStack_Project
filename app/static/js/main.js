 

$(function() {
    "use strict";
	
	
    $(window).on("load", function() {
        // 1. preloader
        $("#preloader").fadeOut(600);
        $(".preloader-bg").delay(400).fadeOut(600);
    });
	
    // 2. navigation
    // 2.1. page scroll
    $(".page-scroll").on("click", function(e) {
        var $anchor = $(this);
        $("html, body").stop().animate({
            scrollTop: $($anchor.attr("href")).offset().top - 70
        }, 1500, 'easeInOutExpo');
        e.preventDefault();
    });
    // 2.2. spy navigation
    $("body").scrollspy({
        target: ".navbar",
        // offset: 70
		offset: 80
    });
    // 2.3. close mobile menu
    $(".navbar-collapse ul li a").on("click", function() {
        $(".navbar-toggle:visible").click();
    });
    // 2.4. highlight navigation
    $(".link-underline-menu").on("click", function() {
        $(".link-underline-menu").removeClass("active");
        $(this).addClass("active");
    });
	
    $(window).on("scroll", function() {
        // 2.5. collapse navigation
        if ($(".navbar").offset().top > 50) {
            $(".navbar-bg-switch").addClass("main-navigation-bg");
        } else {
            $(".navbar-bg-switch").removeClass("main-navigation-bg");
        }
		
        // 3. animate elements
        if ($(this).scrollTop() > 10) {
            $(".border-top").addClass("top-position-primary");
            $(".main-navigation-bg").addClass("main-navigation-bg-position-primary");
            // $(".navbar-collapse").addClass("navbar-collapse-position-primary");
            $(".logo").addClass("logo-home-call");
            $(".main-navigation").addClass("main-navigation-home-call");
            $("h1.home-page-title").addClass("home-page-title-hide").removeClass("home-page-title-show");
			$("h2.home-page-subtitle").addClass("home-page-subtitle-hide").removeClass("home-page-subtitle-show");
            $(".scroll-indicator-wrapper").addClass("scroll-indicator-wrapper-position-secondary");
            $(".to-top-arrow").addClass("show");
        } else {
            $(".border-top").removeClass("top-position-primary");
            $(".main-navigation-bg").removeClass("main-navigation-bg-position-primary");
            // $(".navbar-collapse").removeClass("navbar-collapse-position-primary");
            $(".logo").removeClass("logo-home-call");
            $(".main-navigation").removeClass("main-navigation-home-call");
            $("h1.home-page-title").removeClass("home-page-title-hide").addClass("home-page-title-show");
			$("h2.home-page-subtitle").removeClass("home-page-subtitle-hide").addClass("home-page-subtitle-show");
            $(".scroll-indicator-wrapper").removeClass("scroll-indicator-wrapper-position-secondary");
            $(".to-top-arrow").removeClass("show");
        }
    });
	
    // 4. facts counter
    $(".facts-counter-number").appear(function() {
        var count = $(this);
        count.countTo({
            from: 0,
            to: count.html(),
            speed: 1200,
            refreshInterval: 60
        });
    });
	
    // 5. forms
    // 5.1. contact form
    $("form#form").on("submit", function() {
        $("form#form .error").remove();
        var s = !1;
        if ($(".requiredField").each(function() {
                if ("" === jQuery.trim($(this).val())) $(this).prev("label").text(), $(this).parent().append('<span class="error">This field is required</span>'), $(this).addClass(
                    "inputError"), s = !0;
                else if ($(this).hasClass("email")) {
                    var r = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
                    r.test(jQuery.trim($(this).val())) || ($(this).prev("label").text(), $(this).parent().append('<span class="error">Invalid email address</span>'), $(this).addClass(
                        "inputError"), s = !0);
                }
            }), !s) {
            $("form#form input.submit").fadeOut("normal", function() {
                $(this).parent().append("");
            });
            var r = $(this).serialize();
            $.post($(this).attr("action"), r, function() {
                $("form#form").slideUp("fast", function() {
                    $(this).before('<div class="success">Your email was sent successfully.</div>');
                });
            });
        }
        return !1;
    });
	
    // 6. slick slider
    // 6.1. slick testimonials slideshow, slick fullscreen slideshow
    $(".testimonials-slideshow, .slick-fullscreen-slideshow").slick({
        arrows: false,
        initialSlide: 0,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        fade: true,
        autoplay: true,
        autoplaySpeed: 4000,
        cssEase: "ease",
        speed: 1600,
        draggable: true,
        dots: false,
        pauseOnDotsHover: false,
        pauseOnFocus: false,
        pauseOnHover: false
    });
	// 6.2. slick fullscreen slideshow ZOOM/FADE
    $(".slick-fullscreen-slideshow-zoom-fade").slick({
        arrows: false,
        initialSlide: 0,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        fade: true,
        autoplay: true,
        autoplaySpeed: 4000,
        cssEase: "cubic-bezier(0.7, 0, 0.3, 1)",
        speed: 1600,
        draggable: true,
        dots: false,
        pauseOnDotsHover: true,
        pauseOnFocus: false,
        pauseOnHover: false
    });
    // 6.3. slick fullscreen slider TYPED text
    $(".slick-fullscreen").slick({
        arrows: false,
        initialSlide: 0,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        fade: false,
        autoplay: true,
        autoplaySpeed: 4000,
        cssEase: "ease",
        speed: 1400,
        draggable: true,
        dots: false,
        pauseOnDotsHover: true,
        pauseOnFocus: false,
        pauseOnHover: false
    });
	
    // 7. YouTube player
	$("#bgndVideo").YTPlayer();
	
    // 8. owl carousel
    // 8.1. owl news carousel
    $("#news-carousel").owlCarousel({
        loop: true,
        center: true,
        items: 3,
        margin: 0,
        autoplay: false,
        autoplaySpeed: 1000,
        autoplayTimeout: 3500,
        smartSpeed: 450,
        nav: true,
        navText: ["<i class='owl-custom ion-chevron-left'></i>", "<i class='owl-custom ion-chevron-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            1170: {
                items: 1
            }
        }
    });
	
    // 9. magnificPopup
    // 9.1. magnificPopup works gallery
    $(".popup-photo").magnificPopup({
        type: "image",
        gallery: {
            enabled: true,
            tPrev: "",
            tNext: "",
            tCounter: "%curr% / %total%"
        },
        removalDelay: 100,
        mainClass: "mfp-fade ",
        fixedContentPos: false
    });
	
	// 10. swiper slider
    // 10.1. swiper parallax slider
    var swiper = new Swiper(".parallax .swiper-container", {
        autoplay: 4000,
        speed: 800,
        parallax: true,
        mousewheelControl: false,
        keyboardControl: false,
        nextButton: ".swiper-button-next",
        prevButton: ".swiper-button-prev",
        paginationClickable: true
    });
    // 10.2. swiper thumbnail slider horizontal thumbs
    var swipersliderTop = new Swiper(".swiper-slider-top", {
        direction: "vertical",
        nextButton: ".swiper-button-next",
        prevButton: ".swiper-button-prev",
        autoplay: 4000,
        speed: 1600,
        spaceBetween: 0,
        centeredSlides: true,
        slidesPerView: "auto",
        touchRatio: 1,
        loop: true,
        slideToClickedSlide: true,
        mousewheelControl: false,
        keyboardControl: false
    });
    var swipersliderBottom = new Swiper(".swiper-slider-bottom", {
        direction: "horizontal",
        spaceBetween: 10,
        centeredSlides: true,
        slidesPerView: "auto",
        touchRatio: 1,
        loop: true,
        slideToClickedSlide: true,
        mousewheelControl: false,
        keyboardControl: false
    });
    swipersliderTop.params.control = swipersliderBottom;
    swipersliderBottom.params.control = swipersliderTop;

});


let nextButton = document.getElementById('next');
let prevButton = document.getElementById('prev');
let carousel = document.querySelector('.carousel');
let listHTML = document.querySelector('.carousel .list');
let seeMoreButtons = document.querySelectorAll('.seeMore');
let backButton = document.getElementById('back');

nextButton.onclick = function(){
    showSlider('next');
}
prevButton.onclick = function(){
    showSlider('prev');
}
let unAcceppClick;
const showSlider = (type) => {
    nextButton.style.pointerEvents = 'none';
    prevButton.style.pointerEvents = 'none';

    carousel.classList.remove('next', 'prev');
    let items = document.querySelectorAll('.carousel .list .item');
    if(type === 'next'){
        listHTML.appendChild(items[0]);
        carousel.classList.add('next');
    }else{
        listHTML.prepend(items[items.length - 1]);
        carousel.classList.add('prev');
    }
    clearTimeout(unAcceppClick);
    unAcceppClick = setTimeout(()=>{
        nextButton.style.pointerEvents = 'auto';
        prevButton.style.pointerEvents = 'auto';
    }, 2000)
}
seeMoreButtons.forEach((button) => {
    button.onclick = function(){
        carousel.classList.remove('next', 'prev');
        carousel.classList.add('showDetail');
        backButton.style.display="block"
    }
});
backButton.onclick = function(){
    carousel.classList.remove('showDetail');
    backButton.style.display="none"
}



 
let items = document.querySelectorAll('.sliderbpx .listbpx .itembpx');
let nextbpx = document.getElementById('nextbpx');
let prevbpx = document.getElementById('prevbpx');

// config param
let countItem = items.length;
let itemActive = 0;
// event next click
nextbpx.onclick = function(){
    itemActive = itemActive + 1;
    if(itemActive >= countItem){
        itemActive = 0;
    }
    showsliderbpxbpx();
}
//event prevbpx click
prevbpx.onclick = function(){
    itemActive = itemActive - 1;
    if(itemActive < 0){
        itemActive = countItem - 1;
    }
    showsliderbpxbpx();
}
// auto run sliderbpxbpx
let refreshInterval = setInterval(() => {
    nextbpx.click();
}, 5000)

function showsliderbpxbpx(){
    // remove item active old
    let itemActiveOld = document.querySelector('.sliderbpx .listbpx .itembpx.active');
    itemActiveOld.classList.remove('active');

    // active new item
    items[itemActive].classList.add('active');

    // clear auto time run sliderbpxbpx
    clearInterval(refreshInterval);
    refreshInterval = setInterval(() => {
        nextbpx.click();
    }, 5000)
}

 

 refreshInterval = setInterval(() => {
    nextbpx.click();
}, 5000);



window.addEventListener('scroll', function() {
    var header = document.querySelector('header');
    if (window.scrollY > 30) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

document.querySelector('.mobile-menu-icon').addEventListener('click', function() {
    var icon = this.querySelector('i');
    var menu = document.querySelector('nav ul.menu');
    
     if (icon.classList.contains('fa-bars')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-xmark');
    } else {
        icon.classList.remove('fa-xmark');
        icon.classList.add('fa-bars');
    }
    
     menu.classList.toggle('active');
});

 var menuLinks = document.querySelectorAll('nav ul.menu li a');
menuLinks.forEach(function(link) {
    link.addEventListener('click', function(event) {
          numOfClicks = 0;
         bodyEl.style.overflow = "auto";
        menuLinks.forEach(function(link) {
            link.classList.remove('clicked');
        });
         this.classList.add('clicked');
         document.querySelector('nav ul.menu').classList.remove('active');
         document.querySelector('.mobile-menu-icon i').classList.remove('fa-xmark');
        document.querySelector('.mobile-menu-icon i').classList.add('fa-bars');
         event.preventDefault();  
        var targetId = this.getAttribute('href').substring(1);  
        var targetElement = document.getElementById(targetId);  
        if (targetElement) {
            var offsetTop = targetElement.offsetTop;  
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'  
            });
        }
    });
});

let numOfClicks = 0;
const trigger = document.querySelector(".mobile-menu-icon");
const bodyEl = document.getElementsByTagName("body")[0];

trigger.onclick = () => {
    numOfClicks += 1;
    const isNumOfClicksEven = numOfClicks % 2 === 0;
    isNumOfClicksEven ? bodyEl.style.overflow = "auto" : bodyEl.style.overflow = "hidden";
};
 


 document.addEventListener('DOMContentLoaded', function() {
    var checkbox = document.querySelector('.hamburger input');
    var menu = document.querySelector('nav ul.menu');
    var links = document.querySelectorAll('nav ul.menu li a');  
    
    checkbox.addEventListener('change', function() {
        if (this.checked) {
            menu.classList.add('active');
            document.body.style.overflow = 'hidden'; 
        } else {
            menu.classList.remove('active');
            document.body.style.overflow = '';  
        }
    });

     links.forEach(function(link) {
        link.addEventListener('click', function() {
            menu.classList.remove('active');
            checkbox.checked = false;  
            document.body.style.overflow = '';  
        });
    });

     document.addEventListener('click', function(event) {
        if (!menu.contains(event.target) && !checkbox.checked) {
            menu.classList.remove('active');
            checkbox.checked = false;  
            document.body.style.overflow = '';  
        }
    });
});


// document.querySelector(".colorlight-left").addEventListener("click", function() {
    
//     var youtubeURL = "https://en.colorlightinside.com/";
  
//     window.open(youtubeURL, "_blank");
// });


// document.querySelector(".bms-left").addEventListener("click", function() {
    
//     var youtubeURL = "https://briteminds.ae";
//     window.open(youtubeURL, "_blank");
// });

// document.querySelector(".chipshow-left").addEventListener("click", function() {
    
//     var youtubeURL = "https://led.chipshow.com/";
//     window.open(youtubeURL, "_blank");
// });

// document.querySelector(".reefilm-left").addEventListener("click", function() {
    
//     var youtubeURL = "https://www.reefilm-led.com/";
//     window.open(youtubeURL, "_blank");
// });