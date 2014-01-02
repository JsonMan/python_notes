def local(x):
    print 'x is ', x
    x = 2
    print ' changed local x to ', x
    
x = 55
local(x)
print ' x is still ', x