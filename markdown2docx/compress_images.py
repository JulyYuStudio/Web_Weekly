# -*- coding: utf-8 -*-
import os
import sys
import argparse
import tinify
from pathlib import Path


def compress_images(input_path):
    """
    压缩指定目录下的所有图片并覆盖原文件
    """
    with open('/Volumes/JulyKit/AllProjects/Fronts/Weekly/tinify_key', 'r') as f:
        tinify.key = f.read().strip()
    
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                try:
                    source = tinify.from_file(file_path)
                    source.to_file(file_path)
                    print(f"成功压缩: {file_path}")
                except Exception as e:
                    print(f"压缩失败 {file_path}: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description='图片压缩工具')
    parser.add_argument('-input_path', type=str, required=True, help='要压缩的图片目录路径')
    args = parser.parse_args()
    compress_images(args.input_path,)


if __name__ == "__main__":
    main()