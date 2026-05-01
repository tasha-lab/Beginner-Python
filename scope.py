#global scope. available to everything in the file.defined outside a function
name = "Tasha"
count = 1

# def greeting():
#     print(name)
#     color='blue' #local scope
#     print(color)
# greeting()
# print(color)
# def greeting(firstname):
#     print(firstname)
#     color='blue' #local scope
#     print(color)
# greeting('John')

# def anotherFunction():
#     greeting('Dave')
# anotherFunction()
def anotherFunction():
    color='blue'
    #referencing a global scope while a similar local scope is defined
    global count
    count+=2
    print(count)
    def greeting(name):
        #reading a value from a parent function then reassigning it
        nonlocal color
        color = 'red'
        print(name)
        print(color)
    
    greeting('John')
anotherFunction()