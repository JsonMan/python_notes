'''
Created on 2013-9-4

@author: Administrator
'''
import array

a = array.array("B",range(16))
print a
print repr(a.tostring())

b = array.array("h", range(16))
print b
print repr(b.tostring())