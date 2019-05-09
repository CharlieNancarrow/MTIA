// add listener for all tabs
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    var safesite = ["https://www.speedtest.net"]

    if (changeInfo === "loading") {
        // logic for checking white list, using tab.url
        

        if (tab.url == safesite) {
            chrome.tabs.update(tabId, { url: 'www.google.com' });
        }
    }
});
