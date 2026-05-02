#older methods
person = 'Dave'
coins =3

print('\n'+person+' has '+str(coins)+' coins left')

#%s method - older way
message = '\n%s has %s coins left' %(person,coins)
print(message)
#the format method
message = '\n{} has {} coins left'.format(person,coins)
print(message)
#using Index
message = '\n{0} has {1} coins left'.format(person,coins)
print(message)
#assigning the values
message = '\n{person} has {coins} coins left'.format(person=person,coins=coins)
print(message)

player = {'person':'Dave','coins':4}
message = '\n{person} has {coins} coins left'.format(**player)
print(message)

################
#f-stings. This is the way
#used to format strings

message = f"\n{person} has {coins} coins left"
print(message)
message = f"\n{person} has {2*5} coins left"
print(message)
message = f"\n{person.upper()} has {2*5} coins left"
print(message)
message = f"\n{player['person']} has {3*5} coins left"
print(message)

####################
#You can pass formatting options
num = 10
print(f"\n2.25 times {num} is equal to {2.25*num:.2f}")#f stands for fixed

for num in range(1,11):
    print(f"\n2.25 times {num} is equal to {2.25*num:.2f}")
for num in range(1,11):
    print(f"\n4.52 divided by {num} is equal to {num/4.52:.2%}")

