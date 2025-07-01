from ultralytics import YOLO
import cv2
import os

# Load the YOLOv8 model (pretrained or your custom)
model = YOLO("yolov8n.pt")  # or yolov8s.pt, yolov8m.pt...


def execute(img_path, exam, page):
    # Load image
    img = cv2.imread(img_path)

    # Run inference
    results = model(img_path)[0]  # Single image, first result

    subimage_output_dir = os.path.join("manual_figure_extraction", "yolo", exam)
    os.makedirs(subimage_output_dir, exist_ok=True)

    # Loop over detections
    for i, box in enumerate(results.boxes.xyxy):
        filename = page[:-4] + "_" + f"subimg_{i}.png"
        output_path = os.path.join(subimage_output_dir, filename)

        x1, y1, x2, y2 = map(int, box)
        subimg = img[y1:y2, x1:x2]
        cv2.imwrite(output_path, subimg)
