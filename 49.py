a,b,c = [1,2,3]
print(a)
print(b)
print(c)
a,b,c, *other =[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
a,b,c, *other,d =[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
# in this d is asssign to 9 and so not print
print(d)