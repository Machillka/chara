import cv2
import numpy as np
import os
from PIL import Image

def get_bbox_from_contours(image_path):
    # 1. 读取图像
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    
    # 2. 预处理：转灰度 -> 二值化
    # 这里假设背景是白色或黑色，物体颜色不同
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    
    # 3. 查找轮廓
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return None

    # 4. 找到最大的轮廓（假设是主要物体）
    c = max(contours, key=cv2.contourArea)
    
    # 5. 获取外接矩形坐标 (x, y, w, h)
    x, y, box_w, box_h = cv2.boundingRect(c)
    
    # 6. 计算归一化高宽
    norm_w = box_w / w
    norm_h = box_h / h
    
    return norm_w, norm_h

def generate_labels(image_dir, label_dir):
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_dir, filename)
            label_path = os.path.join(label_dir, os.path.splitext(filename)[0] + '.txt')
            with Image.open(image_path) as img:
                width, height = img.size
            # 这里假设所有图片的标签都是 class_id=0，center_x=0.5，center_y=0.5，width=1.0，height=1.0
            # 你可以根据实际情况修改这些值
            class_id = 0
            center_x = 0.5
            center_y = 0.5
            bbox_width = 0
            bbox_height = 0
            bbox_width = get_bbox_from_contours(image_path)[0]
            bbox_height = get_bbox_from_contours(image_path)[1]
            with open(label_path, 'w') as f:
                f.write(f"{class_id} {center_x} {center_y} {bbox_width} {bbox_height}\n")
# 使用示例

image_directory = '/home/frankrobot/桌面/yolo/picture/train/val-target'
label_directory = '/home/frankrobot/桌面/yolo/labels/train/val-target'
generate_labels(image_directory, label_directory)