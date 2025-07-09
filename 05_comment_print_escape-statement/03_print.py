print("\"This statement is printed in Double Quotes\"")

print('\'This statement is printed in single quotes\'')

print("Hello",'this is Suryakant and my age is',5)
#python automatically puts a space when two or more strings are to be printed and a comma is present

# and if we run the same print function and now we introduce a "sep" into the function
print("Hello",'This is Suryakant and my age is',5,sep=",")
# Output: Hello,This is Suryakant and my age is,5
#now this will put , at the places of spaces.
#sep is a space which we can change according to us

print("Hello",'This is Suryakant and my age is',5,sep=".")
# Output: Hello.This is Suryakant and my age is.5
#this will put a full stop