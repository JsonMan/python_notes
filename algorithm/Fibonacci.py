'''
Created on 2013-1-13

@author: Administrator
'''
def fib1(upper):
    f1,f2 = 0,1;
    while f2<upper:
        print f2,
        f1,f2 = f2,f1+f2

fib1(100)
print;

def fib2(upper):
    f1,f2=0,1;
    result = [];
    while f2<upper:
        result.append(f2);
        f1,f2=f2,f1+f2;
    return result;

ret = fib2(100)
print ret;