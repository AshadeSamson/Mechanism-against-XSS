/// <reference types="chrome"/>

chrome.webRequest.onBeforeRequest.addListener(
    (details) => {
      // Process the URL here before the page loads.
      const url = details.url;
  
      // You can perform any logic here, e.g., send the URL to your Django server.
  
      // Block the request to prevent the page from loading.
      return { cancel: true };
    },
    { urls: ["<all_urls>"] },
    ["blocking"]
  );
  
  // Listen to messages from content scripts if needed.
  chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    // Handle messages from content scripts here.
  });
  
  