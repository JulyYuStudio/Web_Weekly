import os
import re
from PIL import Image, ImageDraw, ImageFont

def parse_markdown(md_file):
    """解析Markdown文件，提取二级标题和对应内容"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 使用正则表达式匹配##标题和内容
    sections = re.split(r'\n##\s+', content)
    if not sections:
        return []
    
    # 第一个元素是文件开头部分，不是标题内容
    sections = sections[1:] 
    
    results = []
    for section in sections:
        # 分割标题和内容
        parts = section.split('\n', 1)
        if len(parts) < 2:
            continue
            
        title = parts[0].strip()
        body = parts[1].strip()
        results.append({'title': title, 'content': body})
    
    return results

def create_image_card(section, output_dir, md_file):
    """创建图片卡片"""
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 设置图片尺寸和背景
    width = 800
    bg_color = (250, 250, 250)  # 更柔和的背景色
    border_color = (210, 210, 210)  # 更深的边框颜色
    divider_color = (225, 225, 225)  # 更明显的分隔线颜色
    shadow_color = (200, 200, 200)  # 阴影颜色
    accent_color = (0, 120, 215)  # 强调色
    
    # 预计算内容高度
    content_height = 100  # 初始高度包含标题和顶部间距
    for line in section['content'].split('\n'):
        if line.startswith('**') and line.endswith('**'):
            content_height += 35
        elif line.startswith('![') and '](' in line and line.endswith(')'):
            content_height += 220  # 图片高度+间距
        else:
            content_height += 30
    
    # 设置初始高度为预计算高度+底部间距
    height = max(600, content_height + 100)
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # 设置字体
    try:
        title_font = ImageFont.truetype('PingFang.ttc', 38)  # 更大的标题字体
        content_font = ImageFont.truetype('PingFang.ttc', 26)  # 更大的正文字体
        bold_font = ImageFont.truetype('PingFang.ttc', 28)  # 加粗文本字体
    except:
        title_font = ImageFont.load_default()
        content_font = ImageFont.load_default()
        bold_font = ImageFont.load_default()
    
    # 绘制带阴影的边框
    draw.rectangle([(20, 20), (width-20, height-20)], outline=border_color, width=2)
    # 添加阴影效果
    draw.rectangle([(22, 22), (width-18, height-18)], outline=shadow_color, width=1)
    
    # 绘制标题
    title_color = (0, 0, 0)
    draw.text((50, 50), section['title'], font=title_font, fill=title_color)
    # 添加标题装饰线
    draw.line([(50, 95), (150, 95)], fill=accent_color, width=3)
    
    # 绘制标题下划线
    draw.line([(50, 90), (width-50, 90)], fill=divider_color, width=1)
    # 增加标题与内容间距
    y_position = 100  # 初始化y_position为标题底部位置
    y_position += 10
    
    # 绘制内容
    content_color = (80, 80, 80)  # 更深的文字颜色提高可读性
    y_position = 110  # 增加顶部间距
    max_width = width - 100  # 内容区域最大宽度
    line_spacing = 10  # 行间距
    
    for line in section['content'].split('\n'):
        # 处理加粗文本
        if line.startswith('**') and line.endswith('**'):
            bold_text = line[2:-2]
            bold_font = ImageFont.truetype('PingFang.ttc', 28) if 'PingFang.ttc' in title_font.path else ImageFont.load_default()
            # 自动换行处理
            if draw.textlength(bold_text, font=bold_font) > max_width:
                words = bold_text.split(' ')
                current_line = ''
                for word in words:
                    test_line = current_line + word + ' '
                    if draw.textlength(test_line, font=bold_font) <= max_width:
                        current_line = test_line
                    else:
                        if current_line:
                            draw.text((50, y_position), current_line.strip(), font=bold_font, fill=content_color)
                            y_position += 35
                        current_line = word + ' '
                if current_line:
                    draw.text((50, y_position), current_line.strip(), font=bold_font, fill=content_color)
                    y_position += 35
            else:
                draw.text((50, y_position), bold_text, font=bold_font, fill=accent_color)  # 使用强调色
                y_position += 40  # 增加间距
                # 在加粗文本后添加装饰线
                draw.line([(50, y_position), (width-50, y_position)], fill=accent_color, width=2)
                y_position += 20
        # 处理图片链接
        elif line.startswith('![') and '](' in line and line.endswith(')'):
            md_dir = os.path.dirname(os.path.abspath(md_file))
            alt_text = line[2:line.index('](')]
            img_path =  line[line.index('](')+2:-1]
            img_abs_path = md_dir + '/' + img_path
            print(f"资源图片路径: {img_abs_path}")   
            try:
                img = Image.open(img_abs_path)
                img.thumbnail((max_width, 200))
                image.paste(img, (50, y_position))
                y_position += img.height + 20
            except Exception as e:
                print(f"图片加载失败: {img_abs_path}, 错误: {str(e)}")
                draw.text((50, y_position), f"[图片加载失败: {alt_text}]", font=content_font, fill=content_color)
                y_position += 30
        else:
            # 普通文本自动换行处理
            if draw.textlength(line, font=content_font) > max_width:
                words = line.split(' ')
                current_line = ''
                for word in words:
                    test_line = current_line + word + ' '
                    if draw.textlength(test_line, font=content_font) <= max_width:
                        current_line = test_line
                    else:
                        if current_line:
                            draw.text((50, y_position), current_line.strip(), font=content_font, fill=content_color)
                            y_position += 30
                        current_line = word + ' '
                if current_line:
                    draw.text((50, y_position), current_line.strip(), font=content_font, fill=content_color)
                    y_position += 30
            else:
                draw.text((50, y_position), line, font=content_font, fill=content_color)
                y_position += 35  # 增加行距
                # 在普通文本后添加细分隔线
                draw.line([(50, y_position), (width-50, y_position)], fill=divider_color, width=1)
                y_position += 15
        
        # 动态调整图片高度（仅在预计算不足时扩展）
        if y_position > height - 100:
            height = y_position + 100  # 精确调整高度
            new_image = Image.new('RGB', (width, height), bg_color)
            new_image.paste(image, (0, 0))
            image = new_image
            draw = ImageDraw.Draw(image)
    
    # 保存图片
    safe_title = re.sub(r'[\\/*?:"<>|]', '', section['title'])
    output_path = os.path.join(output_dir, f"{safe_title}.png")
    print(f"输出路径: {output_path}")
    image.save(output_path)
    
    return output_path

def main():
    """主函数"""
    # 输入Markdown文件路径
    md_file = input("请输入Markdown文件路径: ")
    if not os.path.exists(md_file):
        print("文件不存在")
        return
    
    # 输出目录
    output_dir = os.path.join("output")
    os.makedirs(output_dir, exist_ok=True)
    
    # 解析Markdown并生成图片
    sections = parse_markdown(md_file)
    for section in sections:
        output_path = create_image_card(section, output_dir, md_file)
        print(f"已生成卡片: {output_path}")

if __name__ == "__main__":
    main()