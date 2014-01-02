'''
Created on 2013-9-4

@author: Administrator
'''
import thread
import time,random

def worker():
    for i in range(5):
        time.sleep(random.randint(10,100)/1000.0)
        print thread.get_ident(),"-- task -- ", i , " finished "
        

for i in range(2):
    thread.start_new_thread(worker,())

time.sleep(1)

print "goodbye"

    