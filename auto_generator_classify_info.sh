#!/bin/bash


    # 遍历文件夹中的所有文件
    for file in $(find . -name "*.md"); do
      # 判断文件是否存在
      if [ -f "$file" ]; then
        # 提取文件中以 ## 开头的文本信息
        category = ""
        while read -r line; do
          if [[ "$line" =~ ^##\  ]]; then
           echo "》》 $line"
            # 获取分类名称
            category=$(echo "$line" | sed 's/^##\ \(.*\)$/\1/')
            # 创建分类文件（如果不存在）
            if [ ! -f "$category.md" ]; then
              touch "$category.md"
            fi
          else
            echo "$line" >> "$category.md"
          fi
        done < "$file"
      fi
    done
