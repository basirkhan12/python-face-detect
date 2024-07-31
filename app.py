from flask import Flask, request, jsonify
import cv2
import numpy as np
import requests

app = Flask(__name__)

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image_path):
    """
    Detect faces in a local image file.
    :param image_path: Path to the image file
    :return: List of face coordinates (x, y, w, h)
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image could not be loaded.")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        return faces
    except Exception as e:
        print(f"Error detecting faces from file: {e}")
        return []

def detect_faces_from_url(image_url):
    """
    Detect faces in an image from a URL.
    :param image_url: URL of the image
    :return: List of face coordinates (x, y, w, h)
    """
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = np.frombuffer(response.content, np.uint8)
        img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Image data could not be decoded.")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        return faces
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return []
    except Exception as e:
        print(f"Error processing image from URL: {e}")
        return []

@app.route('/detect', methods=['POST'])
def detect():
    """
    Endpoint to detect faces in an image provided via URL.
    """
    if not request.json or 'url' not in request.json:
        return jsonify({'error': 'No URL provided'}), 400

    image_url = request.json['url']
    faces = detect_faces_from_url(image_url)

    if len(faces) == 0:
        return jsonify({'has_face': False, 'faces': []})

    return jsonify({'has_face': True, 'faces': faces.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
