from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import datetime
from os import listdir
import os
import requests,shutil
#local



def download_pic(img_url: str, label: str, save_dir: str="img"):
    global current_dir
    if label is "" or label is None: return
    save_dir = "{}/output/{}/".format(current_dir,save_dir)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        print(save_dir + label + ".png")
        with open(save_dir + label + ".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


current_dir = "/Users/thetawang/code_work/Ig_pusher/instapy-cli/pic_maker"
ChromeDriveDir ="{}/chromedriver".format(current_dir)

#    Open Web browser

def main():
    driver = webdriver.Chrome(ChromeDriveDir)
    #    go to mobile facebook
    search_label = "women-fashion"
    driver.get("https://unsplash.com/search/photos/{}".format(search_label))

    pic_name_arr=[]
    saved=[i[:-4] for i in listdir("{}/output/{}/".format(current_dir, search_label)) if i[-3:] == "png"]
    saved.extend([i[:-4] for i in listdir("{}/output/{}-old/".format(current_dir, search_label)) if i[-3:] == "png"])
    pic_name_arr = [i for i in listdir("{}/output/{}/".format(current_dir, search_label)) if i[-3:] == "png"]

    #
    while len(pic_name_arr) <30:
        print("len(pic_name_arr): {}".format(len(pic_name_arr)))
        pic_dict = {}
        #    enter email & password
        time.sleep(5)
        try:
            elem = driver.find_elements_by_class_name("_2zEKz")
            for idx, pic in enumerate(elem):
                url = pic.get_attribute("srcset")
                label = (pic.get_attribute("alt"))
                if url is None or url is "": continue
                if label in saved: continue
                saved.append(label)
                url=[unit for unit in str(url).split(",") if "1200w" in unit][0]
                pic_dict[label]=url[:url.rfind(" ")].strip(" ")
            driver.execute_script("window.scrollBy(0, 1000);")
        except selenium.common.exceptions.StaleElementReferenceException:
            break

        print(pic_dict)
        for key, value in pic_dict.items():
            download_pic(img_url=value, label=key, save_dir=search_label)
        pic_name_arr = [i for i in listdir("{}/output/{}/".format(current_dir, search_label)) if i[-3:] == "png"]
    driver.close()