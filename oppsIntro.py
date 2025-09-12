class MyClass:
    x = 5


#example 1 print class dierctly
print(MyClass)   
#example 2 crate an object
y = MyClass()   
print(y.x)    

#The __init__() Method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Nazeer", 29)
print(p1.name)
print(p1.age)
#The string representation of object with the __str__() method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"        


p1 = Person("Nazeer", 29)
print(p1)
#Creating functions
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}I am  {self.age} old")

p1 = Person("Nazeer", 29)
p1.myfunc()
#self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
#it doesnt have to be named self you can call it whatever you like but it has to be the first parameter of any function in the class
class Person:
    def __init__(mysillyobj, name, age):
        mysillyobj.name = name
        mysillyobj.age = age
    
    def myfunc(abc):
        print(f"Hello my name is {abc.name} my age is {abc.age}" )
p1 = Person("Nazeer", 29)
#modifying object properties
p1.age = 30
#delete object properties
# del p1.age
#delete objects
# del p1
p1.myfunc()




























