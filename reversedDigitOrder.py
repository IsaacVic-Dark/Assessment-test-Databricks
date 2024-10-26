# 4. Write a program that takes an integer as input and returns an integer with 
# reversed digit ordering.
# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

# Solution:
# first i prompt a user to enter an integer to be reversed
# then i create a function to perform the reversal 
# inside the function i declare an empty variable to hold the reverse string which is just the number converted to a string using the str() built-in function 
# then i check whether the integer is a negative number if it is i convert it to  string and use the abs() func to ignore the negative symbol
# then i use a for loop to iterate over the string from the last character to the first character
# then i convert the string back to an integer and negate it
# then repeat the same procedure for a positive num but without the abs() func and negating the number

num = int(input("Enter an integer: "))

def reversedDigitOrder(num):
    reversedDigit = ""
    if num < 0:
        number = str(abs(num))
        for x in number:
            reversedDigit = x + reversedDigit
        reversedDigit = int(reversedDigit)
        return print(-reversedDigit)
    else:
        number = str(num)
        for x in number:
            reversedDigit = x + reversedDigit
        reversedDigit = int(reversedDigit)
        return print(reversedDigit)

    
reversedDigitOrder(num)