# Techinically in python an iterator is an object whih implements the iterator protocol which consists of the methods 
#__iter__() and __next__()
# iter() method
'''
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
'''
#even strings are also iterable objects
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# we can also use a for loop to iterate through an iterable object
mytuple = ("apple","banana","cherry")

for x in mytuple:
    print(x)