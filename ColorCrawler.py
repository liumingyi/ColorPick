"""
从Google的网站 COLOR_URL = "https://material.io/design/color/the-color-system.html#tools-for-picking-colors"
上获取 Material Colors,保存到文件以供使用

Create by Mingyi on 2018/9/7 4:44 PM
"""

import requests
from lxml import html
from Config import file_name, color_list_file, COLOR_URL

# def getHtml():
#     return requests.get(COLOR_URL).text
#
#
# text = getHtml()
#
# with open(file_name, 'w', encoding='utf-8') as f:
#     f.write(text)

with open(file_name, 'r', encoding='utf-8') as f:
    text = f.read()

tree = html.fromstring(text)

sections = tree.xpath("//section[@class='module-module-module col-3']")

print(len(sections))

colors = []

for sec in sections:
    for mo in sec:
        for color in mo:
            style = color.get('style')
            if style is not None:
                color_hex = style.split(' ')[1]
                colors.append(color_hex[:-1])

print(colors)

with open(color_list_file, 'w', encoding='utf-8') as f:
    f.write(",".join(colors))
