from datetime import tzinfo, timedelta, datetime, timezone
from pytz import timezone
import os

class pusher(object):

    def __init__(self):
        self.current_path= os.path.dirname(os.path.abspath(__file__))
        self.user = dict()
        self.jobs = list()
        self.func_task = {
            "t1":{ "func": self.task_show_kwargs }
        }

    def add_job(self, task_name, running_time, args):
        temp = {
            "task_name": task_name,
            "running_time": running_time,
            "args": args
        }
        self.jobs.append(temp)

    def add_user(self, account, pws):
        self.user[account] = {
            "account": account,
            "pws": pws
        }

    def get_user(self, account):
        return self.user[account]

    def run_controller(self, jobs=None) -> None:
        jobs = self.jobs if jobs is None else jobs
        for job in jobs:
            if job["task_name"] in self.func_task:
                currnet_time = self.tool_taiwan_time().strftime("%H%M")
                if job["running_time"]==currnet_time:
                    method = self.func_task[job["task_name"]]["func"]
                    method(args=job["args"])
                else:
                    print(job["running_time"],"=/=",currnet_time)
            else:
                print("not find the Task")

    def tool_save(self): #todo
        raise NotImplementedError
    def tool_login(self, account: str, password: str):
        raise NotImplementedError
    def tool_taiwan_time(self,local_timezone_name='Etc/GMT+0',target_timezone_name="Asia/Taipei"):
        #print("In {}".format(local_timezone_name))
        central = timezone(local_timezone_name)
        #print("datetime.now()",datetime.now())
        loc_d =  central.localize(datetime.now())
        bang_d = loc_d.astimezone(timezone(target_timezone_name))
        return bang_d

    def tool_translate(self):# TODO
        raise NotImplementedError
    ####
    def DataStorage(self, tag):
        def Data_1():
            return "Data_sources_1"

        def Data_2():
            return "Data_sources_2"

        if tag == "Data_1":return Data_1
        elif tag == "Data_2":return Data_2

    ####
    def task_show_kwargs(self, **kwargs):
        DataStorage_method = self.DataStorage(kwargs['args']['DataStorage_tag'])
        print(DataStorage_method(),"\t",kwargs)
'''
p = pusher()
p.add_user(account="test_acc", pws="test_pws")

job_detail = {
    "DataStorage_tag": "Data_1",
    "user": p.get_user("test_acc"),
    "keywords":"women"
}
p.add_job(task_name="t1", running_time="09", args=job_detail)
p.run_controller()
'''


