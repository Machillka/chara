import os
from PIL import Image, ImageDraw
import math

def generate_red_house_border(input_folder, output_folder):
    """
    1. 读取文件夹中的图片
    2. 强制调整图片大小为 640x640
    3. 在图片外部绘制红色房子形状的边框（不包含数字）
    """
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 支持的文件格式
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp')

    # 2. 遍历文件夹
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # --- 打开并调整图片大小 ---
                img = Image.open(input_path).convert("RGBA")
                # 强制调整为 640x640
                canvas = Image.new('RGBA', (640, 640), (255, 255, 255, 255))
                draw = ImageDraw.Draw(canvas)
                size = 640
                base_width = size
                base_height = base_width
                roof_height = int(base_width * math.sqrt(3) / 2) 
                total_height = base_height + roof_height
                scale = min(size / base_width, size / total_height)
                scale = 0.9 * scale
                scaled_base_w = int(base_width * scale)
                scaled_base_h = int(base_height * scale)
                scaled_roof_h = int(roof_height * scale)
                start_x = (size - scaled_base_w) // 2
                start_y = (size - scaled_base_h - scaled_roof_h) // 2
                house_points = [
                    (start_x, start_y + scaled_base_h + scaled_roof_h),  # 左下
                    (start_x + scaled_base_w, start_y + scaled_base_h + scaled_roof_h),  # 右下
                    (start_x + scaled_base_w, start_y + scaled_roof_h),  # 右上
                    (start_x + scaled_base_w // 2, start_y),  # 顶部
                    (start_x, start_y + scaled_roof_h),  # 左上
                    (start_x, start_y + scaled_base_h + scaled_roof_h)  # 闭合路径，回到左下
                ]
                draw.polygon(house_points, fill='red', outline='black')
                target_ratio = 0.6
                target_size = int(scaled_base_w * target_ratio)
                img = img.resize((target_size, target_size), Image.Resampling.LANCZOS)
                target_x = start_x + (scaled_base_w - target_size) // 2
                target_y = start_y + scaled_roof_h + (scaled_base_h - target_size) // 2
                draw.rectangle(
                    [target_x, target_y, target_x + target_size, target_y + target_size],
                    fill='white',
                    outline='black'
                )
                canvas.paste(img, (target_x, target_y))
            #     # --- 保存结果 ---
            #     # 转为 RGB 保存为 JPG (如果原图有透明通道且你想保留，请保存为 PNG)
                if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                    rgb_canvas = canvas.convert('PNG')
                    rgb_canvas.save(output_path, quality=95)
                else:
                    canvas.save(output_path)

                print(f"成功处理: {filename}")

            except Exception as e:
                print(f"处理失败 {filename}: {e}")

    print("所有图片处理完成！")

# --- 运行脚本 ---
if __name__ == "__main__":
    # 请确保创建一个名为 'input_images' 的文件夹并放入图片
    INPUT_DIR = "/home/frankrobot/桌面/yolo/chara/picture/train/val-target"  # 替换为你的输入文件夹路径
    OUTPUT_DIR = "/home/frankrobot/桌面/yolo/chara/new_pictures"
    
    generate_red_house_border(INPUT_DIR, OUTPUT_DIR)