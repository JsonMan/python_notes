'''
Created on 2013-8-29

@author: Administrator
'''
def dump(value):
    print value,"=>", dir(value)
    
import sys

dump(0)
dump(1.0)
dump(0.1j)
dump([])
dump({})
dump("string")
dump(sys)
dump(dir)