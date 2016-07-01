# -*- coding: utf-8 -*-
"""
爬虫调度端
"""
from spider_wallstreetcn import html_downloader, html_parser, result_io, url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载html页面
        self.parser = html_parser.HtmlParser()  # html页面解析
        self.result = result_io.ResultIO()  # 保存数据

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.result.collect_data(new_data)
            if count == 320:
                break
            count += 1
        #print(len(self.result.other_list))
        #print(len(self.result.title_img_dict))
        self.result.save()
        '''
        for web in self.result.web_list:
            print(web.title)
            print(web.img)
        '''
        self.result.save_db()
        pass

if __name__ == "__main__":
    root_url = "http://wallstreetcn.com/news?status=published&type=news&order=-created_at&limit=30&page=1"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
