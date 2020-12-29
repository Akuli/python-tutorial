"""Make a programme to get a pyramid like shown in the OUTPUT section where user can type the number of rows needed"""
'''
OUTPUT when rows is equal to 5
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5'''

rows=int(input("Type the number of rows needed:"))#gets the number of rows from the user

for row in range(1, rows + 2): #finds the row from rows' variable
    for column in range(row,rows+1, 1): # this is actually the column where a number has to be added
        print(column, end=' ')# this is where the number is printed into rows
    print()#creates a new line for the next row

