'''
Created on 2013-9-3

@author: Administrator
'''
import fileinput
import sys

for line in fileinput.input("data.txt"):
    sys.stdout.write("->")
    sys.stdout.write(line)