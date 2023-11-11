# Design a vowel eater!
# - A for loop
# - The concept of conditional execution (if-elif-else)
# - The continue statement.
# - Ask the user to enter a word; use user_word = user_word.upper() to convert the word entered by
#  the user to upper case
# - use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U
# from the inputted word;
# Print the uneaten letters to the screen, each one of them on a separate line.

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        print(letter)
        