name = 'swaroop'

if name.startswith('swa') :
    print 'yes ,the string starts with swa'
    
if 'a' in name :
    print " yes a in in name"
    
if name.find('war') != -1 :
    print 'yes , it contains war'

delimiter = '_*_'

mylist = ['brazil', 'Russia', 'India', 'China']

newlist = delimiter.join(mylist)
print newlist,len(newlist),len(mylist)
print delimiter, mylist
