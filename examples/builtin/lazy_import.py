'''
Created on 2013-8-29

@author: Administrator
'''
class LazyImport:
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None
    
    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name)
            
            return getattr(self.module, name)

string = LazyImport("string")
print string.lowercase
        
       