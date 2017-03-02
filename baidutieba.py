import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re



def gethomelink(keyword):
    url = "http://tieba.baidu.com/f?kw="+urllib.parse.quote(keyword)
    return url

def getlinklist(inputlink): #这个函数是获取一个页面上所有帖子的链接
    pages =[] #一个列表
    html = urllib.request.urlopen(inputlink)
    bsobj = BeautifulSoup(html,"html.parser")
    titlelist = bsobj.findAll("a",{"class":"j_th_tit "})
    for title in titlelist:
        pages.append("http://tieba.baidu.com"+title.attrs["href"])
    
    return pages

def same(page1,page2):
    pages1 = []
    pages2 = []
    html1 = urllib.request.urlopen(page1)
    bsobj1 = BeautifulSoup(html1,"html.parser")
    titlelist = bsobj1.findAll("a",{"class":"j_th_tit "})
    for title in titlelist:
        pages1.append(title.get_text())

    html2 = urllib.request.urlopen(page2)
    bsobj2 = BeautifulSoup(html2,"html.parser")
    titlelist2 = bsobj2.findAll("a",{"class":"j_th_tit "})
    for title in titlelist2:
        pages2.append(title.get_text())
    same = 0
    if pages1 == pages2:
        same = 1
    else:
        same = 0
    return same

def getcontent(url):
    html = urllib.request.urlopen(url)
    html = html.read().decode('utf-8')
    title = re.findall(r'title: ".*?"',html)
    title = re.findall(r'".*"',title[0])
    bsobj = BeautifulSoup(html,"html.parser")
    content = bsobj.find("div",{"class":"d_post_content j_d_post_content "})
    print("《",title[0][1:-1],"》")
    print(content.get_text()[8:-1])

def allpagelink(keyword,yourwantnumber):#获取所有页面的所有的帖子连接
    number = int(yourwantnumber)
    wantnumber = number*50
    url = gethomelink(keyword)
    endpageurl=url+"&pn=10000"
    linklist = list()
    pagenumber = 0
    stop = 0
    while stop == 0:
        thispageurl=url+"&pn="+str(pagenumber)
        linklist2 = linklist.extend(getlinklist(thispageurl))
        pagenumber += 50
        wantnumber -= 50
        if same(thispageurl,endpageurl) == 1:
            stop = 1
        elif wantnumber <= 0:
            stop = 1


    return linklist

def main():
    keyword = "尾翼划过的天空"
    wantnumber = 1
    keyword = input("请输入一个正确的贴吧名称：")
    wantnumber = input("你想获取几页内容（1~10000）？")
    wantnumber = int(wantnumber)
    linkset = allpagelink(keyword,wantnumber)
    for link in linkset:
        getcontent(link)
    input()

if __name__=="__main__":
    main()
    
