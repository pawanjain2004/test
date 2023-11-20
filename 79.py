#Exercise to check variable
some_list = ['a','b','c','b','d','m','n','n']
duplicate = []

for value in some_list:
    if some_list.count(value)>1:# count(value) it check each value in the list that how many timmes does it repeated
        
        if value not in duplicate: 
            duplicate.append(value) # append (value) it just copied the value from one to other one
            
       
print(duplicate)        
    