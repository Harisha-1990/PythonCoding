#author: Harisha
#dictionary is a unordered key value pair
#dict
#data type in python but also a datastructure
#It's a way for us to organize information
#curly brackets dentoes dictionary
dictionary = {
  'a':1,
  'b':2
}
# a is Key and it's value 1
print(dictionary)
print(dictionary['b'])
#print(dictionary['c']) #error

dictionary = {
  'a':[1,2,3],
  'b':'hello',
  'x':True
}
# a is Key and it's value 1
print(dictionary)
print(dictionary['a'][2])
print(dictionary['b'])

my_list = [ 
  {
  'a':[1,2,3],
  'b':'hello',
  'x':True
}
, {
  'a':[4,5,6],
  'b':'hello',
  'x':True
}
]
print(my_list[0])
print(my_list[0]['a'])
print(my_list[0]['a'][2])
