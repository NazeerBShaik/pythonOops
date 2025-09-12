# x = "Hello world"
# print(len(x))
# Polymorphism is often used in class methods, where we can have multiple classes with the same method name
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat(Car):
    def move(self):
        print("Sail!")

class Plane(Car):
    def move(self):
        print("Fly!")

car1 = Car("ford","mustang")                         
boat1 = Boat("ibiza","touring 20")
plane1 = Plane("boeing","747")

for x in (car1, boat1, plane1):
    x.move()