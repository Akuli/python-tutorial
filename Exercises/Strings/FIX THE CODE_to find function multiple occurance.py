'''fix the code'''
'''The programme must be able to find all the occurances of a sub-string and something prevents it'''

'''OUTPUT
>>>Type the string:asasa
>>>Type the character/word you want to find the occurance:asa
>>>The index of the occurance is/are {0, 2} repeating 2 times

Here as you can see this finds asa from asasa twice, even though after the first asa, 
only sa is left and that does not contain another asa. 
So,correct the code
'''


input_string = input("Type the string:")
find = input("Type the character/word you want to find the occurance:")
start=0
n=len(input_string) #gets the length of the string
count=set() #intialsies a set to get the substrings' index


for i in range(0,n+1):
    x=input_string.find(find, i)

    if x !=-1:
        count.add(x)


if len(count)==0:
    print("Sorry no occurances found")
else:

  print("The index of the occurance is/are",count,"repeating",len(count),"times")
