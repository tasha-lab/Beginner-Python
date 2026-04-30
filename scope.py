#global scope. available to everything in the file.defined outside a function
name = "Tasha"

# def greeting():
#     print(name)
#     color='blue' #local scope
#     print(color)
# greeting()
# print(color)
def greeting(firstname):
    print(firstname)
    color='blue' #local scope
    print(color)
greeting('John')

def anotherFunction():
    greeting('Dave')
anotherFunction()