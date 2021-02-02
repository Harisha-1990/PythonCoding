user ={
  'basket':[1,2,3],
  'greet':'hello',
  'age':20
}

print('age' in user.keys())
print('hello' in user.values())
print(user.items())
print(user.clear())

user ={
  'basket':[1,2,3],
  'greet':'hello',
  'age':20
}
user.clear()
print(user)

user ={
  'basket':[1,2,3],
  'greet':'hello',
  'age':20
}
user2 = user.copy()
print(user2)

user ={
  'basket':[1,2,3],
  'greet':'hello',
  'age':20
}
user2 = user.copy()
print(user.clear())
print(user2)

user ={
  'basket':[1,2,3],
  'greet':'hello',
  'age':20
}
print(user.pop('age')) #pop returns the value of whatever got removed
print(user)

user ={
  'basket':[1,2,3],
  'greet':'hello',
  'age':20
}
print(user.popitem())#popitem randomly pops of some pair of key value 
print(user)

user ={
  'basket':[1,2,3],
  'greet':'hello',
  'age':20
}
print(user.update({'age':55})) # update as the name suggests simply updates the key value
print(user)

user ={
  'basket':[1,2,3],
  'greet':'hello',
  'age':20
}
print(user.update({'gender':'F'})) # update as the name suggests simply updates the key value
print(user)
