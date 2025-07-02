const video = document.getElementById("videoFeed");
const canvas = document.getElementById("snapshotCanvas");
const ctx = canvas.getContext("2d");
const downloadLink = document.getElementById("downloadLink");
const timestamp = document.getElementById("timestamp");

// Update timestamp every second
setInterval(() => {
    const now = new Date();
    timestamp.innerText = "Live Timestamp: " + now.toLocaleString();
}, 1000);

function takeSnapshot() {
    canvas.width = video.clientWidth;
    canvas.height = video.clientHeight;
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const dataURL = canvas.toDataURL("image/jpeg");
    downloadLink.href = dataURL;
}
