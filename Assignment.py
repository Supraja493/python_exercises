# We have an alphabet (where A is on position 1, B is on position 2, C on position 3... Z on position 26 ?)
# The script is taking a string from the user. and constructing a string with the following idea:
# each letter is repeating "the Amount of times" equal to "the position in the alphabet" and printing the string.
# For example, The input string is "abc", the resulting string should be "abbccc".
# The input string "ef", the resulting string is "eeeeeffffff".


#input from user
string = input("Enter a string: ")

#for loop to access into each element of the string
for i in string:
    # The element in the string should be alphabet
    #if(i >= 'A' and i <= 'Z'):
    if(i.isupper()):
        # print(ord(i) - ord('A'))
        # size gives the position of alphabet in alphabetics
        size = (ord(i) - ord('A')) + 1
        #to print the element size times 
        for j in range(size) :
            print(i,end="")
    
    #this is for lower letters
    
    #elif(i >= 'a' and i <= 'z'):
    elif(i.islower()):
        size = (ord(i) - ord('a')) + 1
        for j in range(size) :
            print(i,end="")
    #if other than alphabets just print space 
    else:
        print(" ",end="")
print("",end="\n")







    
