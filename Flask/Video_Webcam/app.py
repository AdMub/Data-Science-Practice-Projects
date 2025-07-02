# Import required libraries
from flask import Flask, render_template, Response, redirect, url_for
# install cv2 (pip install opencv-python)
import cv2  # OpenCV for handling the webcam and video
import os
from datetime import datetime

# Initialize the Flask app
app=Flask(__name__)

# Start the webcam (0 = default camera on your laptop)
camera=cv2.VideoCapture(0)

# This function generates video frames continuously
def generate_frames():
    while True:

        # Read a single frame from the webcam
        success,frame=camera.read() # read the camera frame
        
        if not success:
            break  # If there's an error reading the camera, exit loop
        else:
            # Add timestamp on video frame
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cv2.putText(frame, timestamp, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Encode the frame to JPEG format
            ret, buffer=cv2.imencode('.jpg', frame)

            # Convert the encoded image to bytes
            frame=buffer.tobytes()

            # Yield the frame in a specific format required for streaming
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Home route: renders index.html
@app.route('/')
def index():
    return render_template('index.html')

# Video streaming route: returns frames as a multipart HTTP response
@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/snapshot')
def snapshot():
    success, frame = camera.read()
    if success:
        if not os.path.exists("snapshots"):
            os.makedirs("snapshots")
        filename = datetime.now().strftime("snapshots/snapshot_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
    return redirect(url_for('index'))

# Run the app in debug mode
if __name__=="__main__":
    app.run(debug=True)





# This tells the browser, "I’m going to keep sending you images, one after another."

# Each frame is encoded as .jpg, then streamed via yield inside generate_frames().