s1='Hai Abhinandhan'
d1={}
for word in s1:
    for letter in word:
        s=d1.keys()
        if letter in s:
            d1[letter]=d1[letter]=d1[letter]+1
        else:
            d1[letter]=1
print("Character frequency is:",d1)