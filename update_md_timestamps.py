#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
更新Weekly目录下Markdown文件的时间戳

根据weekly-list.json文件中的createTime时间戳，
修改docs/Weekly目录下对应Markdown文件的创建时间和修改时间。
"""

import json
import os
import sys
from datetime import datetime


def load_weekly_list(json_path):
    """
    加载weekly-list.json文件
    
    Args:
        json_path: weekly-list.json文件路径
        
    Returns:
        包含周刊信息的列表
    """
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载weekly-list.json文件失败: {e}")
        sys.exit(1)


def update_md_timestamps(weekly_list, weekly_dir):
    """
    更新Markdown文件的时间戳
    
    Args:
        weekly_list: 包含周刊信息的列表
        weekly_dir: Weekly目录路径
        
    Returns:
        更新成功的文件数量
    """
    success_count = 0
    failed_files = []
    
    for item in weekly_list:
        weekly_id = item['id']
        create_time = item['createTime']
        
        # 毫秒级时间戳转换为秒级
        timestamp_seconds = create_time / 1000
        
        # 构建Markdown文件路径
        md_dir = os.path.join(weekly_dir, f"No{weekly_id}")
        md_file = os.path.join(md_dir, f"No{weekly_id}.md")
        
        # 检查文件是否存在
        if not os.path.exists(md_file):
            print(f"警告: 找不到文件 {md_file}")
            failed_files.append(md_file)
            continue
        
        try:
            # 更新文件的访问时间和修改时间
            os.utime(md_file, (timestamp_seconds, timestamp_seconds))
            
            # 格式化时间用于显示
            time_str = datetime.fromtimestamp(timestamp_seconds).strftime('%Y-%m-%d %H:%M:%S')
            print(f"成功: No{weekly_id}.md 时间已更新为 {time_str}")
            success_count += 1
        except Exception as e:
            print(f"错误: 更新 No{weekly_id}.md 时间失败: {e}")
            failed_files.append(md_file)
    
    return success_count, failed_files


def main():
    # 文件路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "weekly-list.json")
    weekly_dir = os.path.join(script_dir, "docs", "Weekly")
    
    # 检查docs/Weekly目录是否存在
    if not os.path.exists(weekly_dir):
        json_path = os.path.join(script_dir, "docs", "weekly-list.json")
        if os.path.exists(json_path):
            weekly_dir = os.path.join(script_dir, "docs", "Weekly")
        else:
            print(f"错误: 找不到weekly-list.json文件")
            sys.exit(1)
    
    # 加载weekly-list.json
    weekly_list = load_weekly_list(json_path)
    
    print(f"开始更新Markdown文件时间戳...")
    print(f"找到 {len(weekly_list)} 个周刊信息")
    
    # 更新时间戳
    success_count, failed_files = update_md_timestamps(weekly_list, weekly_dir)
    
    # 输出结果
    print("\n更新完成!")
    print(f"成功更新: {success_count} 个文件")
    
    if failed_files:
        print(f"失败: {len(failed_files)} 个文件")
        print("失败文件列表:")
        for file in failed_files:
            print(f"  - {file}")


if __name__ == "__main__":
    main()