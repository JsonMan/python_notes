'''
Created on 2013-9-1

@author: Administrator
'''
def dump(func):
    if callable(func):
        print func , " is callable"
    else:
        print func , " is not callable"
        
class A:
    def method(self, value):
        return value

class B(A):
    def __call__(self, value):
        return value

a = A()
b = B()
dump(0)
dump("string")
dump(callable)
dump(dump)
dump(A)
dump(B)
dump(B.method)

dump(a)
dump(b)
dump(b.method)













