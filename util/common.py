import time
def count_down(target):

    for _ in range(10):
        if target < 0:
            print("go ahead           ")
            return
        print("                             ", end="\r")
        print(" Waiting: {}".format(target), end="\r")
        time.sleep(1)
        target-=1


    return count_down(target)
