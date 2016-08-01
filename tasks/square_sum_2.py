# write program reading an integer from standard input - a
# printing sum of all squares smaller than a,
# for example, for a=20, result = 1*1 + 2*2 + 3*3 + 4*4 = 30 (because 5*5=>a)

a = int(input("pass a - "))

element = 1
square = element * element #this could be "square = 1"
result = 0

while square < a:
    result = result + square
    element = element + 1
    square = element * element

print("result = " + str(result))
