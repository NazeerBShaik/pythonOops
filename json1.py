import json
# convert json to python dict
x = '{ "name":"Nazeer","age":29, "city":"Nellore"}'
y = json.loads(x)
print(y["age"])

#convert form python to json
x = { 
    "name":"Nazeer",
    "age":29,
    "city":"Nellore"
}
y = json.dumps(x)
print(x)
#to define the number of indents
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4))
#to change the default parameter
print(json.dumps(x, indent=4, separators=(". ", "= ")))
#to order the result use sort_keys parameter
print(json.dumps(x, indent=4, sort_keys= True))












