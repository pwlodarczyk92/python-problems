x = True
if x:
	print("if")
else:
	print("else")
print(x)

print ("########")

y = True
if y:
	y = False
	print("if")
else:
	y = True
	print("else")
print(y)

print ("########")

z = 0
if z == 0:
	print("if")
elif z == 1:
	print("elif")
else:
	print("else")
print(z)

print ("########")

u = 0
if u == 0:
	print("if1")
	u = 1

if u == 1:
	print("if2")
print(u)

print ("########")

a = 0
if a == 0:
	print("if")
	a = 1
elif a == 1:
	print("elif")
	a = 2
else:
	print("else")
print(a)

print ("########")

b = [0]
def checkb(arg):
	arg[0] = arg[0]+1
	return True

if checkb(b):
	print("if")
elif b[0] == 1:
	print("elif")
else:
	print("else")
print(b)

print ("########")

c = [0]
def checkc(arg):
	arg[0] = arg[0]+1
	return False

if checkc(c):
	print("if")
elif c[0] == 1:
	print("elif")
else:
	print("else")
print(c)

print ("########")

d = [0]
def checkd(arg):
	arg[0] = arg[0]+1
	print("check")
	return False

if d[0] == 0:
	print("if")
elif checkd(d):
	print("elif")
else:
	print("else")
print(d)

print ("########")

if True:
	p = 0
else:
	q = 1
print(p)

print ("########")


if True:
	r = 0
else:
	s = 1
print(s)

