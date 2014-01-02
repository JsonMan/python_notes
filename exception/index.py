def kaboom(list, n):
    print list[n];
    
try:
    kaboom([0,1,3],3);
except IndexError:
    print ' index error';
    
print 'the ended';
