#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value

user = {
  'age':22
  ,'username':'harisha'
  ,'weapons':['karate','dance']
  ,'is_active': True
  ,'clan': 'Japan'
}
print(user.keys())
user['weapons'].append('kungfu')
print(user)
user.update({'is_banned':False})
print(user)
user.update({'is_banned':True})
print(user)
user2= user.copy()
print(user2)
user2.update({'age':25,'username':'kalista'})
print(user2)
