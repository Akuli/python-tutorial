'''Check if a number is pallindrome by converting it into a string'''


pallindrome_input=input("Type the number to check:") #to get the input from user
pallindrome_check=pallindrome_input[::-1] #Reverses the string



if pallindrome_input==pallindrome_check:
    print(f"This number is a pallindrome")
else:
    print("This number is not a pallindrome")

