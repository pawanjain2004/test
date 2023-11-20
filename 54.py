#Dictonary
user ={
    'basket' : [1,2,3],
    'greet': 'hello',
    'age': 20
}
print(user.get('age',55))
user ={
    'basket' : [1,2,3],
    'greet': 'hello',
    #'age': 20
}
print(user.get('age',55))
user ={
    'basket' : [1,2,3],
    'greet': 'hello',
    #'age': 20
}
print(user.get('age'))#if we use  .get then if age doesnot exist then none come error not come

#print(user(age))
user2 = dict(name='Johncena')
print(user2)

