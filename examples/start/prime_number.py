'''
Created on 2013-9-12

@author: Administrator
'''
import sys


def isPrime(n):
    if n<2:
        return False
    
    for m in range(2, (n+1)/2):
        if n % m == 0:
            return False
        
    return True

    
while 1:
    n = input("enter a number, -1 to exit :")
    if isPrime(n):
        print "n is a prime"
        
    if n == -1:
        sys.exit()
