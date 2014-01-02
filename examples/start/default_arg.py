'''
Created on 2013-9-12

@author: Administrator
'''

def f(a, L=None):
    if L == None:
        L = []
    
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)
