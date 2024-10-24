Here’s a sample README file for your GitHub repository:

---

# Face Detection API using Flask, OpenCV, and Haar Cascades

This is a simple Flask-based web service that detects faces in an image. The app can process images either from a file or a URL and returns the coordinates of any detected faces using OpenCV's pre-trained Haar Cascade classifier.

## Features

- Detect faces in an image provided via a URL.
- Uses OpenCV's Haar Cascade classifier for face detection.
- REST API for integrating face detection functionality into your applications.

## Requirements

- Python 3.x
- Flask
- OpenCV
- NumPy
- Requests

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/face-detection-api.git
   cd face-detection-api
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have OpenCV installed, including the Haar Cascade XML file (`haarcascade_frontalface_default.xml`). This is automatically downloaded as part of OpenCV's `cv2` module.

## Usage

1. Run the Flask app:

   ```bash
   python app.py
   ```

2. The app will run on `http://127.0.0.1:5000/`.

3. To detect faces in an image, make a POST request to the `/detect` endpoint with a JSON body containing the image URL:

   ```json
   {
     "url": "https://example.com/image.jpg"
   }
   ```

4. Example response:

   ```json
   {
     "has_face": true,
     "faces": [[x, y, width, height], ...]
   }
   ```

   - `has_face`: Indicates if any faces were detected.
   - `faces`: List of bounding boxes for detected faces.

## API Endpoints

- `POST /detect`: Detect faces in an image provided via URL.

  - **Request Body**: JSON with the `url` key containing the image URL.
  - **Response**:
    - `has_face`: `True` if faces are detected, `False` otherwise.
    - `faces`: List of face coordinates `[x, y, width, height]`.

## Example

```bash
curl -X POST http://127.0.0.1:5000/detect -H "Content-Type: application/json" -d '{"url": "https://example.com/image.jpg"}'
```

## Error Handling

- Returns a 400 error if the request is missing a valid image URL.
- Handles invalid or inaccessible image URLs gracefully.

## License

This project is licensed under the MIT License.
