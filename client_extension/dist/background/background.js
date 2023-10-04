"use strict";
/// <reference types="chrome"/>
chrome.runtime.onInstalled.addListener(() => {
});
chrome.declarativeNetRequest.onRuleMatchedDebug.addListener((details) => {
    if (details.request.url) {
        console.log(details.request.url);
        const url = details.request.url;
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
                console.log(result);
                const tabId = details.request.tabId;
                chrome.tabs.sendMessage(tabId, { action: "showWarning" });
            }
            else {
                console.log(result);
                const tabId = details.request.tabId;
                console.log(tabId);
                chrome.tabs.sendMessage(tabId, { action: "validateSite" });
            }
        })
            .catch((err) => {
            console.log(err);
        });
    }
});
