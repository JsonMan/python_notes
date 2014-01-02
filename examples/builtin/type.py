'''
Created on 2013-9-1

@author: Administrator
'''
def load(file):
    if isinstance(file, type("")):
        file = open(file, "rb")
        
    return file.read()

print len(load("data.txt"))
