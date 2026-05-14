from onnxruntime.quantization import quantize_dynamic, QuantType

input_model = "../../runs/detect/chara_finetune/weights/best_sim.onnx"
output_model = "../../runs/detect/chara_finetune/weights/best_int8.onnx"

# 执行动态量化
quantize_dynamic(
    model_input=input_model,
    model_output=output_model,
    weight_type=QuantType.QUInt8  # 将权重转换为 8-bit 整数
)

print("✅ 量化完成！")