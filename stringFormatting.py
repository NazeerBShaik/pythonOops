price = 59
tax = 0.25
fruit = "apples"

txt = f"The price is {price:.2f} dollors and {price + (price * tax)}"
txt = f"It is very{'Expensive' if price > 50 else 'Cheap'}"
print(txt)
fruits = f"I love {fruit.upper()}"
print(fruits)