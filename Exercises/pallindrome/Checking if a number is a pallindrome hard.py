'''This method is a little hard.It checks if a number is directly if a number is a  pallindrome without converting it into a string'''


user_input=int(input("Type the number to check:")) #gets the input from the user
store=user_input #stores the input variable in another variable
reversed = 0 #initialises the reversed variable so that the number(user_input) can be reversed later

while user_input!=0:
    digit= user_input % 10 #takes the reminder to get the last digit as it is divided by 10
    reversed= reversed * 10 + digit
    user_input= user_input // 10 #takes the quotient to get the other digits other than the last digit which was aldready added



if store==reversed:
    print(f"This number is a pallindrome")
else:
    print("This number is not a pallindrome")

