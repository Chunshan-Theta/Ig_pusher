import time
from util.pusher_instapy_cli import pusher_IG
from config import account_just_test_pusher,account_saturdaybeach,account_sundayshopping96,account_worth_better_beauty


p = pusher_IG()
p.add_user(account=account_just_test_pusher[0], pws=account_just_test_pusher[1])
p.add_user(account=account_worth_better_beauty[0], pws=account_worth_better_beauty[1])
p.add_user(account=account_saturdaybeach[0], pws=account_saturdaybeach[1])
p.add_user(account=account_sundayshopping96[0], pws=account_sundayshopping96[1])

job_detail_test_sample = {
    "DataStorage_tag": "find_a_photo",
    "user": p.get_user(account_just_test_pusher[0]),
    "keywords":"clothing-person-woman",
    "log_filename":"women_test_sample"
}
job_detail_women_shopping = {
    "DataStorage_tag": "find_a_photo",
    "user": p.get_user(account_sundayshopping96[0]),
    "keywords":"clothing-person-woman",
    "log_filename":"women_shopping"
}
job_detail_women_bikini = {
    "DataStorage_tag": "find_a_photo",
    "user": p.get_user(account_saturdaybeach[0]),
    "keywords":"swimsuit-bikini-swimwear",
    "log_filename":"women_bikini"
}
p.add_job(task_name="T_UPLOAD_PHOTO", running_time="0700", args=job_detail_women_shopping)
p.add_job(task_name="T_UPLOAD_PHOTO", running_time="1100", args=job_detail_women_shopping)
p.add_job(task_name="T_UPLOAD_PHOTO", running_time="1700", args=job_detail_women_shopping)
p.add_job(task_name="T_UPLOAD_PHOTO", running_time="0700", args=job_detail_women_bikini)
p.add_job(task_name="T_UPLOAD_PHOTO", running_time="1140", args=job_detail_women_bikini)
p.add_job(task_name="T_UPLOAD_PHOTO", running_time="1700", args=job_detail_women_bikini)
#p.add_job(task_name="T_UPLOAD_PHOTO", running_time="0704", args=job_detail_test_sample)

while True:
    p.run_controller()
    time.sleep(60)