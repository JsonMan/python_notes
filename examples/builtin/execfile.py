'''
Created on 2013-9-1

@author: Administrator
'''
import sys

execfile("debug.py")
#sys.exit()

def EXECFILE(filename, locals = None,
             globals = None):
#    print open(filename).read()
#    sys.exit()
    exec compile(open(filename).read(),\
          filename, "exec") in globals, locals
          
EXECFILE("debug.py");