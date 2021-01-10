#author : Harisha
#list methods
basket = [1,8,7,9,10]
#index, returns the index of the value provided.
print(basket.index(9))
#print(basket.index(9,0,2)) # looks for value 9 in the list from index 0 to 2 
#throws an error that 9 is not in the list. 
print(basket.index(9,0,4))

#keyword is something thats pre built in python that has some meaning
print(9 in basket)
print('x' in basket)
print('h' in 'harisha')
print('I' in 'harisha')

#count, count how many times an item occurs
basket = ['a','b','c','d','e','d']
print(basket.count('d'))
