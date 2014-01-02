import os
import pycurl
import StringIO
import sys 
import urllib


def setVer(uid):
    c = pycurl.Curl()
    c.setopt(pycurl.CONNECTTIMEOUT, 60)
    c.setopt(pycurl.TIMEOUT, 300)
    c.setopt(pycurl.URL, "http://i.new.weibo.com/user/setversion")
#    -d "token=4757691bbc2b440378539a8e3cff17e5&ver=5&pass=very5&uid=2849678757"
    post_data = {"token":"4757691bbc2b440378539a8e3cff17e5",
                 "ver":"5",
                 "pass":"very5",
                 "uid":uid}
    # Option -d/--data <data>   HTTP POST data
    c.setopt(c.POSTFIELDS,  urllib.urlencode(post_data))

    c.setopt(pycurl.HTTPHEADER, ["Accept:"])
    b = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.MAXREDIRS, 5)
    c.perform()
    print b.getvalue()
    
print "python curl  start"
sys.stdout = open("log.txt", "write")
handler = open("uids.txt")
line = handler.readline()

while line :
    print line
    line = handler.readline()
    
handler.close()
sys.exit()


