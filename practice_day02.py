def anagram(str1,str2):
    str1=str1.lower().strip()
    str2=str2.lower().strip()
    return str1,str2

def count_vowel(strg):
    i=0
    for letter in strg:
        if letter in "AEIOUaeiou":
            i=i+1
    print (i," vowels in this word. ")

str1=input("enter: ")
str2=input("enter 2: ")
str1,str2=anagram(str1,str2)
print(str1)
count_vowel(str1)