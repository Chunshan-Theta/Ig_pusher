from os import listdir,path,rename
import random

class pic_obj(object):
    def __init__(self,url: str=None, folder:str="output"):
        self.folder = folder
        self.need_del_photo_handler = False
        self.need_del_photo_dir = None
        self.dir_path = path.dirname(path.realpath(__file__))
        self.pic_label = None
        self.pic_chinese_label = None
        self.pic_eng_label = None
        self.photo_link = url if url is not None else self.random_pic()

    def random_pic(self):
        ## get pics
        pic_name_arr = [i for i in listdir("{}/{}/".format(self.dir_path,self.folder)) if i[-3:] == "png"]

        self.pic_label = random.choice(pic_name_arr)
        self.need_del_photo_dir = [self.dir_path,self.folder,self.pic_label]
        self.pic_chinese_label = self.pic_label.split("_")[0]
        self.pic_eng_label = self.pic_label.split("_")[1][:-4]


        return self.dir_path+"/"+self.folder+"/"+self.pic_label


    def pop(self):
        if self.need_del_photo_handler:
            self.del_photo()
            self.photo_link = self.random_pic()
        self.need_del_photo = self.photo_link.split('/')
        self.need_del_photo_handler = True
        return self.photo_link

    def del_photo(self):
        rename("/".join(self.need_del_photo), self.need_del_photo_dir[0]+"/old/"+self.need_del_photo_dir[2])
        self.need_del_photo_dir = None
        self.need_del_photo_handler =False

'''
obj =pic_obj()
print(obj.pop())
print(obj.pop())
'''