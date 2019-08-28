from instapy_cli import client
import warnings

import sys

class cliBase(object):
    def __init__(self):
        self.__cli_label = None
        self.__admin = None
        self.__pws = None
        self.username = None

    def status(self) -> bool:
        raise NotImplementedError

    def login(self,admin,pws):
        raise NotImplementedError

class ig_cli(cliBase):
    def __init__(self,admin,pws):
        cliBase.__init__(self)
        self.__cli_label = "ig_cli:{}".format(admin)
        self.__admin = admin
        self.__pws = pws
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        del self
    def status(self) -> bool:
        try:
            with client(self.__admin, self.__pws) as cli:
                # do stuffs with cli
                ig = cli.api()
                me = ig.current_user()
                print("[IG] status: {}".format(me["status"]))
            return 1

        except SystemExit as e:
            print(e)
        except:
            type, message, traceback = sys.exc_info()
            while traceback:
                print('..........')
                print(type)
                print(message)
                print('function or module？', traceback.tb_frame.f_code.co_name)
                print('file？', traceback.tb_frame.f_code.co_filename)
                traceback = traceback.tb_next
    def login(self):
        return client(self.__admin, self.__pws)

    def push_post(self,image_dir: str,text_content:str,cli_obj=None)->bool:
        try:
            if cli_obj is None:
                cli_obj =  self.login()
                cli_obj.upload(image_dir, text_content)
                del cli_obj
            else:
                cli_obj.upload(image_dir, text_content)
            return True
        except:
            type, message, traceback = sys.exc_info()
            print(type)
            print('function or module？', traceback.tb_frame.f_code.co_name)
            print('file？', traceback.tb_frame.f_code.co_filename)


