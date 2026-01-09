# Bangladeshi Taka Note Detection
## Deployment & Documentation (Phase 5)

This project deploys a trained Bangladeshi Taka Note Detection model using a REST API and Docker.  
The API accepts an image file and returns detected denominations with confidence scores and bounding box coordinates.

---

## Project Folder Structure

taka-note-detector/
│
├── app/
│ ├── main.py # FastAPI REST API with /predict endpoint
│ ├── inference.py # Model loading and inference logic
│
├── weights/
│ └── best.pt # Trained YOLO model weights
│
├── Dockerfile # Docker configuration file
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## How to Build the Docker Image

From the project root directory, run:

docker build -t taka-note-detector .

---

## How to Run the Docker Container

Run the container using:

docker run -p 8000:8000 taka-note-detector

This starts the container and exposes the REST API on port 8000.

---

## How to Use the API Endpoint

Endpoint details:

- Endpoint: /predict  
- HTTP Method: POST  
- Input: Image file (.jpg, .jpeg, .png)  
- Output: JSON response containing detected denominations, confidence scores, and bounding box coordinates  

---

## Code Documentation

- The model is loaded once when the application starts
- Uploaded images are validated before inference
- Bounding box format is [xmin, ymin, xmax, ymax]
- Clear comments are included throughout the code

---

## Submission Contents

The project submission includes:
- API source code
- Dockerfile
- Model weights
- Project documentation

## Google Doc- 
