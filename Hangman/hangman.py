import random


print("HANGMAN")
my_list = ("python", "java", "javascript", "php")
my_word = random.choice(my_list)
a = input("Guess the word " + my_word[:3] + "_".join(['' for _ in range(len(my_word)-3)]) + ":")
if a == my_word:
    print("You survived!")
else:
    print("You lost!")