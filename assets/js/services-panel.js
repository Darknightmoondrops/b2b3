var panelpage = 1;
panel(1);




function SelectPanel(n) {
    panel(panelpage = n);
}

function panel(n) {
    var i;
    var page = document.getElementsByClassName("services-panel-lengh");
    var StyPanel = document.getElementsByClassName("panels-details");
    if (n > page.length) { panelpage = 1 }
    if (n < 1) { panelpage = page.length }
    for (i = 0; i < page.length; i++) {
        page[i].style.display = "none";
    }
    for (i = 0; i < StyPanel.length; i++) {
        StyPanel[i].classList.remove("border");
    }
    page[panelpage - 1].style.display = "inline-block";
    StyPanel[panelpage - 1].classList.add("border");
}

// =================================== close ======================
function exit(n) {
    console.log(1);
    var boxOne1 = document.getElementsByClassName("question-box-two");
    var shadowBox1 = document.getElementsByClassName("background");
    if (n == 1) {
        boxOne1[0].classList.remove("qu-two-off");
        boxOne1[0].classList.add("qu-two-on");
        shadowBox1[0].style.display = "block";
    }
    if (n == 2) {
        boxOne1[0].classList.remove("qu-two-on");
        boxOne1[0].classList.add("qu-two-off");
        shadowBox1[0].style.display = "none";
    }
}