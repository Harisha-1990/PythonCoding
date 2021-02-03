#set : sets are unordered collections of unique objects
#no duplicates
my_set = {1,2,3,4,5}
print(my_set)
my_set = {1,2,3,4,5,5}
print(my_set)
my_set.add(2)
my_set.add(100)
print(my_set)
my_list = [1,2,3,4,5,5]
print(set(my_list))
my_set = {1,2,3,4,5}
print(list(my_set))
my_set = {1,2,3,4,5}
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)
