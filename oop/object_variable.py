class Person :
    population = 0
    
    def __init__(self, name): #constructor
        self.name = name
        Person.population += 1
    
    def __del__(self): # destructor
        Person.population -= 1
        
        if Person.population == 0 :
            print ' I am the last one'
        else :
            print 'there are still %d person left' % Person.population
            
    def sayHi(self):
        print 'Hi,my name is %s' % self.name
        
    def howMany(self):
        if Person.population == 1 :
            print ' I am the only person here'
        else :
            print ' we have %d persons here' % Person.population
            
p = Person('robert zhai')
p.sayHi()
p.howMany()

p2 = Person('python one')

p2.sayHi()
p2.howMany()

p.sayHi()
p.howMany()

            
