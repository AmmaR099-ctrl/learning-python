def anagram(str1):
    str1=str1.lower().strip()
    return str1

def count_vowel(strg):
    i=0
    for letter in strg:
        if letter in "aeiou":
            i=i+1
    print (i," vowels in this word. ")

str1=input("enter: ")
str1=anagram(str1)
print(str1)
count_vowel(str1)