import time
from util.pusher_instapy_cli import pusher_IG



p = pusher_IG()
p.add_user(account="just.test.pusher", pws="00000000")
p.add_user(account="worth.better.beauty", pws="00000000")
p.add_user(account="saturdaybeach", pws="00000000")
p.add_user(account="sundayshopping96", pws="00000000")

job_detail_test_sample = {
    "DataStorage_tag": "find_a_photo",
    "user": p.get_user("just.test.pusher"),
    "keywords":"clothing-person-woman",
    "log_filename":"women_test_sample"
}
job_detail_women_shopping = {
    "DataStorage_tag": "find_a_photo",
    "user": p.get_user("sundayshopping96"),
    "keywords":"clothing-person-woman",
    "log_filename":"women_shopping"
}
job_detail_women_bikini = {
    "DataStorage_tag": "find_a_photo",
    "user": p.get_user("saturdaybeach"),
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