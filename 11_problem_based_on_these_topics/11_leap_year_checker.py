'''
As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

    if the year number isn't divisible by four, it's a common year;
    otherwise, if the year number isn't divisible by 100, it's a leap year;
    otherwise, if the year number isn't divisible by 400, it's a common year;
    otherwise, it's a leap year.

Look at the code in the editor – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

Test your code using the data we've provided.

Sample input: 
Expected output: 

2000
Leap year

2015
Common year

1999
Common year

1996
Leap year

1580
Not within the Gregorian calendar period
'''

year = int(input("Enter a year: "))
if year < 1582:
	print("Not within the Gregorian calendar period")
elif year%4 != 0: print("Common Year")
elif year%100 != 0: print('Leap Year')
elif year%400 != 0: print('Common Year')
else: print('Leap Year')
	