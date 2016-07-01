"""
url管理器
"""


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 待爬取url
        self.old_urls = set()  # 已爬取url

    def add_new_url(self, url):  # 添加一条url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        pass

    def add_new_urls(self, urls):  # 添加多条url
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
        pass

    def has_new_url(self):  # 判断是否存在待爬取url
        return len(self.new_urls) != 0
        pass

    def get_new_url(self):  # 获取一条待爬取url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
