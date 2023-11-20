basket = ['a','x','b','c','d','d','e']
print(basket.sort())
# none come as sort only modify the list
basket.sort()
print(basket)

toffie = ['a','b','c','f','e','d']
print(sorted(toffie))
# it will print a sorted array and the changes in the array will done in a copy 
# the original remain the same
print(toffie)
# reverse function which reverses the whole array
toffie.reverse()
print(toffie)