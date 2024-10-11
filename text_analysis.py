# Import necessary libraries
from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import os

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Text Analysis API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }
            h1 {
                color: #333;
            }
            form {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 10px;
                font-weight: bold;
            }
            input[type="file"] {
                margin-bottom: 10px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 4px;
            }
            #result {
                margin-top: 20px;
                padding: 10px;
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            #imagePreview {
                margin-top: 20px;
                max-width: 100%;
                height: auto;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Text Analysis API!</h1>
        <form id="uploadForm" enctype="multipart/form-data">
            <label for="image">Upload an image:</label>
            <input type="file" id="image" name="image" accept="image/*" required>
            <button type="submit">Submit</button>
        </form>
        <img id="imagePreview" src="" alt="Image Preview" style="display:none;">
        <div id="result"></div>

        <script>
            document.getElementById('uploadForm').addEventListener('submit', async function(event) {
                event.preventDefault();
                const formData = new FormData();
                const imageFile = document.getElementById('image').files[0];
                formData.append('image', imageFile);

                // Display the image preview
                const imagePreview = document.getElementById('imagePreview');
                imagePreview.src = URL.createObjectURL(imageFile);
                imagePreview.style.display = 'block';

                try {
                    const response = await fetch('/predict', {
                        method: 'POST',
                        body: formData
                    });
                    const result = await response.json();
                    document.getElementById('result').innerText = result.text || result.error;
                } catch (error) {
                    document.getElementById('result').innerText = 'An error occurred: ' + error.message;
                }
            });
        </script>
    </body>
    </html>
    '''

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Check if the request has a file part
        if 'image' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['image']

        # Check if the file is valid
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file:
            try:
                # Open the image file
                img = Image.open(file.stream)

                # Perform text extraction with pytesseract
                text = pytesseract.image_to_string(img)

                # Return the extracted text
                return jsonify({'text': text}), 200

            except Exception as e:
                # Handle any errors
                return jsonify({'error': str(e)}), 500

    elif request.method == 'GET':
        return jsonify({'message': 'Send a POST request with an image file to extract text.'}), 200

# Run the app
if __name__ == '__main__':
    # Set the host and port for development
    app.run(host='0.0.0.0', port=5000, debug=True)
