'''Write a code to remove the vowels and return a blank space inplace of it in a uer given string'''

input_string=input("Type the string:")
new_string= "" #intialises the new string

for character in input_string: #takes each character from the string
    if character not in "aeiouAEIOU":
        new_string= new_string + character #As the character found is not a vowel it is added to the new string

print(new_string)