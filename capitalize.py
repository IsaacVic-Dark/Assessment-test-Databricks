# 5. Write a program that accepts a string as input, capitalizes the first letter of each 
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

# Solution:
# declare a variable "word" to store user input
# define a func and accept "word" as an argument 
# declare a variable to hold the modified "word" and a boolean variable "capitalize" to set to true after a whitespace
# iterate over the word and check if the "capitalize" is true, if true, capitalize the first letter, if false, check for whitespace then append the whitespace and set the "capitalize" to True, if no whitespace append the character as it 
# return the modified word "cap"


word = str(input("Enter a word or sentence to capitalize: "))

def capitalizeFirstLetter(word):
    cap = ""
    capitalize = True
    for char in word:
        if capitalize:
            cap += char.upper()
            capitalize = False
        elif char == " ":
            cap += char
            capitalize = True
        else:
            cap += char
    return print(f"'{cap}', is capitalized")


capitalizeFirstLetter(word)
