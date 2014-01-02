'''
Created on 2013-9-1

@author: Administrator
'''
book = "library2"
pages = 250
scripts = 350
print "the %(book)s book contains \
    more than %(scripts)s scripts" % vars()

print vars()

print locals()