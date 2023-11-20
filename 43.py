amazon_cart = [
    'notebook',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart)
print(amazon_cart[0:3]) #it will print from 0 to 2 as it always print 1 less
print(amazon_cart[0::2]) #it will skip the index value by 2
#  greet = 'hello'
#  greet[0] = 'z'
# it will show error as we cannot change string with this index value only can be done for the list  
amazon_cart[0]='laptop'
new_cart = amazon_cart[0:3] # it means it make a copy of a amazon cart not uses it directly
print(amazon_cart )
new_cart = amazon_cart # in this it uses the same it means it make changes in the original file not make a copy and do changes in that copy
# if we uses [:] then only it make copy and done changes in that

new_cart[0] = 'gum'
#print/(amazon_cart[1:3])
print(new_cart )
print(amazon_cart )

