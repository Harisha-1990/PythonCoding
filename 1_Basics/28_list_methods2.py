#author: Harisha
#list methods 
#sort returns none
basket = ['a','b','c','d','e','d']
basket.sort()
print(basket)

basket = ['a','x','b','c','d','e','d']
basket.sort()
print(basket)

#sorted produces a new array
basket = ['a','x','b','c','d','e','d']
print(sorted(basket))
print(basket) #basket hasn't been modified


basket = ['a','x','b','c','d','e','d']
new_basket= basket[:]
new_basket.sort()
print(new_basket)

#reverse
#reverse returns noen
basket = ['a','x','b','c','d','e','d']
basket.reverse()
print(basket)

#sort and reverse
basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print(basket)
