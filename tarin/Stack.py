'''
Created on 2013-3-7

@author: Administrator
'''
class Stack(object):
    def __init__(self):
        self.stack = [];
    def push(self, Object):
        self.stack.append(Object)
    def pop(self):
        return self.stack.pop();
    def length(self):
        return len(self.stack);
    
s = Stack();

s.push([1,2,3]);
print s.length();
print s.pop();
print s.length();
        