from os import listdir,path,rename,makedirs
import random

class pic_obj(object):
    def __init__(self,url: str=None, folder:str="output"):
        self.folder_name = folder
        self.folder = "output/"+folder
        self.dir_path = "/Users/thetawang/code_work/Ig_pusher/instapy-cli/pic_maker"
        self.pic_label = None
        self.pic_chinese_label = None
        self.pic_eng_label = None
        self.photo_link = None

    def storage_size(self):
        return len([i for i in listdir("{}/{}/".format(self.dir_path,self.folder)) if i[-3:] == "png"])
    def random_pic(self):
        ## get pics
        pic_name_arr = [i for i in listdir("{}/{}/".format(self.dir_path,self.folder)) if i[-3:] == "png"]

        self.pic_label = random.choice(pic_name_arr)
        self.pic_chinese_label = self.pic_label[:-4]
        self.pic_eng_label = self.pic_label[:-4]

        temp_dir = self.dir_path+"/"+self.folder+"/"+self.pic_label
        if path.isfile(temp_dir):
            return temp_dir
        else:
            self.__init__(self,folder=self.folder_name)
            return self.random_pic()


    def pop(self):
        self.random_pic()
        return self.del_photo()

    def del_photo(self):
        save_dir = "{}/{}/{}-{}".format(self.dir_path, "output", self.folder_name, "old")
        if not path.exists(save_dir):
            makedirs(save_dir)
        old_dir = "{}/{}/{}/{}".format(self.dir_path,"output",self.folder_name,self.pic_label)
        new_dir = "{}/{}/{}-{}/{}".format(self.dir_path,"output",self.folder_name,"old",self.pic_label)
        rename(old_dir, new_dir)
        return new_dir

"""
obj = pic_obj(folder="women-fashion")
print(obj.pop(),obj.storage_size())
print(obj.pop(),obj.storage_size())
obj.del_photo()
"""