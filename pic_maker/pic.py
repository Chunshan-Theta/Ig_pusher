from os import listdir,path,rename,makedirs
import random

class pic_obj(object):
    def __init__(self,url: str=None, folder:str="output"):
        self.folder_name = folder
        self.folder = "output/"+folder
        self.need_del_photo_handler = False
        self.need_del_photo_dir = None
        self.dir_path = "/Users/thetawang/code_work/Ig_pusher/instapy-cli/pic_maker"
        self.pic_label = None
        self.pic_chinese_label = None
        self.pic_eng_label = None
        self.photo_link = url if url is not None else self.random_pic()
    def storage_size(self):
        return len([i for i in listdir("{}/{}/".format(self.dir_path,self.folder)) if i[-3:] == "png"])
    def random_pic(self):
        ## get pics
        pic_name_arr = [i for i in listdir("{}/{}/".format(self.dir_path,self.folder)) if i[-3:] == "png"]

        self.pic_label = random.choice(pic_name_arr)
        self.need_del_photo_dir = [self.dir_path,self.folder,self.pic_label]
        self.pic_chinese_label = self.pic_label[:-4]
        self.pic_eng_label = self.pic_label[:-4]


        return self.dir_path+"/"+self.folder+"/"+self.pic_label


    def pop(self):
        if self.need_del_photo_handler:
            self.del_photo()
            self.photo_link = self.random_pic()
        self.need_del_photo = self.photo_link.split('/')
        self.need_del_photo_handler = True
        return self.photo_link

    def del_photo(self):
        save_dir = "{}/{}/{}-{}".format(self.need_del_photo_dir[0], "output", self.folder_name, "old")
        if not path.exists(save_dir):
            makedirs(save_dir)
        dir = "{}/{}/{}-{}/{}".format(self.need_del_photo_dir[0],"output",self.folder_name,"old",self.need_del_photo_dir[2])
        rename("/".join(self.need_del_photo), dir)
        self.need_del_photo_dir = None
        self.need_del_photo_handler =False

"""
obj = pic_obj(folder="women-fashion")
print(obj.pop(),obj.storage_size())
print(obj.pop(),obj.storage_size())
obj.del_photo()
"""