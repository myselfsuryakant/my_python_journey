name=str(input('Enter you name: '))
name= name.lower()
vowel_count = 0
vowels = "aeiou"
for char in name:
    if char in vowels:
        vowel_count = vowel_count + 1
print('The name',name,'has',vowel_count,'vowels')