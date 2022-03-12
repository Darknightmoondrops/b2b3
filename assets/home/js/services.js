//============================================= sugg page ===============================
function suggbox(n) {
    var filterboxEl = document.getElementsByClassName("sugg-page");
    var blackback = document.getElementsByClassName("sugg-background");
    if (n == 1) {
        filterboxEl[0].classList.remove("sugg-page-off");
        filterboxEl[0].classList.add("sugg-page-on");
        blackback[0].style.display = "block";
    }
    if (n == 2) {
        filterboxEl[0].classList.remove("sugg-page-on");
        filterboxEl[0].classList.add("sugg-page-off");
        blackback[0].style.display = "none";
    }
}
// =========================================== presented services =======================
function prsbox(n) {
    var filterboxEl = document.getElementsByClassName("prs-page");
    var blackback = document.getElementsByClassName("prs-background");
    if (n == 1) {
        filterboxEl[0].classList.remove("prs-page-off");
        filterboxEl[0].classList.add("prs-page-on");
        blackback[0].style.display = "block";
    }
    if (n == 2) {
        filterboxEl[0].classList.remove("prs-page-on");
        filterboxEl[0].classList.add("prs-page-off");
        blackback[0].style.display = "none";
    }
}


//=========================================== slider product 5 ===========================
var pagenumber5 = 1;
slidechenger5(1);


function plusslides5(n) {
    slidechenger5(pagenumber5 += n)
}

function currentslide5(n) {
    slidechenger5(pagenumber5 = n);
}

function slidechenger5(n) {
    var i;
    var page = document.getElementsByClassName("p5-page");
    var number = document.getElementsByClassName("dot5");
    if (n > page.length) { pagenumber5 = 1 }
    if (n < 1) { pagenumber5 = page.length }
    for (i = 0; i < page.length; i++) {
        page[i].style.display = "none";
    }
    for (i = 0; i < number.length; i++) {
        number[i].classList.remove("dot-active");
    }
    page[pagenumber5 - 1].style.display = "block";
    number[pagenumber5 - 1].classList.add("dot-active");
    setInterval(function() {
        showSliders(slideIndex = slideIndex + 1)
    }, 5000);
}
//=========================================== slider product 6 ===========================
var pagenumber6 = 1;
slidechenger6(1);


function plusslides6(n) {
    slidechenger6(pagenumber6 += n)
}

function currentslide6(n) {
    slidechenger6(pagenumber6 = n);
}

function slidechenger6(n) {
    var i;
    var page = document.getElementsByClassName("p6-page");
    var number = document.getElementsByClassName("dot6");
    if (n > page.length) { pagenumber6 = 1 }
    if (n < 1) { pagenumber6 = page.length }
    for (i = 0; i < page.length; i++) {
        page[i].style.display = "none";
    }
    for (i = 0; i < number.length; i++) {
        number[i].classList.remove("dot-active");
    }
    page[pagenumber6 - 1].style.display = "block";
    number[pagenumber6 - 1].classList.add("dot-active");
}

//================================================  colors ==============================================
// ============ 1 =============
function pink() {
    var i;
    var color1 = document.getElementsByClassName("colors");
    for (i = 0; i < color1.length; i++) {
        color1[i].style.display = "none";
    }
    color1[0].style.display = "block";
}
// ============ 2 =============
function blue() {
    var i;
    var color2 = document.getElementsByClassName("colors");
    for (i = 0; i < color2.length; i++) {
        color2[i].style.display = "none";
    }
    color2[1].style.display = "block";
}
// ============ 3 =============
function yellow() {
    var i;
    var color3 = document.getElementsByClassName("colors");
    for (i = 0; i < color3.length; i++) {
        color3[i].style.display = "none";
    }
    color3[2].style.display = "block";
}
// ============ 4 =============
function green() {
    var i;
    var color4 = document.getElementsByClassName("colors");
    for (i = 0; i < color4.length; i++) {
        color4[i].style.display = "none";
    }
    color4[3].style.display = "block";
}
// ============ 5 =============
function purple() {
    var i;
    var color5 = document.getElementsByClassName("colors");
    for (i = 0; i < color5.length; i++) {
        color5[i].style.display = "none";
    }
    color5[4].style.display = "block";
}
// ============ 6 =============
function red() {
    var i;
    var color6 = document.getElementsByClassName("colors");
    for (i = 0; i < color6.length; i++) {
        color6[i].style.display = "none";
    }
    color6[5].style.display = "block";
}


//======================================== change page horiz ==============================================

var pagenumber = 1;
pagechenger(pagenumber);


function pluspage(n) {
    pagechenger(pagenumber += n)
}

function pageslide(n) {
    pagechenger(pagenumber = n);
}

function pagechenger(n) {
    var i;
    var page = document.getElementsByClassName("products-page");

    var number = document.getElementsByClassName("page");
    if (n > page.length) { pagenumber = 1 }
    if (n < 1) { pagenumber = page.length }
    for (i = 0; i < page.length; i++) {
        page[i].style.display = "none";
    }
    for (i = 0; i < number.length; i++) {
        number[i].classList.remove("pageActive");
    }
    page[pagenumber - 1].style.display = "block";
    number[pagenumber - 1].classList.add("pageActive");
}


//============================== change page vert ================
var pagenumber8 = 1;
pagechengers(pagenumber8);


function pluspages(n) {
    pagechengers(pagenumber8 += n)
}

function pageslides(n) {
    pagechengers(pagenumber8 = n);
}

function pagechengers(n) {
    var i;
    var pageVert = document.getElementsByClassName("products-page1");

    var number1 = document.getElementsByClassName("pages");
    if (n > pageVert.length) { pagenumber8 = 1 }
    if (n < 1) { pagenumber8 = pageVert.length }
    for (i = 0; i < pageVert.length; i++) {
        pageVert[i].style.display = "none";
    }
    for (i = 0; i < number1.length; i++) {
        number1[i].classList.remove("pageActive");
    }
    pageVert[pagenumber8 - 1].style.display = "block";
    number1[pagenumber8 - 1].classList.add("pageActive");
}
//=============================price range=======================
const rangeInput = document.querySelectorAll(".multi-range input"),
    priceInput = document.querySelectorAll(".text-violet input"),
    range = document.querySelector(".slider .progress");
let priceGap = 1000;

priceInput.forEach(input => {
    input.addEventListener("input", e => {
        let minPrice = parseInt(priceInput[0].value),
            maxPrice = parseInt(priceInput[1].value);

        if ((maxPrice - minPrice >= priceGap) && maxPrice <= rangeInput[1].max) {
            if (e.target.className === "input-min") {
                rangeInput[0].value = minPrice;
                range.style.left = ((minPrice / rangeInput[0].max) * 100) + "%";
            } else {
                rangeInput[1].value = maxPrice;
                range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
            }
        }
    });
});

rangeInput.forEach(input => {
    input.addEventListener("input", e => {
        let minVal = parseInt(rangeInput[0].value),
            maxVal = parseInt(rangeInput[1].value);

        if ((maxVal - minVal) < priceGap) {
            if (e.target.className === "range-min") {
                rangeInput[0].value = maxVal - priceGap
            } else {
                rangeInput[1].value = minVal + priceGap;
            }
        } else {
            priceInput[0].value = minVal;
            priceInput[1].value = maxVal;
            range.style.left = ((minVal / rangeInput[0].max) * 100) + "%";
            range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
        }
    });
});

//======================================= change mode ======================================
function changepage(n) {
    var mode2 = document.getElementsByClassName("hori-list");
    var mode1 = document.getElementsByClassName("vert-list");
    var bordshow1 = document.getElementsByClassName("show-mode-p1");
    var bordshow2 = document.getElementsByClassName("show-mode-p2");

    if (n == 1) {
        mode1[0].style.display = "block";
        mode2[0].style.display = "none";
        bordshow2[0].classList.remove("show-mode-border");
        bordshow1[0].classList.add("show-mode-border");
    }
    if (n == 2) {
        mode1[0].style.display = "none";
        mode2[0].style.display = "block";
        bordshow1[0].classList.remove("show-mode-border");
        bordshow2[0].classList.add("show-mode-border");
    }
}