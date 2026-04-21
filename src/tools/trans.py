# 生成一段代码，获取特定目录下的图片，并生成对应的标签文件到特定的目录下，标签文件的格式为class_id center_x center_y width height
# #class_id：类别 ID（从 0 开始）
# center_x, center_y：边界框中心点的归一化坐标（0-1）
# width, height：边界框的归一化宽度和高度（0-1）
import os
from PIL import Image

graphic_normalized_size = {
    "basic_info": {
        "image_width_px": 640,  # 图片原始宽度（像素）
        "image_height_px": 640,  # 图片原始高度（像素）
        "normalization_rule": "归一化值 = 图形实际像素尺寸 / 图片总像素尺寸（宽÷640，高÷640）",
    },
    "graphics": [
        {
            "序号": 1,
            "图形内容": "机枪兵",
            "归一化宽度": 0.5453,
            "归一化高度": 0.7016,
            "说明": "旋翼展开占比宽，机身紧凑",
        },
        {
            "序号": 2,
            "图形内容": "直升机",
            "归一化宽度": 0.7484,
            "归一化高度": 0.6234,
            "说明": "炮管倾斜，整体纵向占比适中",
        },
    ],
}


def generate_labels(image_dir, label_dir):
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_dir, filename)
            label_path = os.path.join(label_dir, os.path.splitext(filename)[0] + ".txt")
            with Image.open(image_path) as img:
                width, height = img.size
            # 这里假设所有图片的标签都是 class_id=0，center_x=0.5，center_y=0.5，width=1.0，height=1.0
            # 你可以根据实际情况修改这些值
            class_id = 0
            center_x = 0.5
            center_y = 0.5
            bbox_width = 0
            bbox_height = 0
            for graphic in graphic_normalized_size["graphics"]:
                if graphic["图形内容"] in filename:
                    bbox_width = graphic["归一化宽度"]
                    bbox_height = graphic["归一化高度"]
                    break
            with open(label_path, "w") as f:
                f.write(
                    f"{class_id} {center_x} {center_y} {bbox_width} {bbox_height}\n"
                )


# # 使用示例
# image_directory = "C:/Users/86138/Desktop/yolo/picture/train/val-target"
# label_directory = "C:/Users/86138/Desktop/yolo/labels/val-target"
# generate_labels(image_directory, label_directory)
