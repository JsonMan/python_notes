'''
Created on 2013-3-2

@author: Administrator
'''
g_var = 0;
n1_var = 0;

print ("top level->g_var : {0} n1_var : {1}".format(g_var, n1_var));

def test():
    n1_var = 2;
    print("in test->g_var: {0} n1_var: {1} ".format(g_var, n1_var));
    
    def inner_test():
        global g_var;
        g_var = 1;
        n1_var = 4;
        print (" in inner_test->g_var:{0}, n1_var:{1}".format(g_var,n1_var));
        
    inner_test()
    print (" in test->g_var:{0}, n1_var:{1}".format(g_var,n1_var));    
test();
print (" out test->g_var:{0}, n1_var:{1}".format(g_var,n1_var));
        
 
 
global_var = 4;
 
def test_lgb():
    global global_var;
    print global_var;
    
    global_var += 5;
    print global_var;
    
test_lgb();
            
        
        
        
        