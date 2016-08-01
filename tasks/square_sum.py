# write program reading an integer from standard input - a
# printing sum of squares of natural numbers smaller than a
# for example, for a=4, result = 1*1 + 2*2 + 3*3 = 14

a = int(input("pass a - "))

element = 1
result = 0

while element < a:
    result = result + element * element
    element = element + 1

print("result = " + str(result))
