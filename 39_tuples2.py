my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2]
print(new_tuple)

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:4]
print(new_tuple)

x,y,z,*other = (1,2,3,4,5)
print(x)
print(z)
print(other)

my_tuple = (1,2,3,4,5,5)
print(my_tuple.count(5))#count how many 5's in the my_tuple
print(my_tuple.index(5))
print(len(my_tuple))
