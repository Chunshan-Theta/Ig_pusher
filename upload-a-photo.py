from pic_maker.pic import pic_obj
from  pic_maker import get_pic_selenium
import datetime
import random
from instagram_private_api import ClientError
from util.cli import ig_cli
from util.common import count_down
import sys
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
pic = pic_obj(folder="women-fashion")
username = 'worth.better.beauty'
#username = 'just.test.pusher'
password = '00000000'
while True:
    try:
        if int(datetime.datetime.now().hour) in [7,11,17,20]:

            with ig_cli(admin=username, pws=password) as cli:
                if cli.status():
                    image = pic.pop()
                    text = '\r\n' + random.choice(great_words)
                    text += random.choice(emoji)
                    text += random.choice(emoji)
                    text += random.choice(emoji)
                    text += '\r\n #' + " #".join(pic.pic_eng_label.split( ))
                    text += "\r\n #努力 #自己 #愛自己 #開心就好 #魅力 "
                    text = text.strip('-')
                    try:
                        cli.push_post(image_dir=image, text_content=text)
                    except FileNotFoundError as e:
                        print(e)


                    if pic.storage_size() < 30:
                        print(pic.storage_size())
                        get_pic_selenium.main()

            count_down(60 * 60)
        else:
            print(datetime.datetime.now().hour,datetime.datetime.now().minute)
            count_down(10 * 60)

    except Exception as e:
        print("Exception crash: {}".format(e))
        count_down(30 * 60)

    except ClientError as e:
        print("ClientError crash: {}".format(e))
        count_down(30 * 60)
    except:
        text =sys.exc_info()
        print(text)
