# This program counts sum of all the natural numbers which has been entered by the user

n = int(input("Enter a positive integer: ")) # Taking user input
sum = 0 # This will be the sum, initialized by 0 because in the begining, sum must be 0
current_number = 1 # This will calculate the number of counts

while current_number <= n:
    sum = sum + current_number
    current_number += 1

print('The sum of all the positive integers till',n,'is: ',sum)