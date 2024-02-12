const burgerButton = document.getElementById("burger");
const menu = document.getElementById("menu");
const overlay = document.querySelector(".overlay");
const body = document.querySelector("body");
const FAQPage = document.getElementById("FAQPage");
const IndexPage = document.getElementById("index");
const tab = document.getElementById("defaultOpen");
const hasSubMenuElements = document.querySelectorAll(".has_sub_menu");
const mainElement = document.querySelector("main");
const productDetails = document.getElementById("product-dlt");
const contactPage = document.getElementById("contact-page");

// JavaScript For Header

burgerButton.addEventListener("click", function () {
  burgerButton.classList.toggle("active");
  overlay.classList.toggle("active");
  menu.classList.toggle("active");
});

overlay.addEventListener("click", function () {
  burgerButton.classList.remove("active");
  overlay.classList.remove("active");
  menu.classList.remove("active");
});

// dropdown

hasSubMenuElements.forEach(function (element) {
  element.addEventListener("mouseover", function () {
    const otherSubMenus = document.querySelectorAll(".sub_menu:not(.active)");
    otherSubMenus.forEach(function (subMenu) {
      subMenu.style.display = "none";
    });
    const subMenu = this.nextElementSibling;
    subMenu.style.display = "block";
  });
});


// JavaScript For Home Page/ Index Page
if (tab) {
  document.getElementById("defaultOpen").click();
}
function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
// PRODUCT DETAIL PAGE JAVASCRIPT:
$(document).ready(function () {
      setInterval(function () {
      $("#carouselExampleIndicators").carousel("next");
    }, 1000);

  $(".review-form").submit(function (e) {
    e.preventDefault();

    // Serialize form data
    var formData = $(this).serialize();
    var product_id = $("#product_id").val();

    // Submit form data via AJAX
    $.ajax({
      url: "/submit_review/" + product_id,
      type: "POST",
      dataType: "json",
      data: formData,
      success: function (response) {
        if (response.redirect) {
          // Redirect the user to the login page
          window.location.href = response.redirect;
      } else {
          // Display success message if review submitted successfully
          alert("Review submitted successfully!");
      }
          },
      error: function (xhr, status, error) {
        console.error(xhr.responseText);
      },
    });
  });

  if (body == productDetails) {
    var slider = $("#slider");
    var thumb = $("#thumb");
    var slidesPerPage = 4; //globaly define number of elements per page
    var syncedSecondary = true;
    slider
      .owlCarousel({
        items: 1,
        slideSpeed: 2000,
        nav: false,
        autoplay: false,
        dots: false,
        loop: true,
        responsiveRefreshRate: 200,
      })
      .on("changed.owl.carousel", syncPosition);
    thumb
      .on("initialized.owl.carousel", function () {
        thumb.find(".owl-item").eq(0).addClass("current");
      })
      .owlCarousel({
        items: slidesPerPage,
        dots: false,
        nav: true,
        item: 4,
        smartSpeed: 200,
        slideSpeed: 500,
        slideBy: slidesPerPage,
        navText: [
          '<svg width="18px" height="18px" viewBox="0 0 11 20"><path style="fill:none;stroke-width: 1px;stroke: #000;" d="M9.554,1.001l-8.607,8.607l8.607,8.606"/></svg>',
          '<svg width="25px" height="25px" viewBox="0 0 11 20" version="1.1"><path style="fill:none;stroke-width: 1px;stroke: #000;" d="M1.054,18.214l8.606,-8.606l-8.606,-8.607"/></svg>',
        ],
        responsiveRefreshRate: 100,
      })
      .on("changed.owl.carousel", syncPosition2);
    function syncPosition(el) {
      var count = el.item.count - 1;
      var current = Math.round(el.item.index - el.item.count / 2 - 0.5);
      if (current < 0) {
        current = count;
      }
      if (current > count) {
        current = 0;
      }
      thumb
        .find(".owl-item")
        .removeClass("current")
        .eq(current)
        .addClass("current");
      var onscreen = thumb.find(".owl-item.active").length - 1;
      var start = thumb.find(".owl-item.active").first().index();
      var end = thumb.find(".owl-item.active").last().index();
      if (current > end) {
        thumb.data("owl.carousel").to(current, 100, true);
      }
      if (current < start) {
        thumb.data("owl.carousel").to(current - onscreen, 100, true);
      }
    }
    function syncPosition2(el) {
      if (syncedSecondary) {
        var number = el.item.index;
        slider.data("owl.carousel").to(number, 100, true);
      }
    }
    thumb.on("click", ".owl-item", function (e) {
      e.preventDefault();
      var number = $(this).index();
      slider.data("owl.carousel").to(number, 300, true);
    });

    $(".qtyminus").on("click", function () {
      var now = $(".qty").val();
      if ($.isNumeric(now)) {
        if (parseInt(now) - 1 > 0) {
          now--;
        }
        $(".qty").val(now);
      }
    });
    $(".qtyplus").on("click", function () {
      var now = $(".qty").val();
      if ($.isNumeric(now)) {
        $(".qty").val(parseInt(now) + 1);
      }
    });
  }

  if (body === contactPage) {
    $("#signupForm").validate({
      rules: {
        name: "required",
        email: {
          required: true,
          email: true
        },
        message:
        {
          required: true,
          minlength: 20
        },
        subject:
        {
          required: true,
          minlength: 10
        }
      },
      messages: {
        name: "Please enter your firstname",
        email: {
          required: "Please enter a valid email address",
          email: "Please enter a valid email address"
        },
        message: {
          required: "Please Enter Your Message",
          minlength: "Your message must contain atleast 20 words"
        },
        subject: {
          required: "Please Enter Your Message",
          minlength: "Your message must contain atleast 10 words"
        }
      }
    });
  }
});
