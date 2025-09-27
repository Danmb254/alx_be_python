#sets
a = {3, 4, 5}
b = {4, 5, 6,7, 8, 9, 6, 6, 5, 4}
c = a.intersection (b)
print(c)
d = a.union(b)
print(d)
e = b.difference(a)
print(e)
f = 8
print(a in b)
print(b in a)
print(e in b)
print(f in e)
g = list(b)
print(g)
h= set(g)
print(h)