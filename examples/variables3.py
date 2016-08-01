class C:
	def __init__(self, ar):
		self.val = ar


x = C(0)
x.val = x.val + 1
print(x.val)

print("########") 

y = C(0)
z = y
z.val = z.val + 1
print(y.val)
print(z.val)

print("########") 

u = C(0)
v = u
u.val = u.val + 1
print(u.val)
print(v.val)

print("########") 

a = C(0)
b = C(a.val)
b.val = b.val + 1
print(a.val)
print(b.val)

print("########") 

i = C(0)
j = C(i.val)
i.val = i.val + 1
print(i.val)
print(j.val)
