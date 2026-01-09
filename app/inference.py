from ultralytics import YOLO
import os

# Use a raw string for the path to avoid Windows folder errors
MODEL_PATH = r"E:\taka-note-detection-api\app\models\best.pt"

# Load the model
model = YOLO(MODEL_PATH)

def detect_banknote(image_path):
    # CRITICAL: We set conf to 0.01 (1%) just to get data for your Task 3 screenshots
    results = model.predict(source=image_path, conf=0.01, save=False)
    
    detections = []
    # Index 0 to 8 mapping
    class_names = ["2", "5", "10", "20", "50", "100", "200", "500", "1000"]
    
    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            # Safety check for index
            label = class_names[class_id] if class_id < len(class_names) else str(class_id)
            
            detections.append({
                "denomination": f"{label} Taka",
                "confidence": round(float(box.conf[0]), 4),
                "bbox": [round(x, 2) for x in box.xyxy[0].tolist()]
            })
    
    return {"count": len(detections), "detections": detections}