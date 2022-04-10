
// ==========================DETAILS_TAB==================

var detailstabLinks = document.querySelectorAll(".detailstablinks");
var detailstabContent = document.querySelectorAll(".detailstabcontent");


detailstabLinks.forEach(function(el) {
    el.addEventListener("click", detailsopenTabs);
});


function detailsopenTabs(el) {
    var detailsbtnTarget = el.currentTarget;
    var detailsvaluetxt = detailsbtnTarget.dataset.valuetxt;

    detailstabContent.forEach(function(el) {
        el.classList.remove("detailsactive");
    });

    detailstabLinks.forEach(function(el) {
        el.classList.remove("detailsactive");
    });

    document.querySelector("#" + detailsvaluetxt).classList.add("detailsactive");

    detailsbtnTarget.classList.add("detailsactive");
}


// ==========================DETAILS_TAB==================
var pagenumber1 = 1;
console.log(pagenumber1);
slidechenger1(1);


function plusslides1(n) {
    slidechenger1(pagenumber1 += n)
}

function currentslide1(n) {
    slidechenger1(pagenumber1 = n);
}

function slidechenger1(n) {
    var i;
    var page = document.getElementsByClassName("p1-page");
    var number = document.getElementsByClassName("dot1");
    if (n > page.length) { pagenumber1 = 1 }
    if (n < 1) { pagenumber1 = page.length }
    for (i = 0; i < page.length; i++) {
        page[i].style.display = "none";
    }
    for (i = 0; i < number.length; i++) {
        number[i].classList.remove("dot-active");
    }
    page[pagenumber1 - 1].style.display = "block";
    number[pagenumber1 - 1].classList.add("dot-active");
}
// ======================MENU=====================

var tabLinks = document.querySelectorAll(".tablinks");
var tabContent = document.querySelectorAll(".tabcontent");


tabLinks.forEach(function(el) {
    el.addEventListener("click", openTabs);
});


function openTabs(el) {
    var btnTarget = el.currentTarget;
    var valuetxt = btnTarget.dataset.valuetxt;

    tabContent.forEach(function(el) {
        el.classList.remove("active");
    });

    tabLinks.forEach(function(el) {
        el.classList.remove("active");
    });

    document.querySelector("#" + valuetxt).classList.add("active");

    btnTarget.classList.add("active");
}

function menufunc() {
    var toggeler = document.getElementById("menu-list").style.display
    if (toggeler == "none") document.getElementById("menu-list").style.display = "flex";
    if (toggeler == "flex") document.getElementById("menu-list").style.display = "none";

}
// ======================MENU=====================
// ======================SEARCH_MENU==============
function myFunction() {
    document.getElementById("search-box").style.display = "block";
}

function myFunction2() {
    document.getElementById("search-box").style.display = "none";
}
// ======================SEARCH_MENU==============