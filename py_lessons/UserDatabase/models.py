import os

from ultralytics import YOLO

main_path = os.getcwd()

yolov9c_file = os.path.join(main_path, 'models', 'yolov9c.pt')

yolov9 = YOLO(yolov9c_file)
