#author : Harisha
#list methods
basket = [1,2,3,4,5]
#add : None is returned
new_list = basket.append(100) #append will append the value to the end of the list.
print(new_list)
print(basket)

basket = [1,2,3,4,5]
#add
basket.append(100)
new_list= basket
print(new_list)
print(basket)
#insert : with insert we can inset the value at any where in the list. 
basket = [1,2,8,4,5]
basket.insert(3,100)
new_list = basket
print(new_list)
print(basket)
#extend:iterable which iterates over the list. simple terms extends our list
#none is returned
basket = [1,2,3,4,5]
basket.extend([100,101])
print(basket)
basket = [1,2,3,4,5]
basket.extend([100])
print(basket)
#pop: removes the value based on the index provided or removes a value at the end when just brackets enclosed.
#also returns the value whatever you've removed. 
basket =[1,2,3,4,5]
basket.pop()
print(basket.pop(0)) # this returns whatever you have just removed
#removes: removes the value provided
#none is returned
basket =[1,2,3,4,5,100,200]
basket.remove(100)
print(basket)
#clear: clears the list
# None is returned
basket = [1,2,3,4,5]
new_list =basket.clear()
print(new_list)
print(basket)
