'''
Created on 2013-9-2

@author: Administrator
'''

import copy


a = [1,3,5]
b = copy.copy(a)
print "before","=>"
print a 
print b 

a[0][0] = 0
a[1] = None

print "after =>"
print a 
print b 