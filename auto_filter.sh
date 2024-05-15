#!/bin/bash
# 统计## 文本标签类型
# 创建一个空数组，用于存储提取的文本信息
declare -a text_array=()

# 遍历当前目录下所有后缀为 .md 的文件
for file in $(find . -name "*.md")
do
  # 提取文件中以 ## 开头的文本信息
  text=$(grep "^##" $file)

  # 将提取的文本信息添加到数组中
  if [[ -n "$text" ]]; then
    text_array+=("$text")
  fi
done

# 使用 sort 和 uniq 命令对数组中的文本信息进行排序和去重
sorted_text=$(printf "%s\n" "${text_array[@]}" | sort | uniq)

# 打印最终的文本信息
touch "Classify.txt"
# echo "$sorted_text"
echo  "$sorted_text" > "Classify.txt"


