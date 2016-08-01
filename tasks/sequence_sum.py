# write program reading two integers from standard input - a and b
# printing sum of natural numbers from a to b
# for example, for a=3 and b=6, result = 3 + 4 + 5 + 6 = 18

a = int(input("pass a - "))
b = int(input("pass b - "))

while element <= b:
    result = result + element
    element = element + 1

print("result = " + str(result))
