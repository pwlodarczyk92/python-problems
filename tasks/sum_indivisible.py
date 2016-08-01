# write program reading an integer from standard input - a
# printing sum of all numbers indivisible by 3, smaller than a
# for example, for a=10, result = 1 + 2 + 4 + 5 + 7 + 8 = 27

a = int(input("pass a - "))

element = 1
result = 0

while element < a:
	if element % 3 != 0 :
		result = result + element
	element = element + 1

print("result = " + str(result))
