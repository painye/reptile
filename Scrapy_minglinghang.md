# scrapy--命令行

## 创建项目命令
	scrapy -h
		帮助，显示各种命令的信息
	scrapy startproject myproject
		在当前目录创建项目，"myproject"项目名称
	cd myproject
		进入项目目录
	scrapy genspider [-t template] <name> <domain>
		可以使用定义好的模板来生成spider，也可以创建自己的源码文件


## 运行爬虫命令
	scrapy crawl <spider>

## 运行contract检查：
	scrapy check [-l] <spider>

## 列出当前可用的spider
	scrapy list

## View命令
	scrapy view <url>
	在浏览器中打开给定的URL，并以scrapy spider获取的形式展现。有时候spider获取到的页面和普通用户看到的并不相同。因此该命令可以用来检查spider所获取到的页面，并确认是否正确。

## shell命令
	scrapy shell [url]
	加载指定的URL网页源码，并开启交互模式

## parse命令
	scrapy parse <url> [options]
	获取给定的URL并使用相应的spider分析处理。
	如果再使用 --callback 则使用spider的该方法处理，否则使用parse


