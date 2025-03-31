# -*- coding: utf-8 -*-

import re
from docx import Document
from docx.shared import Inches
import text_template as template
import argparse
import os

def match_markdown_images(text):
    # 正则表达式用于匹配 Markdown 中的![]() 图像标记
    pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    matches = pattern.findall(text)
    results = []
    for match in matches:
        # match 是一个元组，第一个元素是中括号内的内容，第二个元素是括号内的内容
        results.append((match[0], match[1]))
    return results

def match_markdown_links(text):
    # 正则表达式用于匹配 Markdown 中的 []() 链接
    pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
    matches = pattern.findall(text)
    results = []
    for match in matches:
        # match 是一个元组，第一个元素是中括号内的内容，第二个元素是括号内的内容
        results.append((match[0], match[1]))
    return results
def is_url(url):
    # 一个相对简单的 URL 正则表达式
    pattern = re.compile(
        r'^(https?|ftp)://'  # 协议部分，支持 http, https, ftp
        r'([A-Za-z0-9.-]+)'  # 域名部分
        r'(:[0-9]+)?'  # 端口部分，可选
        r'(/[A-Za-z0-9_~:/?#[\]@!$&\'()*+,;=.%-]*)?'  # 路径部分，可选
        r'(\?[A-Za-z0-9_~:/?#[\]@!$&\'()*+,;=.%-]*)?'  # 查询部分，可选
        r'(#[A-Za-z0-9_~:/?#[\]@!$&\'()*+,;=.%-]*)?$'  # 片段部分，可选
    )
    return bool(pattern.match(url))

def write_content(text):
    document.add_paragraph(text)

def write_pic(path):
    document.add_picture(path)

def write_end():
    document.add_page_break()
    document.save(output_name + '.docx')

def read_markdown_file(file_path,write,writeEnd):
    try:
        with open(file_path, 'r') as file:
            isArtiles = False
            artContents = ''
            for line_number, line in enumerate(file, start=1):
                # 去除行尾的换行符
                line = line.strip().rstrip('\n')
                if len(line) > 0:
                    ## 标题部分
                    if(line.startswith('## ')):
                        title = line.replace('## ', "").strip()
                        # 是文章标题情况下
                        if(title == '📖好文章'):
                            isArtiles = True
                        else: 
                            if isArtiles: 
                                content = template.templateRedUl.substitute(ul = artContents)
                                write(content.strip())
                            isArtiles = False
                        newline = template.templateRedTitleH2.substitute(h2 = title)
                        ## 写主题TXT
                        write(newline.strip())
                    ## 内容部分
                    else:
                        ## 文章主题内容
                        if isArtiles: 
                            line = line.replace('* ', "").strip()
                            results = match_markdown_links(line.strip())
                            newline = template.templateRedLi.substitute({'li': '📄' + results[0][0],'url':results[0][1]})
                            # write(newline)
                            artContents += newline.strip()
                            # url = template.templateRedUrl.substitute(url = results[0][1])
                            # artContents += url.strip()
                            # print(f"isArtiles ===> {newline} ")
                        else:
                        ## 其他主题内容
                            if(line.startswith('**')):
                                # print(f"title ===> {line} ")
                                title = line.replace('*', "").strip()
                                title = template.templateRedTitleH3.substitute(h3 = title)
                                write(title.strip())
                            elif (line.strip().startswith('* [')):
                                line = line.replace('* ', "").strip()
                                results = match_markdown_links(line)
                                write(results[0][0] + ":" + results[0][1])    
                            elif is_url(line):
                                # print(f"is_url ===> {line} ")
                                url = template.templateRedUrl.substitute(url = line)
                                write(url.strip())
                            elif (line.strip().startswith('![')):
                                imgPath = match_markdown_images(line)
                                write_pic(file_path.rsplit('/', 1)[0]+ "/" + imgPath[0][1])
                            else:
                                newLine = template.templateContent.substitute(content = line.strip())
                                write(newLine.strip())

            writeEnd()        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def md2docx(file_path):
    try:
        document = Document()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # 在这里输入你要读取的文件的路径
    parser = argparse.ArgumentParser(description='一个复杂的命令行参数示例')
    parser.add_argument('-input_path',type=str, help='路径')
    parser.add_argument('-output_name',type=str, help='名称')
    args = parser.parse_args()
    document = Document()
    file_path = args.input_path
    output_name = args.output_name
    read_markdown_file(file_path,write_content,write_end)
    #python3 md2docx.py -input_path ../Weekly/No21/No21.md -output_name 余小余周刊-第21期