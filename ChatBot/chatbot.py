print("Hello! My name is DICT_Bot.\nI was created in 2021.")
your_name = input("Please, remind me your name.\n")
print("What a great name you have,", your_name,'!')
print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "that's a good time to start programming!")
a = int(input("Now I will prove to you that I can count to any number you want.\n"))
for i in range(a +1):
    print(str(i) + "!")
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("""1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
while True:
    k = int(input())
    if k == 2:
        print("Completed, have a nice day!\nCongratulations, have a nice day!")
        break
    else:
        print("Please, try again.")