import requests
import re
import os

page_link = []
i = 0

with open("/home/victor/Downloads/search-1.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件

    page_link = page_link + \
        list((set)(re.findall('<a href="(.*?)-1.html" target="_blank">', data)))


for page in page_link:
    i = i + 1
    print(page)

print(i)
