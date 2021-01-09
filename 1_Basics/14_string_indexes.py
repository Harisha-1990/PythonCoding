#author : Harisha
#String indexes
selfish = 'me me me'
#          01234567
print(selfish[0])
print(selfish[2])
print(selfish[7])
print(selfish)

#[start:stop]
print(selfish[0:5])
print(selfish[0:8])

#[start:stop:stepover]
selfish = '01234567'
print(selfish[0:8:1])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
print(selfish[::2])
#In python negative index means start at the end of the string
print(selfish[-1])
print(selfish[-2])
#print(selfish[-10]) # out of range error
print(selfish[::-1])
