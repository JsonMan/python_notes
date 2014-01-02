class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
        
try :
    s = raw_input('enter something')
    if len(s) < 3 :
        raise ShortInputException(len(s), 3)
    else :
        print 'no exception'
except EOFError :
    print ' eof on me'
except ShortInputException, x:
    print 'ShortInputException occurred' , x.length,x.atleast
