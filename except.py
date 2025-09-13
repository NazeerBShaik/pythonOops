
x = 20
try:
    print(x)
except:
    print("An exception occured")
else:
    print("Nothing went wrong") 

finally:
    print("the try except is finished")       










x = -1
if x > 0:
    raise Exception("sorry no number below zero")
elif not type(x) is str:
    raise TypeError("only strings are allowed")
