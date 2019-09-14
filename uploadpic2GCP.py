import paramiko
from util.config import hostname, password,username,port
from pic_maker import get_pic_selenium
from os import listdir, getcwd
from pic_maker.pic import pic_obj
import random

def catch_pic_in_folder(client:paramiko.SSHClient,link: str):


    command = "ls {}".format(link)
    stdin, stdout, stderr = client.exec_command(command)
    picarr = [p for p in stdout.read().decode("utf-8").split("\n") if p is not '']
    return {
        "stdin": stdin,
        "stdout": stdout,
        "stderr": stderr,
        "picarr": picarr,
    }
def scp(localpath,remotepath):
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    #sftp.get(source, dest)
    sftp.put(localpath=localpath,remotepath=remotepath)
    t.close()

def scp_dir(localpath="pic_maker/output/women-fashion-old",remotepath ="/home/f106524018/Ig_pusher/pic_maker/output/women-fashion"):
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    pic = pic_obj(folder="women-fashion")
    pic_size = pic.storage_size()

    for _ in range(pic_size):
        pic_dir = pic.pop()
        Pic_label = pic.pic_label
        print("{}/{}".format(remotepath, Pic_label))
        sftp.put(localpath="{}/{}".format(localpath,Pic_label),remotepath="{}/{}".format(remotepath,Pic_label))

    t.close()




try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    client.connect(hostname, port=port, username=username, password=password)

    #
    result = catch_pic_in_folder(client, "/home/f106524018/Ig_pusher/pic_maker/output/women-fashion")
    current_pic = (result["picarr"])
    print(len(current_pic))

    #
    result = catch_pic_in_folder(client, "/home/f106524018/Ig_pusher/pic_maker/output/women-fashion-old")
    old_pic =(result["picarr"])
    print(len(old_pic))

    while len(current_pic)<90 :

        get_pic_selenium.main(folder_label = "women-fashion",search_label="{}-{}".format(random.choice(["lady",
                                                                                                        "girl",
                                                                                                        "women",
                                                                                                        "female"]),
                                                                                         random.choice(["dress",
                                                                                                        "skirt",
                                                                                                        "clothing",
                                                                                                        "apparel"])
                                                                                         ))
        scp_dir()
        result = catch_pic_in_folder(client, "/home/f106524018/Ig_pusher/pic_maker/output/women-fashion")
        current_pic = (result["picarr"])
        print(len(current_pic))

    #
    result = catch_pic_in_folder(client, "/home/f106524018/Ig_pusher/pic_maker/output/women-fashion")
    current_pic = (result["picarr"])
    print(len(current_pic))

except EOFError as e:
    print("net broken")
finally:
    client.close()

