#!/bin/bash

inputArg1=$1
echo ${inputArg1}期中...
echo 生成周刊第${inputArg1}期中...


cd markdown2docx
## 激活环境
python3 -m venv myenv
source myenv/bin/activate

out_name=余小余周刊-第${inputArg1}期

python3 compress_images.py -input_path ../docs/Weekly/No$inputArg1
python3 md2docx.py -input_path ../docs/Weekly/No$inputArg1/No$inputArg1.md -output_name $out_name
echo "生成周刊第{$inputArg1}期[结束]"

echo "更新weekly-list"
node ../H5/scripts/updateWeeklyData.js
deactivate