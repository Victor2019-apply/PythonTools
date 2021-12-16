# 用于获取网页的html
import re
from types import resolve_bases
from urllib import request
import urllib
# 用于解析html
from bs4 import BeautifulSoup
import requests

# 设置保存路径
path = r"/home/victor/Downloads/"
bookname = "姐姐禁恋之歌"

# 得到网页的html
def getHtml(url):
    print("start!")
    # 伪装请求头  防止被反爬
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    }
    req = urllib.request.Request(url=url, headers=headers)  
    req = urllib.request.urlopen(req).read()
    
    # print(req)
    return req

# 解析小说章节页面,获取所有章节的子链接
def jsoupUrl(html):
    # 获取soup对象
    url_xiaoshuo = BeautifulSoup(html)
    # 因为我们要拿取class为box1中的div
    class_dict = {'class': 'box_con'}
    url_xiaoshuo = url_xiaoshuo.find_all('div', attrs=class_dict)
    # 因为分析html中的代码可以发现div的class为box1的有两个,通过上面的代码返回的是一个list格式的结果，所以下面的索引应该是１
    # 我们要获取li中的值，所以find_all，这个方法返回的是一个ｌｉｓｔ集合
    url_xiaoshuo = url_xiaoshuo[1].find_all('dd')
    # print(url_xiaoshuo)
    # 创建一个集合,用于存放每个章节的链接
    url_xs = []
    for item in url_xiaoshuo:
        # 获取每个元素中的href值
        url = 'http://www.bz01.org/' + item.a['href']
        
        # 将值传入url_xs集合中
        url_xs.append(url)
    
    # print(url_xs)
    return url_xs

# 解析小说每个章节的的主要内容
def jsoupXiaoshuo(list):
    title = path + bookname + ".txt"
    with open(title, 'w') as f:
        for item in list:
            print(item)

            # 获取章节内容
            html = getHtml(item)
            html = BeautifulSoup(html)
            class_dict = {'id': 'content'}
            html = html.find_all('div', attrs=class_dict)
            
            # 去掉标签内容
            chapter = str(html[0]).replace("<br/>", "")
            chapter = chapter.replace("</div>", "")
            chapter = chapter.replace("【待续】", "")
            # print(chapter)
            f.write(chapter+'\n')




if __name__ == '__main__':
    html = getHtml("http://www.bz01.org/3_3655/")
    print("step 1")
    url_xs = jsoupUrl(html)
    print("step 2")

    jsoupXiaoshuo(url_xs)

    print("下载完成！")