'''
Created on 2013-8-21

@author: Administrator
'''
import re
import math

def getwords(doc):
    splitter = re.compile("\\W*")
    words = [s.lower() for s in splitter.split(doc) if len(s)>2 and len(s) < 20]
    return dict([(w,1) for w in words])

print getwords("this is a text this is a text     this is a text")