import bisect

a=[24,33,41,41,45,50, 53,59, 62, 66, 70]
i=bisect.bisect_left(a, 41)
print("item i:")
print(i)

b=[1.3, 2.2, 3.4, 4.6, 5.5, 6.9, 7.2, 8.4]
j=bisect.bisect_left(b, 4.1)
print("item j:")
print(j)

c=['aaa', 'bbb', 'ccc', 'ddd']
k=bisect.bisect_left(c, 'bug')
print("item k:")
print(k)
print("item d:")
d=[24, 33, 41, 41, 45, 50, 53, 59, 62, 66, 70]
bisect.insort_left(d, 44)
print(d)


print("item i mais a direita:")

r=bisect.bisect_right(a, 41)

print(r)

print("inserir um elemento a d mais a direita:")

bisect.insort_right(d, 51)

print(d)
