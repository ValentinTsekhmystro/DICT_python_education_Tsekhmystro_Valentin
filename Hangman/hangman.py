import random


print("HANGMAN")
my_list = ("python", "java", "javascript", "php")
a = input("Guess the word:")
if a == random.choice(my_list):
    print("You survived!")
else:
    print("You lost!")