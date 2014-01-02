import sys

try :
    s = raw_input('enter something')
except EOFError :
    print 'eof of me'
    sys.exit()
except :
    print ' some error occurred'
   
 
