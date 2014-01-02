'''
Created on 2013-3-17

@author: Administrator
'''
import re

pattern = 'this';

text = 'this is a string contains this str';
match = re.search(pattern,text);
print match.start(),',',match.end(),text[match.start():match.end()]

for match in re.findall(pattern, text):
    print match;