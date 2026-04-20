import ultralytics
from ultralytics import YOLO

# 加载预训练模型
model = YOLO('yolov26m.pt')#一条注释（测试请忽略）

# 训练配置（启用完整的数据增强）
results = model.train(
    data='yolo26.yaml',           # 数据集配置文件
    epochs=100,                    # 训练轮数（原3轮太少，增加到100）
    imgsz=640,                     # 输入图像尺寸
    
    # ========== 数据增强参数（YOLO自带） ==========
    augment=True,                  # 启用数据增强
    
    # 颜色增强
    hsv_h=0.015,                   # 色调增强范围（HSV-Hue）
    hsv_s=0.7,                     # 饱和度增强范围（HSV-Saturation）
    hsv_v=0.4,                     # 明度增强范围（HSV-Value）
    
    # 几何增强
    degrees=15.0,                  # 随机旋转角度（±15度）
    translate=0.2,                 # 随机平移（±20%）
    scale=0.5,                     # 随机缩放（±50%）
    shear=5.0,                     # 随机剪切（±5度）
    perspective=0.0005,            # 随机透视（轻微）
    
    # 翻转增强
    fliplr=0.5,                    # 水平翻转概率（50%）
    flipud=0.0,                    # 垂直翻转概率（0%，因为房子有方向性）
    
    # 组合增强
    mosaic=1.0,                    # 马赛克增强概率（100%）
    mixup=0.2,                     # 混合增强概率（20%）
    copy_paste=0.1,                # 复制粘贴增强（10%）
    
    # 训练优化参数
    batch=16,                      # 批次大小（根据显存调整）
    workers=8,                     # 工作线程数
    device='cuda',                 # 使用GPU（如果没有GPU改为'cpu'）
    optimizer='auto',              # 自动选择优化器
    lr0=0.01,                      # 初始学习率
    lrf=0.01,                      # 最终学习率
    momentum=0.937,                # SGD动量
    weight_decay=0.0005,           # 权重衰减
    
    # 其他设置
    patience=50,                   # 早停轮数
    save=True,                     # 保存模型
    save_period=10,                # 每10轮保存一次
    verbose=True,                  # 显示详细信息
    exist_ok=True,                 # 覆盖已有结果
)

print("训练完成！")