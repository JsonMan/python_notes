'''
Created on 2013-9-3

@author: Administrator
'''
import md5

hash = md5.new()
hash.update("one sljdljl")
print repr(hash.digest())