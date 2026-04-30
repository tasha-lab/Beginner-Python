# String
# literal assignment
first = "Tasha"
last = "Wanjiku"
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
pizza = str("peperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)
# casting a number to a string
decade = "1980s"
decade1 = str(1980)

print(type(decade))
print(type(decade1))
# multiple lines
multiline = """
hey!
    uko aje 


         bye
"""

print(multiline)

# escaping special characters
sentence = "i'm well"
print(sentence)

# string methods
print(first)
print(first.upper())
print(first.lower())
print(first)

print(multiline)
print(multiline.title())
print(multiline.replace("hey", "hello"))
print(multiline)

print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("")

# building a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("muffin".ljust(16, ".") + "$5".rjust(4))
print("chocolate".ljust(16, ".") + "$8".rjust(4))
print("tea".ljust(16, ".") + "$2".rjust(4))
print("juice".ljust(16, ".") + "$4".rjust(4))
print("")

# string value index
print(first[1])
print(first[-1])  # last letter
print(first[2])
print(first[0:])  # includes the last digit or data
print("")

# some methods that return boolean data
print(first.startswith("T"))
print(first.endswith("T"))
print(first.endswith("a"))

# boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# complex type
comp = 5 + 3j
print(type(comp))
print(comp.real)
print(comp.imag)

# built in functions
gpa = 3.42
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print(round(gpa, 4))

#casting a string to an integer
zipcode = 10001
zip_value = int(zipcode)
print(type(zip_value))



