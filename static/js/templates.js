// Navbar Scroll
$(document).ready(function() {
    $(window).scroll(function() {
        if ($(document).scrollTop() > 80) {
            $('#nav').addClass('navbar-fixed-top');
        }
        else {
            $('#nav').removeClass('navbar-fixed-top');
        }
    });
});
// Alert notifications

function registerVer() {
    swal({
      title: "You've signed up!",
      text: "Thanks for Joining the community",
      icon: "success"
    });
}

function loginVer() {
    swal({
      title: "You're In!",
      icon: "success"
    });
}

function logout() {
    swal({
        title: "You have logged out!",
        icon: "success"
    });
}

// Image zoom function

$(function() {
    var mousehov=
        function() {
        $(this).css("opacity", "0").addClass("pics-over").animate({height:"500px", opacity:"1"});
        };

    var mouseoff=
        function() {$(this).removeClass("pics-over").animate({height:"200px"})}

    $(".recipe-thumb").children().hover(mousehov, mouseoff);

    });

// Twenty Twenty image

$(function() {
    $("#about-img[data-orientation!='vertical']").twentytwenty({default_offset_pct:0.5})
});

