class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("This is just not cool man")
    # # print(x/0)
    # if not type(x) is str:
    #     raise TypeError('Only strings are allowed')
    # raise Exception("I'm a custom exception!")
except NameError:
    print('NameError means something is probebaly undefined')
except Exception as Error:
    print(Error)
except ZeroDivisionError:
    print('Do not divide a number by 0')
else:
    print('No errors')
finally:
    print("I'm going to print with or without an error")
