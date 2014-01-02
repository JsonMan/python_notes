'''
Created on 2013-2-24

@author: Administrator
'''
def change(number,list):
    number = 1;
    list = [1,2,3];
    
def change2(number,list):
    number = 1;
    list[:] = [1,2,3];
    
def change3(number,list):
    number = 1;
    list = list[:]
    list[:] = [5,6,7];
    
number = 5;
list = [3,4];
change(number,list);
print number,',',list;
change2(number,list);
print number,',',list;

change3(number,list);
print number,',',list;