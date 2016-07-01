# py_spider_wallstreetcn
一个简单的爬虫实现

Python版本为3.5，使用ide pycharm
Spider_wallstreetcn说明：

该爬虫主要由调度段，url管理器，，网页下载器和网页解析器以及数据保存模块组成
文件结构如下：

url管理器：1添加新的url到待爬取集合（判断是否存在，防止重复抓取）
		   2判断是否有待爬取的url
		   3获取待爬取url
		   4从待爬取移动到已爬取
		   		  
网页下载器：urllib库

网页解析器： 使用beautifulsoup第三方库

		   1创建beautifulsoup对象
		   2搜索节点 find_all或find
		   3访问节点名称，属性，文字
		   4返回新的url和需要获取的数据

将一条root_url 传入调度端 
”http://wallstreetcn.com/news?status=published&type=news&order=-created_at&limit=30&page=1“
这里用的是这个url
然后url管理器将这个url加入到待爬取集合（set）, 网页下载器下载页面内容。
经过分析，需要爬取的页面分为两类
一类是30篇文章的页面，可翻页
一类是文章页面
But 作者是21世纪经济报道 的文章页面比较特殊，我的处理是用正则匹配之后，将除了以上两种url统统忽略掉
页面解析器需要分情况解析这两种页面，从第一种页面获取图片的url和文章的title用dict保存，获取30篇文章的url以及下一页的url；从第二中页面获取除了图片url以外的所有文章属性用list保存，不获取新的url
将页面解析器获取到的新url加入到待爬取集合，如此循环一直到抓够300篇
最后将抓到的url-title数据和文章其他属性数据匹配好，写入数据库

