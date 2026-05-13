#single function that returns a value
squared = lambda num : num*num
print(squared(2))


addTwo= lambda num : num+2
print(addTwo(6))

sum_total= lambda a,b : a + b
print(sum_total(2,2))
print(sum_total(10,8))

########################################
#lambda is mostly used in other functions

def funcbuilder(x):
    return lambda num: num+x
addTen = funcbuilder(10)
addTwenty = funcbuilder(20)

print(addTen(7))
print(addTwenty(10))

########################################3
#higher oder function = function that takes as a function as an argument or return a function

numbers =[2,3,5,18,20,21]
#map-built in function that receives a function as its first argument
squaredNums = map(lambda num : num*num,numbers)
print(list(squaredNums))

#filter

odd_nums = filter(lambda num : num%2 != 0,numbers)
print(list(odd_nums))

###############################3
from functools import reduce


numbers = [1,2,3,4,5,1]
total = reduce(lambda accumulator, current : accumulator + current,numbers,10)
print(total)
print(sum(numbers,10))



names = ['Dave Gray','Sarah Ito','John Jacob dhjkjaskdnDGJK23BC']

char_count = reduce(lambda acc, curr: acc+len(curr),names,0)

print(char_count)