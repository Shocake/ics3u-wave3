from math import sqrt
def pyth(a, b):
    return sqrt(a**2 + b**2)

a = float(input("Input a"))
b = float(input("Input b"))

print("The hypoteneuse is " + str(pyth(a, b)) + " units long.")