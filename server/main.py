from flask import Flask, request, abort
import os
import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/pics', methods=['POST'])
def upload_pic():
    # Check if the request contains the correct Content-Type
    if request.content_type != 'image/jpeg':
        abort(400, 'Content-Type must be image/jpeg')

    # Check if the request contains a file
    if 'file' not in request.files:
        abort(400, 'No file part')

    file = request.files['file']

    # Check if the file has a valid filename
    if file.filename == '':
        abort(400, 'No selected file')

    # Secure the filename
    filename = secure_filename(file.filename)

    # Encode the filename in base64
    base64_filename = base64.urlsafe_b64encode(filename.encode()).decode()

    # Save the file to the root directory
    file_path = os.path.join('/', base64_filename)
    file.save(file_path)

    return f"File saved as {base64_filename}", 201

if __name__ == '__main__':
    app.run(debug=True, port=9502, host="0.0.0.0")