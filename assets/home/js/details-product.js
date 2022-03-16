// var slideIndexDetails = 1;
// showSlidersDetails(slideIndexDetails);
//
// //dot-btn => image controls
// function currentSlideDetails(n) {
//     showSlidersDetails(slideIndexDetails = n);
// }
//
// function showSlidersDetails(n) {
//     var i;
//     var slidesDetails = document.getElementsByClassName("carousel-item");
//     var dotsBtnDetails = document.getElementsByClassName("dot-btndetails");
//     if (n > slidesDetails.length) { slideIndexDetails = 1 }
//     if (n < 1) { slideIndexDetails = slidesDetails.length }
//     for (i = 0; i < slidesDetails.length; i++) {
//         slidesDetails[i].style.display = "none";
//     }
//     for (i = 0; i < dotsBtnDetails.length; i++) {
//         dotsBtnDetails[i].classList.remove("slide-activedetails");
//     }
//     slidesDetails[slideIndexDetails - 1].style.display = "block";
//     dotsBtnDetails[slideIndexDetails - 1].classList.add("slide-activedetails");
//
// }
//===========================slider=========================
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


var slideIndex = 1;
showpic(slideIndex);

//dot-btn => image controls
function currentpic(n) {
    showpic(slideIndex = n);
}

function addSlides(n) {
    showpic(slideIndex += n);
}

function showpic(n) {
    var i;
    var dotsBtnDetails = document.getElementsByClassName("dot-btndetails");
    if (n > dotsBtnDetails.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = dotsBtnDetails.length }
    for (i = 0; i < dotsBtnDetails.length; i++) {
        dotsBtnDetails[i].classList.remove("slide-activedetails");
    }
    dotsBtnDetails[slideIndex - 1].classList.add("slide-activedetails");

}


