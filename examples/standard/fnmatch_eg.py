'''
Created on 2013-9-3

@author: Administrator
'''
import fnmatch
import os

for file in os.listdir("."):
    if fnmatch.fnmatch(file ,"*.txt"):
        print file