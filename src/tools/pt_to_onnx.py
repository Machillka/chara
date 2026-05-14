from ultralytics import YOLO

model = YOLO("../../runs/detect/chara_finetune/weights/best.pt")

model.export(format="onnx", imgsz=640, simplify=True,opset = 17)

