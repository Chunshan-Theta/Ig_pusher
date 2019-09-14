import os
import requests
import json
import csv
from util.cli import ig_cli
from util.common import count_down
import datetime
import random

def record(text):
    with open("./upload_log.tsv", "a") as csvfile:
        write = csvfile.write
        write("{}{}".format(text, "\n"))

great_words=[
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
emoji=[
    "🧚‍",
    "🧜‍‍",
    "🏃‍🏃‍‍",
    "💄",
    "💋‍",
    "💍‍",
    "💕‍",
]
#username = 'worth.better.beauty'
username = 'just.test.pusher'
password = '00000000'

def exist_photo():
    with open('./upload_log.tsv', newline='') as csvfile:
        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        rows = csv.reader(csvfile, delimiter='\t')

        # 以迴圈輸出指定欄位
        filenames = [row[0] for row in rows]
    return filenames


def find_a_photo(q,skip_files):
    idx = 0
    while True:
        idx += 1
        r = requests.get("https://unsplash.com/napi/search/photos?query=women&xp=&per_page=20&page={}".format(idx))
        data = json.loads(r.content.decode("utf-8"))
        for p in data["results"]:
            filename = (p["alt_description"])
            image_url = (p["urls"]["regular"])
            user = (p["user"])
            if filename in skip_files or filename is None or image_url is None:
                #print("out:idx: {}:filename: {}".format(idx, filename))
                continue
            else:
                record("{}\t{}".format(p["alt_description"], p["urls"]["regular"]))
                return filename, image_url
        if idx > 20:
            raise Exception("too long process")

while True:
    try:
        if int(datetime.datetime.now().hour) in [7,11,17,20]:

            with ig_cli(admin=username, pws=password) as cli:
                if cli.status():
                    filename, image_url= find_a_photo(q="women",skip_files=exist_photo())
                    print(filename, image_url)
                    text = '\r\n' + random.choice(great_words)
                    text += random.choice(emoji)
                    text += random.choice(emoji)
                    text += random.choice(emoji)
                    text += '\r\n #' + " #".join(filename.split(" ")) if type(filename) is str else ""
                    text += "\r\n #人像攝影 #女裝 #時尚 #歐美"
                    text += "\r\n #outfitoftheday #lookoftheday #fashion #fashiongram #beautiful #lookbook #outfit #clothess"
                    text = text.strip('-')
                    try:
                        cli.push_post(image_dir=image_url, text_content=text)
                    except Exception as e:

                        print(e)


                count_down(60 * 60)
        else:
            print(datetime.datetime.now().hour,datetime.datetime.now().minute)
            count_down(10 * 60)
    except Exception as e:
        print("Exception crash:{}: {}".format(type(e),e))
        count_down(30 * 60)

    except SystemError as e:
        print("ClientError crash: {}".format(e))
        count_down(30 * 60)



