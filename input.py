import math

name = input("Enter your name: ")
print(f"Hello {name}")

#multiple inputs
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

#input number
x = input("Enter a number:")

y = math.sqrt(float(x))
print(f"The sqare root if {x} is {y:.2f}")

#validate input
y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again.")

print("Thank you")