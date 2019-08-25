from instapy_cli import client
import warnings
from instagram_private_api import ClientError

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
        except ClientError as e:
            warnings.warn(e)
            return 0
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
        except ClientError as e:
            warnings.warn(str(e))
            return False


