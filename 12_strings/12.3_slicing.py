name = "Suryakant"
print(name[0:3])
# Output will be Sur
# Just like the range function which goes from starting to n-1
# slicing also goes uptil n-1 

print(name[2:-1])
print(name[2:8])
# These will give same output

age = "Surya0123456789"
print(age[0])  # Output: S
print(age[0:10]) # Ouput: Surya01234
print(age[0:10:2]) # Output: Sra13
# print(age[0:10:n-1]) 
# This last line has an additional :2, this implies that n-1 characters will be skipped.
# so, in output Sra13, u,y,0,2,4 has been skipped
print(age[0:10:3]) # This will skip n-1 = 3-1 = 2 characters

print(name[:9]) # This will replace first empty character with 0
print(name[1:]) # This will replace last empty character with length