name = "Suryakant"
print(name[0]) # Output: S
print(name[-1]) # Output: t, -1 will give last element
# This program will print 0 index of this string

'''
 S  u  r  y  a  k  a  n  t
 0  1  2  3  4  5  6  7  8
-9 -8 -7 -6 -5 -4 -3 -2 -1

'''
print(name[-6])

# it is hard to play around negative index so I would recommend you to convert them into positive index. 
'''
How?
Add the length of your string to the negative index and you will have your positive index ready
'''

print(name[-3]) 
print(name[6]) # name[-3] = name[-3 + 9] = name[6]
# Both will give "a" as output