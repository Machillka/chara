from PIL import Image, ImageDraw, ImageFont
import math

def generate_house_image(digit:str, output_path:str):
    # 1. 设置画布 (640x640)
    size = 640
    # 创建白色背景的图像
    image = Image.new('RGB', (size, size), 'white')
    draw = ImageDraw.Draw(image)

    # 2. 计算房子的几何比例
    # 房子底部宽度设为 1m (对应640像素)
    base_width = size
    # 房子主体高度设为 1m
    base_height = base_width
    # 房子屋顶是等边三角形 (边长1m)，其高度计算公式为：sqrt(3)/2 * 边长
    roof_height = int(base_width * math.sqrt(3) / 2)

    # 3. 计算房子的顶点坐标
    # 房子总高度 (用于计算中心点)
    total_height = base_height + roof_height

    # 为了保证房子在640x640画布中完整显示且居中，我们需要计算缩放比例
    # 如果总高度大于640，就按高度缩放；否则按宽度缩放
    scale = min(size / base_width, size / total_height)
    scale = 0.9 * scale  # 留一点边距

    # 计算缩放后的尺寸
    scaled_base_w = int(base_width * scale)
    scaled_base_h = int(base_height * scale)
    scaled_roof_h = int(roof_height * scale)

    # 计算左上角起始坐标，使房子居中
    start_x = (size - scaled_base_w) // 2
    start_y = (size - scaled_base_h - scaled_roof_h) // 2

    # 定义房子的五个顶点坐标 (左下, 右下, 右上, 顶部, 左上)
    # 顺序：左下 -> 右下 -> 右上 -> 顶部 -> 左上 -> 回到左下
    house_points = [
        (start_x, start_y + scaled_base_h + scaled_roof_h),  # 左下
        (start_x + scaled_base_w, start_y + scaled_base_h + scaled_roof_h),  # 右下
        (start_x + scaled_base_w, start_y + scaled_roof_h),  # 右上
        (start_x + scaled_base_w // 2, start_y),  # 顶部
        (start_x, start_y + scaled_roof_h),  # 左上
        (start_x, start_y + scaled_base_h + scaled_roof_h)  # 闭合路径，回到左下
    ]

    # 4. 绘制房子轮廓 (红色填充)
    draw.polygon(house_points, fill='red', outline='black')

    # 5. 计算中间靶标的位置和大小
    # 靶标大小为 60cm x 60cm，相对于底部1m的比例是 0.6
    target_ratio = 0.6
    target_size = int(scaled_base_w * target_ratio)

    # 靶标位于房子主体矩形的中心
    target_x = start_x + (scaled_base_w - target_size) // 2
    target_y = start_y + scaled_roof_h + (scaled_base_h - target_size) // 2

    # 绘制靶标背景 (白色方块)
    draw.rectangle(
        [target_x, target_y, target_x + target_size, target_y + target_size],
        fill='white',
        outline='black'
    )

    # 6. 在靶标中间绘制数字
    # 设置字体 (你需要指定一个系统中存在的字体路径，或者使用默认字体)
    try:
        # 尝试使用系统字体，如果报错则回退到默认字体
        font = ImageFont.truetype("arial.ttf", int(target_size * 0.6)) # Windows/Mac常见字体
    except IOError:
        font = ImageFont.load_default()

    # 获取文本尺寸以便居中
    text = str(digit)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_w = text_bbox[2] - text_bbox[0]
    text_h = text_bbox[3] - text_bbox[1]

    # 计算文本绘制位置 (在靶标内居中)
    text_x = target_x + (target_size - text_w) // 2
    text_y = target_y + (target_size - text_h) // 2

    # 绘制黑色文字
    draw.text((text_x, text_y), text, fill='black', font=font)

    # 7. 保存图片
    image.save(output_path)
    print(f"图片已生成: {output_path}")

# --- 运行代码 ---
#生成01-99的图片
for i in range(1, 100):
    digit_str = f"{i:02d}"  # 格式化为两位数
    output_file = f"digit_{digit_str}.png"
    generate_house_image(digit_str, output_file)