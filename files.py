# r - Read
# a - Append|update-creates files if it doesnt exists
# w - Write
# x - Create
import os

#Read- error if a file does not exist
f = open("names.txt") #f = open("names.txt","r")
# print(f.read())
# print(f.read(2))
# print(f.readline())
# print(f.readline())
for line in f:
    print(line)

f.close() #always close the file

try:
    f=open("names_list.txt")
    print(f.read())
except:
    print("The file does not exist!")
finally:
    f.close()

#######################Append##############################
f=open("names.txt", "a")
f.write("\nNeil")
f.close()

f=open("names.txt")
print(f.read())
f.close()
####################write######################
f=open("context.txt","w")
f.write("i deleted all of the context")
f.close()

f=open("context.txt")
print(f.read())
f.close()

######################ways to create a file##################
#opens a file for writing and creates one if it does not exist
f=open("names_list.txt","w")
f.close()

##creates the specified file but returns an error if the file exist
if not os.path.exists("dave.txt"):
    f=open("dave.txt","x")
    f.close

######################delete a file################
##avoid an error if it does not exist
if os.path.exists("names_list.txt"):
    os.remove("names_list.txt")
else:
    print("file does not exist")

with open("morenames.txt") as f:
    content = f.read()

with open("names.txt","w") as f:
    f.write(content)