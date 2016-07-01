import urllib
import urllib.request


class HtmlDownloader(object):
    def download(self, url):   # 下载html
        if url is None:
            return
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return
        return response

