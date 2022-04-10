const button = document.querySelector(".heart-like-button");

button.addEventListener("click", () => {
    if (button.classList.contains("liked")) {
        button.classList.remove("liked");
    } else {
        button.classList.add("liked");
    }
});




//============ copy ============
const shareBtn = document.querySelector('.share-btn');
const shareOptions = document.querySelector('.share-options');
var link = document.getElementsByClassName("link");
link[0].innerHTML = window.location.href;

shareBtn.addEventListener('click', () => {
    shareOptions.classList.toggle('active');
})

function _handleClick(event) {
    event.preventDefault();

    var textarea = document.createElement("textarea");

    textarea.style.position = 'fixed';
    textarea.style.top = '-1px';
    textarea.style.left = '-1px';
    textarea.style.width = '1px';
    textarea.style.height = '1px';
    textarea.style.opacity = 0;
    textarea.style.pointerEvents = 'none';

    textarea.value = window.location.href;

    document.body.appendChild(textarea);

    textarea.select();

    try {
        var copiedURL = document.execCommand('copy');
        if (copiedURL) {
            alert('URL Copied');
        } else {
            console.log('Copy failed');
        }
    } catch (err) {
        console.log('Copy failed', err);
    }

    document.body.removeChild(textarea);
}

document.getElementById('copy').addEventListener('click', _handleClick, false);