class C:
	def __init__(self, x):
		self.val = x


def function1(arg1):
	value = arg1
	return value

x = C(0)
y = function1(x)
x.val = x.val + 1
print(x.val)
print(y.val)

print("########") 

p = C(0)
q = function1(p)
q.val = q.val + 1
print(p.val)
print(q.val)

print("########") 


def function2(arg1):
	value = C(arg1.val)
	return value

a = C(0)
b = function2(a)
b.val = b.val + 1
print(a.val)
print(b.val)

print("########") 

i = C(0)
j = function2(i)
i.val = i.val + 1
print(i.val)
print(j.val)

print("########") 


def function3(arg1):
	value = arg1.val+1

z = C(0)
function3(z)
print(z.val)

print("########") 


def function4(arg1):
	arg1.val = arg1.val+1

t = C(0)
function4(t)
print(t.val)

print("########") 


def function5(arg1):
	value = arg1.val + 1
	return value

u = C(0)
v = function5(u)
v = v + 1
print(v)
print(u.val)

print("########") 


def function6(arg1):
	arg1.val = arg1.val+1
	return arg1.val

r = C(0)
s = function6(r)
s = s + 1
print(r.val)
print(s)

print("########") 

k = C(0)
function6(k)
print(k.val)