'''
Created on 2013-3-4

@author: Administrator
'''
class Circle:
    def __init__(self):
        self.radius = 1;
    def area(self):
        return self.radius * self.radius * 3.14;

c = Circle();
c.radius = 3;
print(c.area())

print(Circle.area(c));