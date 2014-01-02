'''
Created on 2013-9-8

@author: Administrator
'''

def read_file(filename):
    try :
        
        fh = open(filename, "r")
        for line in fh:
            line = line.rstrip("\n")
            print line
        
        fh.close()
    except IOError:
        print "exception occurred"
    
if __name__ == "__main__":
    read_file("data.txt")