name = str(input("Enter your name sir: "))
age = int(input("Enter your age: "))
if(age>18 and age<100):
    print(name,'You can Drive Sir')
elif(age == 18):
    print(name,'Happy Birthday, we will wait for you till you\'re 18')
elif(age<18):
    print(name,'Sir, you cannot drive!')
elif(age<=0):
    print(name,'First, you need to get out of your mom')
elif(age>=100):
    print(name,'You should be resting in your grave Sir')
