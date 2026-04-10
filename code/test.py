import ultralytics
model = ultralytics.YOLO('yolov26m.pt')
results = model.train(data='yolo26.yaml', epochs=3, imgsz=640)