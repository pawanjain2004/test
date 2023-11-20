user_name = input('what is your name')
password=input('what is your password')
length_password = len(password)
hidden_password= '*' * length_password
print(f'{user_name} your password is  {hidden_password} is {length_password} letters long')
