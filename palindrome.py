# 2. Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

# Solution:
# first create a function that takes in an argument "word"
# declare a variable that will hold the reversed word
# use methods .replace() and .lower() to remove whitespace (" ", "") and convert letter to lowercase respectively for accuracy
# used a for loop to iterate through the altered word (withoutSpace) and assign each character to variable (reversedWord) from right to left 
# then the reversedWord is passed to an if statement tp check whether its equal with original word (word) 

def isPalindrome(word):
    reversedWord = ""
    withoutSpace = word.replace(" ", "").lower()
    for char in withoutSpace:
        reversedWord = char + reversedWord
    if reversedWord == withoutSpace:
        return print(f"{word} is a palindrome")
    else:
        return print(f"{word} is not a palindrome")

word = "nuRses run"
isPalindrome(word) 