# print('1')
# print('2')
# print('3')
# print('4')
# print('5')
#This will print values from 1 to 5

# Now lets do the same using for loop

for i in range(1, 6): #Here 6 is the range limit hence it will get 5
    print(i)

#Table of n
n=int(input("Enter the number: "))

for i in range(1, 11): # this is the simple code
    print(n*i)

for i in range(1, 11): # this code has table written in human form
    print(n,'x', i, '=', n * (i))