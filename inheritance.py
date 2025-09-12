''' class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

        
    class Student(Person):
    #we can give any name as self
        def printname(abc):
            print(abc.fname, abc.lname)        

    x = Student("nazeer", "shaik")
    x.printname()
'''
# multilevel inheritance
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)                

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.grduationyear = year
# Adding methods
    def welcome(self):
        print("Welcome",self.fname, self.lname," to the class of ", self.grduationyear)
x = Student("Nazeer", "Shaik", 2025)
x.welcome()
# If you add a method in the parent class, the inheritance of the parent method will be overridden
