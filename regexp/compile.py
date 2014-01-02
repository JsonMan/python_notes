'''
Created on 2013-3-17

@author: Administrator
'''
import re

p = 'thisee';

reg = re.compile(p);
text = 'is this a reg to test this one';

mat = reg.search(text);
if mat :
    print 'match';
    print mat.start(),',',mat.end();
else:
     print 'no match'   
    