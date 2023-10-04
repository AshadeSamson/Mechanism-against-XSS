// listen to messages from service worker (background.ts)
chrome.runtime.onMessage.addListener((msg) => {
    if(msg.action == 'showWarning'){
        popUpWarning();
    }
    else{
        validSite();
    }
})


function popUpWarning(){
    const popUp = document.createElement("div");
    popUp.id = 'warning';
    popUp.innerText = 'This URL is suspected to be malicious of a potential XSS vulnerability, Proceed with caution';

    document.body.appendChild(popUp);

    setTimeout(() => {
        popUp.remove();
    }, 10000)
}

function validSite(){
    const valid = document.createElement("div");
    valid.id = 'valid';
    valid.innerText = 'This URL is a Benign URL address';

    document.body.appendChild(valid);

    setTimeout(() => {
        valid.remove();
    }, 10000)
}