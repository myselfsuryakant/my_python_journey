print("Welcome to the Guess Number Game!")
print('You just need to Guess a number between 0 and 20')
secret_number = 9
guess_str = input("Enter your number: ")
number = int(guess_str)

if(number == secret_number):
    print("Congralatutions! You have guessed the correct number!")
elif(number>secret_number and number <20):
    print('The number is less than what you\'ve thought')
elif(number<secret_number and number >0):
    print('The number is greater than what you\'ve thought')
else:
    print("Apni hadd me reh k number soch na, Lawde!")