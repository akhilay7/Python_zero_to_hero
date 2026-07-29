import time
loc= time.localtime()
#time.sleep(10)
print(loc)

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", loc)
print(formatted_time)
