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
		
## 用命令行创建Scrapy项目
	1、在命令行中定位到自己想要创建项目的路径中
	2、	scrapy stratproject "新的项目"
		有两个文件夹，一个同名文件夹，一个scrapy.cfg（配置文件）
	3、进入刚才创建的项目
		cd "项目"
		scrapy genspider "spider文件名" "爬取的域名"


## scrapy主要组件
	1、爬虫引擎（engine）
		控制各个组件之间的数据流，当某些操作触发事件后都是通过engine处理
	2、调度器
		调度接受来自engine的请求，并将请求放入队列中，并通过事件返回给engine
	3、下载器
		通过engine请求下载网络数据并将结果返回给engine
	4、spider
		Spider发出请求，并处理engine返回给他下载器相应数据，以items和柜子内的数据请求(urls)返回给engine
	5、管道数目（item pipline)
		负责处理engine返回给spider解析后的数据，并将数据持久化，例如将数据存入数据库或文件
	6、下载中间件
		engine和下载器的交互组件，以钩子（插件）的形式存在，可以代替接受请求、处理数据的下载以及将结果响应给engine
	7、spider中间件
		engine和spider之间的交互组件，可以代替处理response以及返回给engine items以及新的请求集


## scrapy工作流程
	1、引擎打开一个网站(open adomain)，找到处理该网站的Spider并向该spider请求第一个要抓取的URL
	2、引擎从spider中获取到第一个要抓取的URL并在调度器(Scheduler)以Request调度
	3、引擎向调度器请求一个要爬取的URL
	4、调度器返回下一个要抓取的URL给引擎，引擎将URL通过下载中间件(request方向)转发给下载器(Downloader)
	5、一旦页面下载完毕，下载器生成一个该页面的Response，并将其通过下载中间件(response方向)发送给引擎
	6、引擎从下载器中接收到response并通过spider中间件发送给spider处理
	7、spider处理response并返回爬取到的item pipeline，将（spider返回的）request给调度器
	8、引擎将（spider返回的）爬取的item给item pipeline，将（spider返回的)request给调度器
	9、从第二部重复到调度器中没有更多的request，引擎关闭该网站。


## scrapy框架目录
	└─project_dir
	  │  scrapy.cfg
	  │
	  └─project_name
	      │  items.py
	      │  middlewares.py
	      │  pipelines.py
	      │  settings.py
	      │  __init__.py
	      │
	      ├─spiders
	      │  │  __init__.py
	      │  │
	      │  └─__pycache__
	      └─__pycache__

	items.py: 定义爬虫的数据模型，类似于实体类
	middlewarse.py: 爬虫中间件，负责调度
	piplines.py：管理文件，负责对spider返回数据的处理
	spiders: 目录 负责存放继承自scrapy的爬虫类
	scrapy.cfg.scrapy : 基础配置
	init: 初始化文件
	setting.py: 负责对整个爬虫的配置


# scrapy交互模式
	scrapy shell 网址


# 我遇到的错误

## 在命令行模式下执行scrapy crawl 项目名 命令时注意
	1、确保spiders文件夹下要包含spider.py
	2、在项目文件夹内执行命令
		在scrapy.cfg所在文件夹里执行命令


## 在命令行中遇到的错误
		from items import QuoteItem
		ModuleNotFoundError: No module named 'items'
	解决办法：加上上一目录的文件夹
		from quotetutoriol.items import QuoteItem
	错误原因：
		应该是项目文件夹（父文件夹）和spiders（子文件夹）其实里面都有空白的文件__init__.py

		
