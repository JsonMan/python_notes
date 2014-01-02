ab = {
      'swaroop' :'swaroopch@163.com',
      'larry' : 'larry@163.com',
      'Spammer' : 'spammer@hotmail.com'
      
      }

print " swaroop's address is %s " % ab['swaroop']

ab['guido'] = 'guido@python.org'

del ab['larry']

for name, address in ab.items():
    print ' contact %s at %s ' % (name, address)
    
if 'guido' in ab :
    print " guido's address is %s" % ab['guido']

