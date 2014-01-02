shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have ', len(shoplist), ' items to purchase'
print ' these items are :'

for item in shoplist :
    print item,

shoplist.append('rice')

print 'my shopping list now is ', shoplist

shoplist.sort()

print '  my sorted shoplist now is ', shoplist

olditem = shoplist[0]
print olditem

del shoplist[0]

print ' I bought the ', olditem

print ' my shopping list now is ',shoplist