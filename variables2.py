x = [0]
x[0] = x[0] + 1
print(x[0])

print("########") 

y = [0]
z = y
z[0] = z[0] + 1
print(y[0])
print(z[0])

print("########") 

u = [0]
v = u
u[0] = u[0] + 1
print(u[0])
print(v[0])

print("########") 

a = [0]
b = [a[0]]
b[0] = b[0] + 1
print(a[0])
print(b[0])

print("########") 

i = [0]
j = [i[0]]
i[0] = i[0] + 1
print(i[0])
print(j[0])

print("########") 

q = [0]
r = [q]
s = [r[0]]
q[0] = q[0] + 1
r[0][0] = r[0][0] + 1
print(q[0])
print(r[0])
print(s[0])

print("########") 

q = [0]
r = [q[0]]
s = [r[0]]
q[0] = q[0] + 1
r[0] = r[0] + 1