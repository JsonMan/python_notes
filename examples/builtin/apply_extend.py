'''
Created on 2013-8-29

@author: Administrator
'''
class Rectangle:
    def __init__(self, color="white", width=10, height=10):
        
        print "create a ", color,self, "sized", width, "x", height
        
class RoundRectangle(Rectangle):
    def __init__(self, **kw):
        apply(Rectangle.__init__, (self,),kw)
  
rect = Rectangle(color="green")

rrect = RoundRectangle(color="blue")     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        