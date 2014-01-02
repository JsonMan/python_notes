'''
Created on 2013-2-23

@author: Administrator
'''
input = open('./data.txt');
for line in input.readlines():
    print line,
input.close();