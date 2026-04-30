#reusable blocks of code
#def-defines the functions
#hello- names the function.should be lowercase and use underscores
#hello()-calls the function
#parameters-placeholders for data. they go inside the function name parenthesis.they do not change
#sum(2,3) 2 and 3 are the arguments.They can change
def hello():
    print('Hello World!!')
hello()

def sum(num1,num2):
    print(num1+num2)
sum(2,3)
sum(7,10)

def sum2(num1=0,num2=0):
    # if type(num1) is not int or type(num1) is not int
    if type(num1) != int or type(num1) != int:
        return 0
    return num2+num1
total=sum2('a')
print(total)

#when we dont know the number of arguments, use *args
#returns a tuple
def multiple_items(*args):
    print(args)
    print(type(args))
multiple_items('Dave','John','Sarah')

#heyword arguments
#returns a dictionary
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
mult_named_items(first='Dave',last='John')

