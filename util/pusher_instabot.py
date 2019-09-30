from util.pusher import pusher
from instapy_cli import client
from instapy_cli.cli import InstapyCli
import instagram_private_api
import csv
import os, sys
import random
import time
import requests
import json



class pusher_IG(pusher):
    def __init__(self):
        pusher.__init__(self)
        self.func_task = {
            "T_UPLOAD_PHOTO": {"func": self.task_uploadphoto}
        }
        self.great_words = [
            "不需再對過去耿耿於懷，因為當時的你是另一個自己。",
            "奇蹟也需要一點時間醞釀。",
            "不要讓人因為你的來歷而定位你，你唯一的限制只有你的靈魂。",
            "我何其幸運，擁有這些令我難以割捨的事物。",
            "為了你，我才想變成一個更好的人。",
            "誘人的雙唇來自於善意的言語。",
            "如果你愛一個人，她的一切喜好，她的每一句話，他都會記得清清楚楚的",
            "我們值得更好",
            "先愛自己才能愛人",

        ]
        self.emoji = [
            "🧚‍",
            "🧜‍‍",
            "🏃‍🏃‍‍",
            "💄",
            "💋‍",
            "💍‍",
            "💕‍",
        ]


    ####
    def DataStorage(self, tag):
        def find_a_photo_unsplash(q, skip_files, log_filename):
            idx = 0
            while True:
                idx += 1
                r = requests.get(
                    "https://unsplash.com/napi/search/photos?query={}&xp=&per_page=50&page={}".format(q, idx))
                data = json.loads(r.content.decode("utf-8"))
                valid_photo = []
                valid_photo_likes = []
                for p in data["results"]:
                    filename = (p["alt_description"])
                    likes = (p["likes"])
                    image_url = (p["urls"]["regular"])
                    user = p["user"]
                    user_ig = (user['instagram_username'])
                    if filename in skip_files or filename is None or image_url is None:
                        # print("out:idx: {}:filename: {}".format(idx, filename))
                        continue
                    else:
                        valid_photo.append(p)
                        valid_photo_likes.append(likes)
                if len(valid_photo) > 0:
                    p = valid_photo[valid_photo_likes.index(max(valid_photo_likes))]
                    filename = (p["alt_description"])
                    image_url = (p["urls"]["regular"])
                    user = p["user"]
                    user_ig = (user['instagram_username'])
                    log = "{}\t{}".format(p["alt_description"], p["urls"]["regular"])
                    self.tool_record(text=log,filename=log_filename)
                    return filename, image_url, user_ig
                if idx > 20:
                    raise Exception("too long process")

        if tag == "find_a_photo":return find_a_photo_unsplash

    ###
    def tool_login(self, account: str, password: str) -> InstapyCli:
        raise NotImplementedError

    def tool_exist_photo(self,filename ="upload_log"):
        file_dir = '{}/{}.tsv'.format(self.current_path,filename)
        if not os.path.exists(file_dir):
            return []
        with open(file_dir, newline='') as csvfile:
            # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
            rows = csv.reader(csvfile, delimiter='\t')

            # 以迴圈輸出指定欄位
            filenames = [row[0] for row in rows]
        return filenames

    def tool_record(self,text,filename ="upload_log"):

        with open("{}/{}.tsv".format(self.current_path,filename), "a+") as csvfile:
            write = csvfile.write
            write("{}{}".format(text, "\n"))
    ####

    def task_uploadphoto(self, **kwargs):
        try:
            cli = self.tool_login(account=kwargs['args']['user']['account'],password=kwargs['args']['user']['pws'])
        except Exception as e:
            print("ERROR:tool_login",e)
        DataStorage_method = self.DataStorage(tag=kwargs['args']['DataStorage_tag'])
        filename, image_url, user_ig = DataStorage_method(q=kwargs['args']['keywords'],
                                                          skip_files=self.tool_exist_photo(filename=kwargs['args']['log_filename']),
                                                          log_filename=kwargs['args']['log_filename'])
        print(filename, image_url, user_ig)
        text = '\r\n' + random.choice(self.great_words)
        text += random.choice(self.emoji)
        text += random.choice(self.emoji)
        text += random.choice(self.emoji)
        text += '\r\n #' + " #".join(filename.split(" "))
        text += '\r\n\r\n\r\n '
        text += "\r\n #人像攝影 #女裝 #時尚 #歐美 #女裝鞋 #女裝衫 #女裝裙 #女裝外套 #女裝褲"
        if user_ig is not None:
            text += "\r\n #作者: @{}".format(user_ig)
            text += "\r\n #From: @{}".format(user_ig)
        text += "\r\n #outfitoftheday #lookoftheday #fashion #fashiongram #beautiful #lookbook #outfit #clothess"
        text = text.strip('-')

        try:
            cli.upload(image_url, text)
            del cli
            time.sleep(60)
        except:
            type, message, traceback = sys.exc_info()
            print(type)
            print('function or module？', traceback.tb_frame.f_code.co_name)
            print('file？', traceback.tb_frame.f_code.co_filename)


'''
p = pusher_IG()
p.add_user(account="just.test.pusher", pws="00000000")
p.add_user(account="worth.better.beauty", pws="00000000")

job_detail = {
    "DataStorage_tag": "find_a_photo",
    "user": p.get_user("worth.better.beauty"),
    "keywords":"women",
    "log_filename":"women_shopping"
}
p.add_job(task_name="T_UPLOAD_PHOTO", running_time="1957", args=job_detail)
#p.add_job(task_name="T_UPLOAD_PHOTO", running_time="1100", args=job_detail)
#p.add_job(task_name="T_UPLOAD_PHOTO", running_time="1700", args=job_detail)
while True:
    p.run_controller()
    time.sleep(30)
'''