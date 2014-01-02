

class ThirdClass:
    def setData(self,data):
        self.data = data;
    def display(self):
        print self.data;
    def __add__(self,other):
        tmp =  ThirdClass();
        tmp.setData(self.data+other);
        return tmp;
    def __mul__(self,other):
        self.data = self.data * other;

z = ThirdClass();
z.setData('abc');
z.display();
t = z+'xyz';
t.display();
z*3;
z.display();