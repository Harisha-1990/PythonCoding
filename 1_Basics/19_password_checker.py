#author : Harisha
#password checker
username = input('What is your user name\n')
password = input('What is your password\n')
length_of_pwd = len(password)
hidden_pwd = '*' * length_of_pwd
print(f'{username} your password {hidden_pwd} is {length_of_pwd} letters long')
