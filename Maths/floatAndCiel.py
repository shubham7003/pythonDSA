import math

def divison(a,b):
    x = a//b
    y = math.ceil(a/b)

    return [x, y]

print(divison(5,2))
print(divison(-7,2))