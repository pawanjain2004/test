basket = [1,2,3,4,5]
print(len(basket))
#adding
new_list = basket.append(100)
print(new_list)
#here it print none as append change the existing list not going to print tha
new_list= basket # now here we equate newlist and basket
#insert and append only modify the list not copy itmodify only
print(basket)
print(new_list)
# addem dded any number to the last of the list
# but if we have to add in the middle of list then we have to use insert 
basket.insert(4, 100) # here 4 is the index value
print(basket)
new_list = basket.extend([110])
print(basket)
new_list= basket.extend([110,120,130])
print(basket)
#using extend we can add multiple number but at the end
print("removing")
#forremoving
pinnet=[1,2,3,4,5]
pinnet.pop()#it remove the last digit of the list
pinnet.pop(0)#it remove the value on the index value zero
pinnet.remove(3)#it remove the value 3 from the list
#remove also not a copy of the code

print(pinnet)
pinnet=[1,2,3,4,5]
new_list=pinnet.pop(4)
print(new_list)
#in this the result is 5 means index value 4 is 5 
#index value get copied in the pop
new_list=pinnet.remove(4)
print(new_list)
#in this none come means no copy
#clear remove every thing from the list
new_list=pinnet.clear()
print(basket)
