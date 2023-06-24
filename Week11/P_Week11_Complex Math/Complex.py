a = int(input("a: "))
b = int(input("b: "))

import math

pi = math.pi
sine = math.sin(a*b)
value = math.exp(a) + b**(pi) - sine

print("%0.3f"%(value))