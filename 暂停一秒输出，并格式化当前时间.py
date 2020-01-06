import time
for i in range(1):
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
time.sleep(1)#此处可让时间暂停几秒钟
