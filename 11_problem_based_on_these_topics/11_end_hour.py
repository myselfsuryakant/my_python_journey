'''
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
Hint: using the % operator may be the key to success.

test data: 
Input:                                       Output:
12                                           13:16
17
59

23                                           10:40
58
642

0                                            1:0
1
2939

'''
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

if(hour>24):
    print("Please give valid hour")
    
if(mins>60):
    print("Please give valid minute")
    

a = dura/60
h = int(a)

b = dura%60
m = int(b)

end_hour = hour + h
end_min = mins + m

while end_min >= 60:
    end_hour += 1
    end_min -= 60

while end_hour > 24:
    end_hour -= 24

print("End = ",end_hour,":",end_min,sep="")