import onnx
model = onnx.load("../../runs/detect/chara_finetune/weights/best.onnx")
print(model.graph.input)  # 查看输入
print(model.graph.output) # 查看输出