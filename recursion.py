#recursion=a function calls itself
def add_1(num):
    if num>=9:
        return num+1
    total=num+1
    print(total)
    #line 2-5 prints only 1-9
    return add_1(total) #calls itself until it is equal to or greater than 9
add_1(0)
#to print 10, assign add_1(0) to avariable and print out the variable