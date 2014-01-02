'''
Created on 2013-2-11

@author: Administrator
'''
class FirstClass :
    def setData(self,data):
        self.data = data;
    def display(self):
        print self.data;
        
class SecondClass(FirstClass):
    #override
    def display(self):
        print 'curren value = "%s"' % self.data;
    
z = SecondClass();
z.setData(99);
z.display();
