"use strict";
/// <reference types="chrome"/>
chrome.runtime.onInstalled.addListener(() => {
    const conditions = [
        {
            id: 1,
            priority: 1,
            action: {
                type: "block"
            },
            condition: {
                urlFilter: "<all_urls>",
            },
        },
    ];
    chrome.declarativeNetRequest.updateDynamicRules({ removeRuleIds: [1] }, () => {
        chrome.declarativeNetRequest.updateDynamicRules({
            addRules: conditions,
        });
    });
});
chrome.webNavigation.onBeforeNavigate.addListener((details) => {
    const url = details.url;
    const serverEndpoint = "http://127.0.0.1:8000/urlapp/check/";
    const urlMsg = { url };
    fetch(serverEndpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(urlMsg),
    })
        .then((response) => {
        if (!response.ok) {
            throw new Error("Network connection not OK");
        }
        return response.json();
    })
        .then((result) => {
        if (result.is_malicious) {
            const tabId = details.tabId;
            chrome.scripting.executeScript({
                target: { tabId },
                function: Warning,
            });
        }
    })
        .catch((err) => {
        console.log(err);
    });
});
function Warning() {
    const popUp = document.createElement("div");
    popUp.id = 'warning';
    popUp.innerText = 'This URL is suspected to be malicious of a potential XSS vulnerability, Proceed with caution';
    document.body.appendChild(popUp);
    setTimeout(() => {
        popUp.remove();
    }, 10000);
}
