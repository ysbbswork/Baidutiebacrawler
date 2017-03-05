# 贴吧爬虫v1.0
Python3
需要用到BeautifulSoup
## 爬虫功能
这是一只可以爬取百度任意贴吧帖子内容的爬虫。
爬取内容只包含文字信息，不包含图片内容。

### 使用
安装了BeautifulSoup
Python3 IDE 打开并运行
1.输入一个你像爬取的贴吧，(例如：纯文字)
2.输入你要爬取的页面数（例如:1）

## 补充

* 爬取的内容暂时设置为每个贴子的1L，需要爬取每个帖子所有楼层，请自行修改
  getcontent()函数bsobj.find为.findAll，并加入for..in..语句打印内容

* 如需要，可简单修改为爬取某个帖子所有楼层。

* 设置版本v1.0，先给自己挖坑，准备完善补充内容后持续更新：
-[ ] 可选模式
-[ ] 根据输入判断是爬取贴吧还是贴子
-[ ] 可以爬取图片，并作为选择
-[ ] 可以将爬取内容保存到本地
-[ ] 两种保存方式
-[ ] 添加GUI
