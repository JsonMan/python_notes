'''
Created on 2013-3-4

@author: Administrator
'''
class Circle:
    """ circle class"""
    all_circles = []
    pi = 3.14
    def __init__(self,r=1):
        self.radius = r;
        self.__class__.all_circles.append(self);
        
    def area(self):
        """ determine the area"""
        return self.__class__.pi * self.radius * self.radius;
    
    @staticmethod
    def total_area():
        total = 0;
        for c in Circle.all_circles:
            total += c.area();
        return total;
    
c1 = Circle(1);
c2 = Circle(2);
print Circle.total_area();
print Circle.__doc__;

    