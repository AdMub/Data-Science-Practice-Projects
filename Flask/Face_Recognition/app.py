# Import required libraries
from flask import Flask, render_template, Response, redirect, url_for
# install cv2 (pip install opencv-python)
import cv2  # OpenCV for handling the webcam and video
import face_recognition
import numpy as np
import os
from datetime import datetime

# Initialize the Flask app
app=Flask(__name__)

# Start the webcam (0 = default camera on your laptop)
camera=cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
admub_image = face_recognition.load_image_file("AdMub/admub.jpg")
admub_face_encoding = face_recognition.face_encodings(admub_image)[0]

# Load a second sample picture and learn how to recognize it.
messi_image = face_recognition.load_image_file("Messi/messi.jpg")
messi_face_encoding = face_recognition.face_encodings(messi_image)[0]

# Load a third sample picture and learn how to recognize it.
ronaldo_image = face_recognition.load_image_file("Ronaldo/ronaldo.jpg")
ronaldo_face_encoding = face_recognition.face_encodings(ronaldo_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    admub_face_encoding,
    messi_face_encoding,
    ronaldo_face_encoding
]
known_face_names = [
    "Adisa Mubarak",
    "Lionel Messi",
    "Cristiano Ronaldo"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# This function generates video frames continuously
def generate_frames():
    while True:

        # Read a single frame from the webcam
        success,frame=camera.read() # read the camera frame
        
        if not success:
            break  # If there's an error reading the camera, exit loop
        else:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

       # process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

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
    # Read files in snapshot folder
    snapshot_dir = os.path.join('static', 'snapshots')
    if not os.path.exists(snapshot_dir):
        os.makedirs(snapshot_dir)
    files = os.listdir(snapshot_dir)
    return render_template('index.html', snapshots=files)

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
        filename = datetime.now().strftime("static/snapshots/snapshot_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
    return redirect(url_for('index'))

# Run the app in debug mode
if __name__=="__main__":
    app.run(debug=True)





