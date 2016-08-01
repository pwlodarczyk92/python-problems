def function1(x):
	x = x + 1

def function2(x):
	x = x + 1
	return x


x = 0
function1(x)
print(x)

print("########") 

y = 0
z = function1(y)
print(y)
print(z)

print("########") 

u = 0
function2(u)
print(u)

print("########") 

a = 0
b = function2(a)
print(a)
print(b)