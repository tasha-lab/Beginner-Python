#dictionaries
band ={
    "vocals":"plant",
    "guitar":"page"
}
band2 = dict(vocals='plant',guitar='page')

print(band)
print(band2)
print(type(band))
print(len(band))

#access items
print(band['vocals'])
print(band.get('guitar'))

#list all keys
print(band.keys())
#list all values
print(band.values())
#list of key/value pairs as tuples
print(band.items())
print(type(band.items()))

#verify key exist in dictionary
print('guitar' in band)
print('vocals' in band)
print('violin' in band)

#change values
band['vocals']='Coverdale'
print(band)
band.update({"bass":"JPJ"})
print(band)
print(band.pop('bass'))
print(band)
band["drums"]='Bonham'
print(band)
print(band.popitem()) #removes what was last added and returns a tuple

#delete and clear
band["drums"]='Bonham'
del band['drums']
print(band)

band2.clear()
print(band2)

del band2

#copying dictionaries
# band2 =band #creates a reference.They are both refering to the same place in memory or dictionary
# print('bad copy!')
# print(band2)
# print(band)

# band2['guitar']='Dave'
# print(band)

band2 = band.copy()
print(band2)
print('good copy!')
band2['drums']='Bonham'
print(band2)
print(band)

#using dict constructor function
band3 = dict(band)
print(band3)
print('')
#nested dictionaries
member1 = {
    'name':'plant',
    'instrument':'vocals'
}
member2 = {
    'name':'page',
    'instrument':'guitar'
}
band ={
    "member1":member1,
    "member2":member2
}
print(band)
print(band['member1']['name']) #getting a single value


##sets
nums ={1,2,3,4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicates are allowed.ignores the duplicate
nums ={1,2,3,4,2}
print(nums)

#true is a dupe of 1 and false is a dupe of 0
nums ={1,True,3,4,5,False,0}
print(nums)

#check if a value is in a set
print(2 in nums)
print(4 in nums)
#but you cannot refer to an items using an index position or using the key

#adding elements to a set
nums.add(8)
print(nums)

#add elements from one set to another
moreNums ={5,6,7,8,9}
nums.update(moreNums)
print(nums)

#you can use update with lists,tuples and dictionaries too
#merge 2 sets to create a new set
one = {1,2,3}
two = {4,5,6}

myNewSet=one.union(two)
print(myNewSet)

#heep only duplicates
one = {1,2,3,2,4}
two = {4,5,6,3,2}

one.intersection_update(two)
print(one)

#keep everything other than the duplicates
one = {1,2,3,2,4}
two = {4,5,6,3,2}

one.symmetric_difference_update(two)
print(one)