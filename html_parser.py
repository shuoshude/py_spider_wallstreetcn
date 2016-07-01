"""
页面解析器，使用bautifulsoup第三方库
"""

from _datetime import datetime
from bs4 import BeautifulSoup
import re


class HtmlParser:
    def _get_new_urls(self, page_url, soup):  # 返回页面中将要保存的新url
        page = "http://wallstreetcn.com/news?status=published&type=news&order=-created_at&limit=30&page="
        new_urls = set()

        '''
        pattern = re.compile(r'http://wallstreetcn\.com/news\?status=published&type=news&order=-'
                             r'created_at&limit=30&page=\d+')
        '''
        if page_url[:-1] == page or page_url[:-2] == page:
        #if pattern.match(page_url):
            links1 = soup.find_all('a', attrs={"class": "button"})
            links2 = soup.find_all('a', class_="title")
            for link in links1:
                new_url = link['href']
                new_urls.add(new_url)
                if new_url == "javascript:void(0)":
                    new_urls.pop()
            for link in links2:
                new_url = link['href']
                new_urls.add(new_url)
        #elif pattern.match(page_url):
        else:
            new_urls = None

        return new_urls

    def _get_new_data(self, page_url, soup):  # 返回需要获取的数据
        page = "http://wallstreetcn.com/news?status=published&type=news&order=-created_at&limit=30&page="
        pattern = re.compile(r'http://wallstreetcn\.com/node/\d+')
        if page_url[:-1] == page or page_url[:-2] == page:
            links1 = soup.find_all('img', class_="lazy img")
            links2 = soup.find_all('a', class_="title")
            img = []
            title = []
            for link in links1:
                img.append(link['data-original'])
            for link in links2:
                title.append(link.get_text().strip())
            new_data = dict(map(lambda x, y: [x, y], title, img))
        elif pattern.match(page_url):
            new_data = {}
            title_node = soup.find('h1', class_="article-title")
            content_node = soup.find('div', class_="article-content")
            author_node = soup.find('span', class_="item author").find("a")
            time_node = soup.find('span', class_="item time")
            comment_count_node = soup.find('span', class_="wscn-cm-counter")
            title = title_node.get_text().strip()
            content = content_node.get_text()
            author = author_node.get_text()
            post_at = datetime.strptime(time_node.get_text(), '%Y年%m月%d日 %H:%M:%S')
            if comment_count_node is not None:
                comment_count = comment_count_node.get_text()
            else:
                comment_count = 0
            new_data['title'] = title
            new_data['author'] = author
            new_data['post_at'] = post_at
            new_data['comment_count'] = comment_count
            new_data['content'] = content
        else:
            new_data = {}
        return new_data
        pass

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data



