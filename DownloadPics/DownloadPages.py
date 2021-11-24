import requests
import re
import os
import datetime
import time

# 设置保存路径
path = r'/home/victor/Downloads/夏茉GiGi/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
}
start = datetime.datetime.now()


def get_img(urls, savepath):
    i = 1
    for url in urls:
        # 发送请求  获取响应
        response = requests.get(url, headers=headers)
        # 打印网页源代码来看  乱码   重新设置编码解决编码问题
        # 内容正常显示  便于之后提取数据
        response.encoding = 'utf-8'

        # 正则匹配提取想要的数据  得到图片链接和名称
        img_info = re.findall('img src="(.*?)" alt="(.*?)" class="content_img"', response.text)

        for src, name in img_info:
            img_url = src
            img_content = requests.get(img_url, headers=headers).content
            img_name = str(i) + "-" + name + '.jpg'
            with open(savepath + img_name, 'wb') as f:     # 图片保存到本地
                print(f"正在为您下载图片：{img_name}")
                f.write(img_content)
        
        i = i + 1
        time.sleep(1)

def get_pages(url):
    # url = 'http://www.xiannvku.com/pic/show-16157'

    URL = url + '-1.html'
    # 伪装请求头  防止被反爬
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    }

    # 发送请求  获取响应
    response = requests.get(URL, headers=headers)

    page_num = re.findall("<a href='(.*?)'>(.*?)</a>", response.text)

    num = (int)(page_num[-1][1]) + 1

    page_num = re.findall("<a href='(.*?)'>(.*?)</a>", response.text)

    title = re.findall("<title>(.*?)</title>", response.text)

    savepath = path + (str)(title[0]) + '/'

    print("创建文件夹：" + savepath)

    os.mkdir(savepath)

    # 要请求的url列表
    url_list = [
        url + f'-{i}.html' for i in range(1, num)]
    get_img(url_list, savepath)

def main():
    page_link = []
    i = 0

    with open("/home/victor/Downloads/search-1.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件

        page_link = page_link + \
            list((set)(re.findall('<a href="(.*?)-1.html" target="_blank">', data)))

    i = 1
    for page in page_link:
        get_pages(page)
        print(f"正在获取第{i}套图。。。")
        i = i + 1
    
    delta = (datetime.datetime.now() - start).total_seconds()
    print(f"抓取{i}套图用时：{delta}s")


if __name__ == '__main__':
    main()
