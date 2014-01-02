'''
Created on 2013-9-1

@author: Administrator
'''
import os
import string
import sys
def replace(file, search, replace):
    back = os.path.splitext(file)[0] + ".bak"
    temp = os.path.splitext(file)[0] + ".tmp"
    
    try :
        os.remove(temp)
    except os.error:
        pass
    
    fi = open(file)
    fo = open(temp,"w+")
    
    print fi.readlines()
    print fi.tell()
    sys.exit
    
    for s in fi.readlines():
        print s
        fo.write(s.replace(search, replace))
        print (s.replace(search, replace))
    
    fi.close()
    fo.close()
    
    try:
        os.remove(back)
    except os.error:
        pass
    
    os.rename(file,back)
    
filename = "data.txt"
replace(filename,"task","replaced")

 
    
    
    