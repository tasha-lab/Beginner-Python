#lists hold multiple values
users = ['Dave','Sarah','Tom']
data = ['Dave',42, True]
empty =[]

print('Dave' in users)
print('Dave' in data)
print('Dave' in empty)
print(users[0])
print(users[-1])
print(users[-2])
print(users.index('Sarah'))
print(users[0:])
print(users[0:2])
print(users[-3:-1])
print('')


print(len(data))
users.append('Elsa')
print(users)

users +=['Jason','Mary']
print(users)
users.extend(['Robert','John'])
print(users)
print('')
users.insert(0,'Bob')
print(users)
users[2:2]=['Eddie','Alex']
print(users)
print(users.index('Alex'))
print(users.index('Eddie'))

users[1:3]=['Robert','Carol']
print(users)
users.remove('Bob')
print(users)
print(users.pop())
print(users)
del users[0]
print(users)

# del data
data.clear()
print(data)
print('')

users[1:2]=['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,80,2,65,70]
# nums.reverse()
# print(nums)

# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

#preserving the original list
print(sorted(nums,reverse=True))
print(nums)

#making a copy
numsCopy = nums.copy()
myList=list(nums)
myNums =nums[:]

print(numsCopy)
myList.sort()
print(myList)
print(myNums)
print(nums)

print(type(nums))

anotherList=list([1,'Neil',True])
print(anotherList)
print('')

#Tuples. they cannot be changed
title = "Tuples".upper()
print(title.center(20, "="))
myTuple = tuple(('Dave',42,True))
#packing a tuple
anotherTuple = (1,2,3,4,2,2,2)

print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append('Neo')
newTuple = tuple(newList)
print(newTuple)
#unpacking a tuple
(one,two, *hey)=anotherTuple
print(one)
print(two)
print(hey)
(one,*two,hey)=anotherTuple
print(one)
print(two)
print(hey)
print(anotherTuple.count(2))