'''
Created on 2013-9-3

@author: Administrator
'''
import StringIO
message = "that man is reading"

file = StringIO.StringIO(message)
print file.read()