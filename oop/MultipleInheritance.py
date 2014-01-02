class Lister:
    def __repr__(self):
        return ( "<Instance of %s, address %s:\n>" % (self.__class__.__name__ , id(self)));

class Super:
    def __init__(self):
        self.data1 = 'spam';
    
class Sub(Super, Lister):
    def __init__(self):
        Super.__init__(self);
        self.data2 = 'eggs';
        self.data3 = 42;

x = Sub();
print x;
