from ultralytics import YOLO

# Load the model.
model = YOLO('yolov8n.pt')

# Training.
results = model.train(
    data='/home/y-yu/WorkSpace/codebase/CiViL/ultralytics-main/ultralytics/datasets/ingredients/data.yaml',
    # data='/home/y-yu/WorkSpace/codebase/CiViL/ultralytics-main/ultralytics/datasets/utensils/data.yaml',
    imgsz=1280,
    epochs=50,
    batch=8,
    name='yolov8n_v8_50e'
)