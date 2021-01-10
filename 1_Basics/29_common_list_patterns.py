#author: Harisha
#Common list patterns 
#sort returns none
basket = ['a','x','b','c','d','e','d']
print(basket[::-1])# this is also acting like reverse function

#range
#If i want to generate a list from 1 to 100, i can use range
print(range(1,100))
print(list(range(1,100)))
print(list(range(100)))

#.join 
# dot join works on strings
# .join() is a string method that joins lists into a string
# It's often used in below way

sentence ='hey'
new_sentence = sentence.join(['hi','my','name','is','harisha'])
print(new_sentence)

sentence =' '
new_sentence = sentence.join(['hi','my','name','is','harisha'])
print(new_sentence)
