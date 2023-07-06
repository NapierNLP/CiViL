from ultralytics import YOLO

# Load the model.
model = YOLO('yolov8n-seg.pt')

# Training.
results = model.train(
    data='utensils/data.yaml',
    # data='/home/y-yu/WorkSpace/codebase/CiViL/ultralytics-main/ultralytics/datasets/utensils/data.yaml',
    imgsz=1280,
    epochs=50,
    batch=8,
    name='yolov8n_v8_50e'
)
