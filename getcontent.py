import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


def getcontent():
    url = "https://tieba.baidu.com/p/2524140951"
    html = urllib.request.urlopen(url)
    html = html.read().decode('utf-8')
    title = re.findall(r'title: ".*?"',html)
    title = re.findall(r'".*"',title[0])
    print("《",title[0][1:-1],"》")
    bsobj = BeautifulSoup(html,"html.parser")
    content = bsobj.find("div",{"class":"d_post_content j_d_post_content "})
    print(content.get_text()[8:-1])

if __name__=="__main__":
    main()
    
