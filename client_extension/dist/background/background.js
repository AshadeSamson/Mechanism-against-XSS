"use strict";
/// <reference types="chrome"/>
chrome.webRequest.onBeforeRequest.addListener((details) => {
    // capture and extract the url address
    const url = details.url;
    const data = { url };
    const serverEndpoint = 'http://127.0.0.1:8000/urlapp/check/';
    const requestObject = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    };
    // send request with url to server
    fetch(serverEndpoint, requestObject)
        .then(res => {
        if (!res.ok) {
            throw new Error('Network connection was not OK');
        }
        return res.json();
    })
        .then(response => {
        // if url is malicious, block page load and popup warning
        if (response.is_malicious) {
            chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
                var _a;
                if ((_a = tabs[0]) === null || _a === void 0 ? void 0 : _a.id) {
                    chrome.tabs.sendMessage(tabs[0].id, { action: 'showWarning' });
                }
            });
        }
        else {
        }
    })
        .catch(err => {
        console.log(err);
    });
}, { urls: ["<all_urls>"] }, ["blocking"]);
// Listen to messages from content scripts if needed.
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
});
