from flask import Flask, request, abort, jsonify
import os
import base64

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

    # Generate a base64-encoded filename
    base64_filename = base64.urlsafe_b64encode(os.urandom(12)).decode('utf-8') + '.jpg'

    # Save the image data to a file
    file_path = os.path.join('.', base64_filename)  # Save in the current directory
    with open(file_path, 'wb') as f:
        f.write(image_data)

    # Return a success response
    response = {
        'status': 'success',
        'message': f'File saved as {base64_filename}'
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True, port=9502, host="0.0.0.0")