//DOM ELEMENTS
const selectElement = (element) => document.querySelector(element);
const h_scrolling = document.querySelectorAll(".circle");
const left_scrolling_button = document.querySelector(".left");
const right_scrolling_button = document.querySelector(".right");
const view = document.querySelector("#view");

const cover_title = document.querySelector(".cover-title");
const cover_text = document.querySelector(".cover-text");
const cover_image = document.querySelector(".cover-image");
const cover_image_first = document.querySelector(".first");
const ad_wrapper = document.querySelector(".ad-wrapper");
const ad_image = document.querySelectorAll(".ad-col2 img");

const content1 = document.getElementById("content1");
const content2 = document.getElementById("content2");
const content3 = document.getElementById("content3");
const content = document.querySelector(".content");

const container = document.querySelector(".thumbnail-container");
const controls = document.querySelector(".controls");
const allBox = container.children;
const containerWidth = container.offsetWidth;
const margin = 30;
var items = 0;
var totalItems = 0;
var jumpSlideWidth = 0;

const slides = document.querySelector(".test-slider").children;
const indicatorImages = document.querySelector(".test-indicator").children;
let test_index = 0;

const subscribe = document.querySelector("#footer-email-btn");
const mail = document.querySelector("#footer-email");

// items setup per slide

responsive = [
  { breakPoint: { width: 0, item: 1 } }, //if wdth greater than 0 display 1 item
  { breakPoint: { width: 600, item: 2 } }, //if wdth greater than 600 display 2 item
  { breakPoint: { width: 1000, item: 4 } }, //if wdth greater than 1000 display 4 item
];

function load() {
  let height = content2.clientHeight.toString();
  ad_wrapper.style.height = height + "px";
  for (let i = 0; i < responsive.length; i++) {
    if (window.innerWidth > responsive[i].breakPoint.width) {
      items = responsive[i].breakPoint.item;
    }
  }
  start();
}

function start() {
  var totalItemsWidth = 0;
  for (let i = 0; i < allBox.length; i++) {
    //width and margin setup for items
    allBox[i].style.width = containerWidth / items - margin + "px";
    allBox[i].style.margin = margin / 2 + "px";
    totalItemsWidth += containerWidth / items;
    totalItems++;
  }
  //thumbnail-container width setup
  container.style.width = totalItemsWidth + "px";

  //slide control numbers set up
  const allSlides = Math.ceil(totalItems / items);
  const ul = document.createElement("ul");
  for (let i = 1; i <= allSlides; i++) {
    const li = document.createElement("li");
    li.id = i;
    li.innerHTML = i;
    li.setAttribute("onclick", "controlSlides(this)");
    ul.appendChild(li);
    if (i === 1) {
      li.className = "active";
    }
  }
  controls.appendChild(ul);
}

// when click on numbers slide to next slide
function controlSlides(event) {
  //select control ul element
  const ul = controls.children;
  //select il children 'li'
  const li = ul[0].children;
  var active;
  for (let i = 0; i < li.length; i++) {
    if (li[i].className == "active") {
      active = i;
      li[i].className = "";
    }
  }
  //add active class to selected
  event.className = "active";

  var number = event.id - 1 - active;
  jumpSlideWidth = jumpSlideWidth + containerWidth * number;
  container.style.marginLeft = -jumpSlideWidth + "px";
}

window.onload = load();

// selectElement('.menu-icons').addEventListener('click',()=>{
// 	selectElement('.container-nav').classList.toggle('active');
// });

//Variables

let circle_active = "col8 circle circle-active";
let circle = "col8 circle";
let index;
let scroll_index = 1;

//Functions
//For Scrolling
let class_present = (array, class_name) => {
  for (i = 0; i < array.length; i++) {
    if (array[i].className === class_name) {
      return i;
    }
  }
};

function change_template(index) {
  switch (index) {
    case 0:
      cover_title.innerHTML = "Focused on First Years";
      cover_text.innerHTML =
        "Get good qualtity drafters straight from the hands from your trusty 		seniors and make your drawing classes easy and interesting.";
      cover_image_first.style.marginLeft = "0%";
      view.innerHTML = "View Now";
      view.href = "/store/search/?q=drafter";
      break;

    case 1:
      cover_title.innerHTML = "Sell It Out!";
      cover_text.innerHTML =
        "What is point in keeping something that you dont use? Someone might need it. Sell it Out! and get the value";
      cover_image_first.style.marginLeft = "-111.3%";
      view.innerHTML = "Sell Now";
      view.href = "/account/profile/sell/new/";
      break;

    case 2:
      cover_title.innerHTML = "Wanna Buy or Sell Furnitures";
      cover_text.innerHTML =
        "Need some Furnitures. Check it Out. Watch it out and choose a best one suitable for you.";
      cover_image_first.style.marginLeft = "-222.4%";
      view.href = "/store/Homes%20and%20Furnitures";
      view.innerHTML = "View Now";
      break;

    case 3:
      cover_title.innerHTML = "Get Electric With GaaKU";
      cover_text.innerHTML =
        "Buy electronics, gadgets and electric devices in GaaKU at lowest price. Experience satisfying and hassle-free online shopping.";
      cover_image_first.style.marginLeft = "-333.4%";
      view.href = "/store/Electronics";
      view.innerHTML = "View Now";
      break;

    case 4:
      cover_title.innerHTML = "Looking for Books and Notes...";
      cover_text.innerHTML =
        "Come on this the fountain to drink the knowledge. Make difficult subjects easier. Look for your particular notes.";
      cover_image_first.style.marginLeft = "-444.4%";
      view.href = "/store/Education%20Materials";
      view.innerHTML = "View Now";
      break;

    case 5:
      cover_title.innerHTML = "Checking Out For Spares";
      cover_text.innerHTML =
        "GaaKU is the right place for you to find what you want. Go GaaKU!!!";
      cover_image_first.style.marginLeft = "-555.4%";
      view.href = "	/store/Other%20Accessories";
      view.innerHTML = "View Now";
      break;
    default:
      break;
  }
}

let index_position = (array, position_shift) => {
  index = class_present(array, circle_active);
  array[index].className = circle;
  if (position_shift === "right") {
    index = (index + 1) % array.length;
  } else {
    index = (index - 1) % array.length;
  }
  if (index < 0) {
    index = array.length - 1;
  }
  array[index].className = circle_active;
  change_template(index);
};

function image_resize() {
  for (i = 0; i < ad_image.length; i++) {
    console.log(ad_image[i].clientHeight);
  }
}

function element_resize(element1, element2) {}

// subscribe.addEventListener('click',function(){
// 	alert("You have sucessfully subscribed");
// })

right_scrolling_button.addEventListener("click", function () {
  index_position(h_scrolling, "right");
});

left_scrolling_button.addEventListener("click", function () {
  index_position(h_scrolling, "left");
});

setInterval(function () {
  index_position(h_scrolling, "right");
  scroll_index++;
  if (scroll_index > 3) {
    scroll_index = 1;
  }
  switch (scroll_index) {
    case 1:
      content1.style.transform = "translateX(0px)";
      content2.style.transform = "translateX(150%)";
      content3.style.transform = "translateX(150%)";
      content1.style.transitionDelay = "0.3s";
      content2.style.transitionDelay = "0s";
      content3.style.transitionDelay = "0s";
      break;
    case 2:
      content1.style.transform = "translateX(150%)";
      content2.style.transform = "translateX(0px)";
      content3.style.transform = "translateX(150%)";
      content1.style.transitionDelay = "0s";
      content2.style.transitionDelay = "0.3s";
      content3.style.transitionDelay = "0s";
      break;
    case 3:
      content1.style.transform = "translateX(150%)";
      content2.style.transform = "translateX(150%)";
      content3.style.transform = "translateX(0px";
      content1.style.transitionDelay = "0s";
      content2.style.transitionDelay = "0s";
      content3.style.transitionDelay = "0.3s";
      break;
  }

  test_index++;
  if (test_index >= indicatorImages.length) {
    test_index = 0;
  }
  for (let j = 0; j < indicatorImages.length; j++) {
    indicatorImages[j].classList.remove("active");
  }
  indicatorImages[test_index].classList.add("active");
  for (let j = 0; j < slides.length; j++) {
    slides[j].classList.remove("active");
  }
  slides[test_index].classList.add("active");
}, 5000);

$(window).resize(function () {
  let height = content2.clientHeight.toString();
  ad_wrapper.style.height = height + "px";
});
