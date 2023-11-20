#formatted strings
name = "Pawan"
age = 55
print('hi ' + name + '. You are ' + str(age) + ' years old')
# we have another way
print(f'hi {name} . You are {age} years old') # f suggest that it is a formatted string
#another way by .format
print('hi {} . You are {} years old'.format('pawan', '54'))
print('hi {1} . You are {0} years old'.format(name, age)) # name is earlier so it is 0 and another one is 1


