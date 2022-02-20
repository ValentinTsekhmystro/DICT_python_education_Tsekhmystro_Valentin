credit_sum = int(input("Enter the loan principal:\n"))
credit = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:\n""")
if credit in "m":
    m = int(input("Enter the monthly payment:\n"))
    a = credit_sum // m
    print(f"It will take {a} months to repay the loan")
elif credit in "p":
    p = int(input("Enter the number of months:\n"))
    b = credit_sum // p + 1
    c = credit_sum - (p - 1) * b
    if b == c:
        print(f"Your monthly payment = {b}")
    else:
        print(f"Your monthly payment = {b} and the last payment = {c}")