print("Hello! My name is DICT_Bot.\nI was created in 2021.")
your_name = input("Please, remind me your name.\n")
print("What a great name you have,", your_name,'!')
print("Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "that's a good time to start programming!")