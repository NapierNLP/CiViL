from ultralytics import YOLO
import cv2
import math


def video_detection(path_x):
    video_capture = path_x
    cap = cv2.VideoCapture(video_capture)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))


model = YOLO('runs/detect/yolov8n_v8_50e5/weights/best.pt')
classNames = ["Blender", "Bowl", "Canopener", "Choppingboard", "Colander", "Cup", "Dinnerfork",
              "Dinnerknife", "Fishslice", "Garlicpress", "Kitchenknife", "Ladle", "Pan", "Peeler", "Saucepan",
              "Spoon", "Teaspoon", "Tongs", "Tray", "Whisk", "Woodenspoon"
              ]

