'''
Created on 2013-9-13

@author: Administrator
'''

def cheeseshop(kind, *args, **kargs):
    print " kind:",kind
    print "args:"
    for item in args:
        print item
    
    print "*" * 40
    keys = sorted(kargs.keys())
    for kw in keys:
        print kw,":",kargs[kw]
    
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")
