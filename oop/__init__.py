class Person :
    def __init__(self, name): # constructor
        self.name = name
    def sayHi(self):
        print 'hello ,my name is ', self.name
        
p = Person('robert zhai')
p.sayHi()

Person('workman').sayHi()