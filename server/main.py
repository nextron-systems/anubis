from flask import Flask, request, abort, jsonify
import os
import base64
from datetime import datetime

app = Flask(__name__)

@app.route('/pics', methods=['POST'])
def upload_pic():
    # Check if the request has the correct Content-Type
    if request.content_type != 'image/jpeg':
        abort(400, 'Content-Type must be image/jpeg')

    # Read the image data from the request
    image_data = request.data

    if not image_data:
        abort(400, 'No image data received')

    dt_data = datetime.now()
    final_filename = f"{dt_data.year}{dt_data.month}{dt_data.day}{dt_data.hour}{dt_data.minute}{dt_data.second}.jpg"

    # Save the image data to a file
    file_path = os.path.join('.', final_filename)  # Save in the current directory
    with open(file_path, 'wb') as f:
        f.write(image_data)

    # Return a success response
    response = {
        'status': 'success',
        'message': f'File saved as {final_filename}'
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True, port=9502, host="0.0.0.0")