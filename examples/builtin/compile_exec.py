'''
Created on 2013-9-1

@author: Administrator
'''
source ="""
print 'sum test'
print 5+6
"""

code = compile(source, "<string>","exec")
print code
exec code