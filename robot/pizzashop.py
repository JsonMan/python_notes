from employee import Server,PizzaRobot
class Customer:
    def __init__(self, name):
        self.name = name;
    def order(self, server):
        print self.name ," orders from ", server;
    def pay(self, server):
        print self.name, " pays for items to " , server;
        
class Oven:
    def bake(self):
        print " oven bakes";
        
class PizzaShop:
    def __init__(self):
        self.server = Server('Pat');
        self.chef = PizzaRobot('Bob');
        self.oven = Oven();
    
    def order(self, name):
        customer = Customer(name);
        customer.order(self.server);
        self.chef.work();
        self.oven.bake();
        customer.pay(self.server);
        
scene = PizzaShop();
scene.order('Homer');
print '...';
scene.order('Shaggy');
