// listen to messages from service worker (background.ts)
chrome.runtime.onMessage.addListener((msg) => {
    if(msg.action == 'showWarning'){
        popUpWarning();
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