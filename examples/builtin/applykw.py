'''
Created on 2013-8-29

@author: Administrator
'''
def say(a=1,b=2):
    print a,b 
    
def haha(**kw):
    apply(say,(),kw)
    
print haha(a=33,b=55)