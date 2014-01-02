class SchoolMember :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print ' (initialized schoolmember %s)' % self.name
        
    def tell(self):
        print 'Name : "%s" , Age : "%s" ' % (self.name, self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print 'Initialized teacher %s ' % self.name
        
    def tell(self):
        SchoolMember.tell(self)
        print 'salary :"%d" ' % self.salary
        
class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'Initialized student %s ' % self.name
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "%d"' % self.marks
        
t = Teacher('Mrs. shivi', 40, 30000)
s = Student('robertzhai', 22, 75)
#s=t
print

members = [t, s]
for member in members :
    member.tell()
    