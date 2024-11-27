from flask import Flask, request, Response, render_template
import cv2
import numpy as np

app = Flask(__name__)

# Global variable to store the current frame
current_frame = None

@app.route('/stream', methods=['POST'])
def stream():
    global current_frame
    # Read the incoming image data
    image_data = request.data

    # Convert image data to a NumPy array
    np_arr = np.frombuffer(image_data, np.uint8)
    current_frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    return "Frame received", 200

def generate():
    global current_frame
    while True:
        if current_frame is not None:
            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', current_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    # Stream the frames to the client
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9502, debug=True)
