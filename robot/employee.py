#Our pizza shop team can be defined by the following classes in the 
#example file employees.py. It defines four classes and some self-test 
#code. The most general class, Employee, provides common behavior such 
#as bumping up salaries (giveRaise) and printing ( __ repr __ ). There
# are two kinds of employees, and so two subclasses of Employee--Chef and
#  Server. Both override the inherited work method to print more specific
#   messages. Finally, our pizza robot is modeled by an even more specific
#    class: PizzaRobot is a kind of Chef, which is a kind of Employee. 
#    In OOP terms, we call these relationships "is-a" links: a robot is 
#    a chef, which is a(n) employee.

class Employee:
    def __init__(self,name,salary=0):
        self.name = name;
        self.salary = salary;
        
    def giveRaise(self,percent):
        self.salary = self.salary * (1+percent);
        
    def work(self):
        print self.name , " does stuff";
    
    def __repr__(self):
        return "<Employee : name = %s, salary = %s>" %(self.name, self.salary);
    
class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary = 50000);
        
    def work(self):
        print self.name ,'makes food';
        
class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary = 40000);
    def work(self):
        print self.name , " interfaces with customer";

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name);
    def work(self):
        print self.name , " makes pizza";

if __name__ == '__main__':
    bob = PizzaRobot('bob');
    print bob;
    bob.giveRaise(0.20);
    print bob;print;
    
    for klass in Employee,Chef,Server,PizzaRobot:
        obj = klass(klass.__name__);
        obj.work();

        


