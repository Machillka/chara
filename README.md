# Chara

> 项目描述

## 目录说明

- `src/`: 包含训练和推理的核心代码。
  - `yolo_fit_train.py`: 用于训练 YOLO 模型的脚本。
  - `predict.py`: 用于加载训练好的模型并进行推理的脚本。

## 项目说明

需要读取最优模型进行增量训练的话，请修改`yolo_fit_train.py`中的模型读取路径, 存放在`runs/detect/chara_finetune/weights/best.pt`中，同时推理模型默认使用最佳模型

- [ ] 加入校验集，或者实现交叉检验等检验方法
- [ ] 加入模型评估方法，计算mAP等指标

## 其他

默认使用 cuda 进行训练, 如果需要指定请修改`yolo_fit_train.py`中的`device`参数
