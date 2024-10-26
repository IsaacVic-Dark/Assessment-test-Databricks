# 3. Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"

# Solution:
# first i declare a function "isPangram" then pass in the the variable containing the word/sentence to be checked
# declare a variable to hold the letters of the alphabet and change the sentence/word to lowercase
# used a for loop to iterate over alphabet and inside the loop an if statement to check whether the current letter exists in the word/sentence
# if the loop completes without any missing letters it returns a print statement showing that the word/sentence is a pangram

def isPangram(sentence):
    alphabet = "qwertyuioplkjhgfdsazxcvbnm"
    sentence = sentence.lower()
    
    for letter in alphabet:
        if letter not in sentence:
            return print(f"'{sentence}', not pangram")
    
    return print(f"'{sentence}', is pangram")

sentence = "The quick brown fox jumps over the lazy dog"
isPangram(sentence)

