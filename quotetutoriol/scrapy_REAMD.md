# scrapy

## 安装scrapy框架
	1、 安装wheel库
		pip install wheel
		# wheel库可以安装一些wheel文件，来安装一些库
	2、安装lxml库
		http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
		点击相应文件
		pip install "文件本机路径"
	3、安装Pyopenssl
		https://pypi.python.org/pypi/pyOpenSSL#downloads
		pip install "文件本机路径"
	4、安装Twisted
		http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
		点击相应文件
		pip install "文件本机路径"
		Scrapy的核心框架
	5、安装Pywin32 
		https://pypi.org/project/pywin32/#files
		选择3.7版本的python
	6、Scrapy
		pip install scrapy


# scrapy的基本使用

## 目标站点分析
	1、http://quotes.toscrape.com/
	（官方抓取网站，显示名人名言，标签作者信息）
	2、抓取第一页
		请求第一页的url并得到源代码进行分析
	3、获取内容和下一页链接
		分析源代码，提取首页内容，获取下一页链接等待进一步爬取
	4、翻页爬取
		请求下一页信息，分析内容并请求再下一页链接
	5、保存爬取结果
		将爬取结果保存为特定格式如文本，数据库
