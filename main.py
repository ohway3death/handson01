import time 

now = time.ctime()
cnvtime = time.strptime(now)

print("hello world")
print(time.strftime("%Y/%m/%d %H:%M", cnvtime))