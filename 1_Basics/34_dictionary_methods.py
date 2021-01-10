#author: Harisha
#dictionary is a unordered key value pair
#dict
#dictionary keys need to have a special property. A key needs to be immutable.
# we cannot give list in the keys becuase the list is mutable.
#Also a key in the dictionary has to be unique
dictionary = {
  123:[1,2,3],
  'greeting':'hello',
  'is_magic':True
  }
print(dictionary[123])

dictionary = {
  123:[1,2,3],
  True:'hello',
  'is_magic':True
  }
print(dictionary[True])


dictionary = {
  123:[1,2,3],
  True:'hello',
  [100]:True
  }
#print(dictionary[100]) #result in error
# a key in the dictionary has to be unique
dictionary = {
  '123':[1,2,3],
  '123':'hello'
  }
print(dictionary['123'])
