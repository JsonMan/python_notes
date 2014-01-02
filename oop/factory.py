def factory(aClass, *args):
    return apply(aClass, args);

class Spam:
    def doit(self, message):
        print message;
        
class Person:
    def __init__(self, name, job):
        self.name = name;
        self.job = job;
        print self.name ,"," ,self.job;
        
        
obj1 = factory(Spam);
obj2 = factory(Person, 'root', 'linux');
