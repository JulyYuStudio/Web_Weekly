#!/bin/bash
# 自动生成周刊的目录

# echo "## Weekly History" > README.md
# done > README.md
find Weekly -name "*.md" -type f | while read file; do
    # 输出文件路径
    echo "* [周刊$(basename "$file" .md)]($file)"
done > README.md
