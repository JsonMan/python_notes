'''
Created on 2013-9-1

@author: Administrator
'''
import os
import sys

def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) + args)
    return os.wait()[0]

run("python", "hello.py")
print "ended"