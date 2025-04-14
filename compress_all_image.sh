#!/bin/bash


cd markdown2docx
## 激活环境
source myenv/bin/activate
# pip3 install tinify
python3 compress.py -input_path ../docs/Weekly

deactivate