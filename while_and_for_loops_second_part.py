# Design a vowel eater!
# - A for loop
# - The concept of conditional execution (if-elif-else)
# - The continue statement.
# - Ask the user to enter a word; use user_word = user_word.upper() to convert the word entered by
#  the user to upper case
# - use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U
# from the inputted word;
# Assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

word_without_vowels = ""

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)

    
 