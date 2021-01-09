#author : Harisha
#Built in functions + methods
print(len('hello family')) #caluclates the length of the string
greet= 'hello family'
print(greet[0:len(greet)])
# Built in function: Built in function had the syntax of the word that was highlighted in blue and then brackets to perform some action on a datatype
# Built in methods: Methods are similar to functions but they are owned by something. In python there are some methods that only strings can perform.Usually have a dot infront of it.

# .format() is a method
quote ='to be or not to be'
print(quote.upper()) # capitalizes everything
print(quote.capitalize()) # first letter will be capitalized
print(quote.find('be')) # gives us the first occurence of the b which is position 3. 
print(quote.replace('be','me'))
print(quote)
quote2 = quote.replace('be','me')
print(quote2)
