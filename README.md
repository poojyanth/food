# Text Analysis API

Welcome to the Text Analysis API! This API allows you to upload an image and extract text from it using OCR (Optical Character Recognition) with the help of Tesseract.

## Features

- Upload an image file
- Extract text from the uploaded image
- Display the extracted text and the uploaded image

## Requirements

- Python 3.x
- Flask
- Pillow
- pytesseract

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/text-analysis-api.git
    cd text-analysis-api
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:

    ```sh
    pip install Flask Pillow pytesseract
    ```

4. Install Tesseract OCR:

    - **Windows**: Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
    - **macOS**: Use Homebrew to install Tesseract:

        ```sh
        brew install tesseract
        ```

    - **Linux**: Use your package manager to install Tesseract. For example, on Ubuntu:

        ```sh
        sudo apt-get install tesseract-ocr
        ```

## Usage

1. Run the Flask application:

    ```sh
    flask run
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. You will see a form to upload an image. Select an image file and click "Submit".

4. The extracted text from the image will be displayed below the form along with the uploaded image.

## API Endpoints

### `GET /`

Displays the home page with the upload form.

### `POST /predict`

Accepts an image file and returns the extracted text.

#### Request

- `Content-Type: multipart/form-data`
- Form data:
  - `image`: The image file to be uploaded.

#### Response

- `200 OK`: Returns the extracted text in JSON format.
- `400 Bad Request`: If no file is provided or the file is invalid.
- `500 Internal Server Error`: If an error occurs during text extraction.

## Example

Here's an example of how to use the API with `curl`:

```sh
curl -X POST -F "image=@path/to/your/image.png" http://127.0.0.1:5000/predict