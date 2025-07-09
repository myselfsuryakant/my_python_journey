name = "Suryakant" #string, "name" is variable name and Suryakant is the value it stores in " " and value is a string
age = 23 #integer, 23 is the value stores in variable age storing value 23 
cgpa = 8.99 #float 8.99 is the value stored in cgpa

# = is the assignment operator used to assign value to the variable

'''
Rules of defining a variable name
1. Variable name must start with an alphabet (a,z) (A,Z) or underscore(_)
variable names are case sensitive Age and age are different
python keywords cannot be used as variable names(if, for, while)
'''

# 32age = 45 invalid because variable name cannot start with a number
# age = 32 is valid
# a@ge = 42 is invalid
# _age = 32 is valid

print(name)
print(type(name)) #this tells us the data type of variable "name"
print(age)
print(type(age))
print(cgpa)
print(type(cgpa))