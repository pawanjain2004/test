# *args  **kwargs
# args is arguments
# kw args iss key word arguments
# RULE : param , *args , default parameters , **kwargs
# param is parameters
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
# args take the value 1 ,2,3,4,5
# where kwargs take the value from num1 - 5 and num 2 = 10

print(super_func('pawan', 1, 2, 3, 4, 5, num1=5, num2=10))
