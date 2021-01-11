#author: Harisha
# a key in the dictionary has to be unique
user = {
  'basket':[1,2,3],
  'greet':'hello'
  }
print(user['basket'])
print(user.get('basket'))
print(user.get('age',55)) # If age doesn't exists on the user dictionary then pull 55

user = {
  'basket':[1,2,3],
  'greet':'hello',
  'age':25
  }
print(user['basket'])
print(user.get('basket'))
print(user.get('age',55))# gets the value defined in the user dictionary


user = {
  'basket':[1,2,3],
  'greet':'hello',
  'age':25
  }
user2 = dict(name='john john') # we can alo create dictionary by using built in function
#we can also create the dectionary like the one we created for user
print(user2)
