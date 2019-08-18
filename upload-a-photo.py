from instapy_cli import client
import os
import sys
sys.path.append("./pic_maker")
from pic_maker.pic import pic_obj
from  pic_maker import get_pic_selenium
import time,datetime


while True:
    if int(datetime.datetime.now().hour) == 7 or int(datetime.datetime.now().hour) == 11 or int(datetime.datetime.now().hour) == 20:
        pic = pic_obj(folder="women-fashion")
        username = 'worth.better.beauty'
        password = '00000000'
        with client(username, password) as cli:

            pic.pop()

            image = pic.photo_link
            text = '\r\n' +"我們值得更好" + '\r\n #' + " #".join(pic.pic_eng_label.split( ))+" #努力 #做自己 #愛自己 #開心就好 #魅力"
            text = text.strip('-')
            try:
                cli.upload(image, text)
            except FileNotFoundError as e:
                print(e)
            pic.del_photo()

            if pic.storage_size() < 30:
                print(pic.storage_size())
                get_pic_selenium.main()
        time.sleep(60 * 60)
    else:
        print(datetime.datetime.now().hour)
        time.sleep(60 * 25)

