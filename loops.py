value = 1
# while value <= 10:
#     print(value)
#     #breaking the statement
#     if value == 5:
#         break
#     value+=1

# while value <= 10:
#     value+=1 #increament before the if statement to avoid it only stopping at 5
#     #breaking the statement
#     if value == 5:
#         continue
#     print(value)
# else:
#     print('Value is equal to'+str(value))

#for loops iterate over a sequence
names = ['Dave','Sarah','John']
# for x in names:
#     print(x)

# for x in "mississippi":
#     print(x)
# for x in names:
#     if x == 'Sarah':
#         break
#     print(x)
# for x in names:
#     if x == 'Sarah':
#         continue #skips an iteration and goes to the next one
#     print(x)

# for x in range(5):
#     print(x)
# print('')
# for x in range(2,4):
#     print(x)
# for x in range(5,101,5):
#     print(x)
# else:
#     print('glad that\'s over')

names = ['Dave','Sarah','John']
actions =['codes','eats','sleeps']
for name in names:
    for action in actions:
        print(name+" "+action+" ")
print('')
for action in actions:
    for name in names:
        print(name+" "+action+" ")