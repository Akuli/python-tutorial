'''Write  code to count a character from a string without using any built-in methods other than input() and print()'''


string_input = input("Type the string:") #gets the input string
find = input("Type the character you want to find:") #gets the character that has to be found
count = 0

for character in string_input:
    if character == find:
        count +=1

print("The number of time", find, "repeated is", count)