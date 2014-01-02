'''
Created on 2013-2-24

@author: Administrator
'''
def message(text,*line ,**head):
    for key in head.keys():
        print key+":"+head[key];
    print
    print text
    for item in line:
        print item;
        
message('this is text','first line','second line',subject='lunch',to='jack@163.com',sender='one@163.com')