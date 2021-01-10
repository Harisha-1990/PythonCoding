#author: Harisha
#lists unpacking
a,b,c =[1,2,3]
print(a)
print(b)
print(c)

a,b,c,*other = [1,2,3,4,5,6,7,8,9]
#unpack 1,2,3 and keep everthing same
print(other)

a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
#unpack 1,2,3 and keep everthing same
print(other)
print(d)
