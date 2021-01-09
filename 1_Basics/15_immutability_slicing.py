#author : Harisha
#Immutability
#Slicing: The idea of accessing string using [start:stop:stepover] is called slicing because we can slice the string however we like. 
#Immutable:we cannot change the value of it once it is created
#strings are immutable
selfish = '01234567'
#selfish[0]=8
print(selfish) #error indicates str obect doesnt support item assignment 
# the only way yo change the string is by creating something like below
selfish = selfish+'8'
print(selfish)
