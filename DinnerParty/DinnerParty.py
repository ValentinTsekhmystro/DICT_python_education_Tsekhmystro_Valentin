number_of_friends = int(input('Enter the number of friends joining (including you):\n'))

if number_of_friends < 1:
    print('No one is joining for the party')
    exit()
payments = {}
print('Enter the name of every friend (including you), each on a new line:')
for _ in range(number_of_friends):
    name = input()
    payments[name] = 0

total_amount = int(input("Enter the total amount:\n"))
a = round(total_amount / number_of_friends, 2)
for name in payments:
    payments[name] = a
print(payments)