'''
Created on 2013-9-8

@author: Administrator
'''
def write_file(filename):
    
    try:
        fh = open(filename, "w")
        fh.write("line 1\n")
        fh.write("line 2\n")
        fh.write("line 3\n")
        fh.write("line 4\n")
        fh.write("line 5\n")
        fh.close()
        
    except IOError:
        print "exception occurred"
    
if __name__ == "__main__":
    write_file("data.txt")