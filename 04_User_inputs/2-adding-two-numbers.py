# a = input("Enter a number: ")
# print(a+3) #This should print the summation of number and 3

# Output: TypeError: can only concatenate str (not "int") to str
# This is because, python is treating a as string
# So we have to typecast a into an integer

a = input("Enter a number: ")
a = int(a)
print("The summation: ",a + 3)

# Now, this is correct way