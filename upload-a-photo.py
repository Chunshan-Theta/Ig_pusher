from instapy_cli import client
import os
import sys
sys.path.append("./pic_maker")
from pic_maker.pic import pic_obj
pic = pic_obj()
for _ in range(1):
    pic.pop()
    username = 'just.test.pusher'
    password = '00000000'
    image = pic.photo_link
    text = '\r\n' +pic.pic_chinese_label + '\r\n #' + " #".join(pic.pic_eng_label.split( ))

    with client(username, password) as cli:
        cli.upload(image, text)
