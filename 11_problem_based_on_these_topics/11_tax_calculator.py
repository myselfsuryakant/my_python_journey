'''
Use If-Else Statamemt.
Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

    if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
    if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

Your task is to write a tax calculator.

    It should accept one floating-point value: the income.
    Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code in the editor.

Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.

Look at the code in the editor – it only reads one input value and outputs a result, so you need to complete it with some smart calculations.

Test your code using the data we've provided.
Test data:

Sample input: 
Expected output: 

10000
The tax is: 1244.0 thalers

100000
The tax is: 19470.0 thalers

1000
The tax is: 0.0 thalers

-100
The tax is: 0.0 thalers
'''

income = float(input("Enter the annual income: "))

if income <= 85528:
	tax = (income * 0.18) - 556.02
elif income > 85528:
	surplus = income - 85528
	tax = (surplus * 0.32) + 14839.02
	
if tax < 0: tax = 0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")