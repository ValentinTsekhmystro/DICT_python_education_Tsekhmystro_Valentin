import random

print("HANGMAN")
my_list = ("python", "java", "javascript", "php")
my_word = random.choice(my_list)
remember_letters =[]
all_letters = list(set(my_word))
word = "".join([i if i in remember_letters else "_" for i in my_word])
print(word)
life = 8
while life > 0:
    letter = input("Input a letter:")
    if letter in my_word and letter not in remember_letters:
        remember_letters.append(letter)
        all_letters.remove(letter)
    elif letter in remember_letters:
        print("No improvements")
        life -= 1
    else:
        print("That letter doesn't appear in the word")
        life -= 1
    word = "".join([i if i in remember_letters else "_" for i in my_word])
    print(word)
    if len(all_letters) == 0:
        print("You guessed the word!\nYou survived!")
        break

if len(all_letters) > 0:
    print("You lost!")
