document.getElementById("screenshot").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            func: captureTweet
        });
    });
});

function captureTweet() {
    const tweet = document.querySelector("article[data-testid='tweet']");
    if (!tweet) {
        alert("No tweet found on this page!");
        return;
    }
    html2canvas(tweet).then(canvas => {
        const link = document.createElement("a");
        const tweetId = window.location.pathname.split("/")[3] || "unknown";
        link.download = `tweet_${tweetId}_${Date.now()}.png`;
        link.href = canvas.toDataURL("image/png");
        link.click();
    }).catch(err => {
        alert("Error capturing screenshot: " + err.message);
    });
}