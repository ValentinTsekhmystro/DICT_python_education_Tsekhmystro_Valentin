number_of_friends = int(input())
print('Enter the number of friends joining (including you):')


if number_of_friends < 1:
    print('No one is joining for the party')
    exit()

payments = {}
print('Enter the name of every friend (including you), each on a new line:')

for _ in range(number_of_friends):
    name = input()
    payments[name] = 0

print(payments)