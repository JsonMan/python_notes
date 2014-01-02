'''
Created on 2013-2-25

@author: Administrator
'''
def divide(x,y):
    try:
        result = x/y;
    except ZeroDivisionError:
        print "Whoa ,divide error";
        #raise
    return result;

def calc(x,y):
    return x*(divide(x,y));

try:
    print calc(1,0)
except TypeError:
    print " type error";
except:
    print " error to complete the process";
    

