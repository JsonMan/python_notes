'''
Created on 2013-9-8

@author: Administrator
'''

number = 0;

def main():
    global number
    number = int(input('enter a number'))
    show_number()
    
def show_number():
    print 'the number you entered is', number
   
show_number() 
main()