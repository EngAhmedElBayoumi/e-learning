(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });

    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });


    // Post carousel
    $(".post-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:2
            }
        }
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        center: true,
        autoplay: true,
        smartSpeed: 2000,
        dots: true,
        loop: true,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
})(jQuery);
var pri=document.getElementById('primary')
var med=document.getElementById('middle')
var high=document.getElementById('high')
var pri_teacher=document.getElementById('primary-teacher')
var med_teacher=document.getElementById('middle-teacher')
var high_teacher=document.getElementById('high-teacher')
pri.style.display="none"
med.style.display="none"
high.style.display="none"
pri_teacher.style.display="none"
med_teacher.style.display="none"
high_teacher.style.display="none"
function Choose(){

if(document.getElementById('choose-level').value == "1"){
med.style.display="none"
high.style.display="none"
pri.style.display="block"
pri_teacher.style.display="block"
med_teacher.style.display="none"
high_teacher.style.display="none"

}else if(document.getElementById('choose-level').value == "2"){
    pri.style.display="none"
    high.style.display="none"
    med.style.display="block"
    pri_teacher.style.display="none"
    med_teacher.style.display="block"
    high_teacher.style.display="none"
}else if(document.getElementById('choose-level').value == "3"){
    pri.style.display="none"
    med.style.display="none"
    high.style.display="block"
    pri_teacher.style.display="none"
    med_teacher.style.display="none"
    high_teacher.style.display="block"  
   
}else{
    pri.style.display="none"
    med.style.display="none"
    high.style.display="none" 
    pri_teacher.style.display="none"
    med_teacher.style.display="none"
    high_teacher.style.display="none"
}
}

