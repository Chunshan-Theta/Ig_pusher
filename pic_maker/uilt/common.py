import requests
from bs4 import BeautifulSoup
import shutil
import time
import os

def soup_go_to(url:str):
    r = requests.get(url)
    content = (r.text)

    soup = BeautifulSoup(content, 'html.parser')
    #print(soup.prettify())
    return soup


def download_pic(img_url: str, label: str, save_dir: str="img"):
    save_dir = "./output/{}/".format(save_dir)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        with open(save_dir + label + ".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)





