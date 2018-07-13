# -*- coding: utf-8 -*-
# 导入俩库，足够了
import requests
from bs4 import BeautifulSoup
import io
from epubtest import BuildEpub

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

# 定义第一个函数， 用来爬取每一章的url和章节名
def get_url(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content,"html.parser")
    # 找到每一章所在的位置，都在'li'这个标签
    text = soup.find('div', {'class': 'mulu'}).find('ul').find_all('li')
    print(u"找到{0}个li标签".format(len(text)))
    urls = []
    titles = []
    page = range(0, len(text))  # 总本
    for i in page:  # 循环第三部的每一章
        try:
            url1 = text[i].find('a').get('href')
            title = text[i].find('a').get_text()
            urls.append(url1)
            titles.append(title)
        except Exception as e:
            print(u"获取text[{0}]时出现异常{1}".format(i,e))
    #返回链接和章节名
    return urls, titles

# 定义第二个函数，用来得到每一章的内容，并存入TXT文件
def get_text(filename,url):
	# 从上一个函数获取链接和章节名
    urls, titles = get_url(url)
    # 文本文件设置为追加模式'a'，避免前面的内容被覆盖
    f = io.open('./{0}.html'.format(filename), 'a',encoding="utf-8")
    for i in range(len(urls)):
        url_tt = url + str(urls[i])  # 每一章完整的链接
        content = requests.get(url_tt).content
        soup = BeautifulSoup(content,"html.parser")
        # 得到一章的内容
        a = u"[\****/[<br /><br />六九中文急速更新 ]\****/]"
        b = u"****[ 请到<br /><br />六九中文阅读最新章节 ]****"
        c = u"逐浪网（）原创小说，转载请注明。"
        text = soup.find('div', {'class': 'yd_text2'}).get_text().replace("\\\\\\","")\
        .replace(u"\u2022","").replace(u"\xa0","<br />").replace(a,"").replace(b,"").replace(c,"")\
        .replace("<br /><br /><br /><br />","<br />")
        # 章节名 + 章节内容
        texts = titles[i] + text
        # 写入txt文件
        f.write(texts)
        print (titles[i]+u"已经写入完成")
    # 循环完之后关闭文件句柄
    f.close()

# 编译成epub文档
def get_epub(filename,url):
    buildEpub = BuildEpub()
    # 从上一个函数获取链接和章节名
    urls, titles = get_url(url)
    # 文本文件设置为追加模式'a'，避免前面的内容被覆盖
    #f = io.open('./{0}.html'.format(filename), 'a',encoding="utf-8")
    for i in range(len(urls)):
        url_tt = url + str(urls[i])  # 每一章完整的链接
        content = requests.get(url_tt).content
        soup = BeautifulSoup(content,"html.parser")
        # 得到一章的内容
        a = u"[\****/[<br /><br />六九中文急速更新 ]\****/]"
        b = u"****[ 请到<br /><br />六九中文阅读最新章节 ]****"
        c = u"逐浪网（）原创小说，转载请注明。"
        text = soup.find('div', {'class': 'yd_text2'}).get_text().replace("\\\\\\","")\
        .replace(u"\u2022","").replace(u"\xa0","<br />").replace(a,"").replace(b,"").replace(c,"")\
        .replace("<br /><br /><br /><br />","<br />")
        # 章节名 + 章节内容
        titleh5 = "<h5>{0}</h5>".format(titles[i])
        texts = titleh5 + text
        buildEpub.addChapter_usestring(texts,titles[i])
        # 写入txt文件
        #f.write(texts)
        print (titles[i]+u"已经生成完成")
    buildEpub.createEpub("output",filename)
    # 循环完之后关闭文件句柄
    #f.close()
# 运行程序
if __name__ == '__main__':
    prourl = "https://www.88dushu.com/xiaoshuo/78/78932/" # 小说主页面，后面还需加上每一章的链接
    profilename = "nihao"
    url = raw_input(u"输入网址:格式形如{0}\n:".format(prourl))
    filename = raw_input(u"输入保存的文件名，格式形如{0}\n:".format(profilename))
    #get_text(filename,url)
    get_epub(filename,url)
