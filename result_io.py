import sqlite3
import os


class Web:  # module用于保存文章
    def __init__(self):
        self.title = None
        self.author = None
        self.post_at = None
        self.comment_count = None
        self.content = None
        self.img = None

    def set_value(self, title, author, post_at, comment_count, content, img):
        self.title = title
        self.author = author
        self.post_at = post_at
        self.comment_count = comment_count
        self.content = content
        self.img = img


class ResultIO:
    def __init__(self):
        self.web_list = []
        self.title_img_dict = {}
        self.other_list = []

    def save(self):  # 保存整理数据，用一个Web类型的list保存数据
        for data in self.other_list:
            if data['title'] in self.title_img_dict.keys():
                web = Web()
                web.set_value(data['title'], data['author'], data['post_at'], data['comment_count'],
                              data['content'], self.title_img_dict[data['title']])
            else:
                img = "null"
                web = Web()
                web.set_value(data['title'], data['author'], data['post_at'], data['comment_count'],
                              data['content'], img)
            self.web_list.append(web)
        pass

    def collect_data(self, data):  # 初步获取数据，初步获取数据有两类
        if data is None or not data:
            return
        if 'title' in data.keys():
            self.other_list.append(data)
        else:
            self.title_img_dict.update(data)
        pass

    def save_db(self):  # 写入数据库
        try:
            os.remove("test.db")
        except:
            pass
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()
        cursor.execute('create table if not exists article (title varchar(200) primary key,'
                       ' author varchar(20),'
                       ' post_at datetime,'
                       ' content text,'
                       ' comment_count char,'
                       ' img text)')
        sql = 'insert into article(title, author, post_at, content, comment_count, img) values(?,?,?,?,?,?)'
        for web in self.web_list:
            cursor.execute(sql, (web.title, web.author, web.post_at, web.content, web.comment_count, web.img))
        cursor.close()
        conn.commit()
        conn.close()
        pass
