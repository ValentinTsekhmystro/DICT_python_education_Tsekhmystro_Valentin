amount = float(input())
xchange_rates = [0.82, 0.17, 1.9622, 0.208]
print(f'I will get {round(amount * xchange_rates[0], 2)} ARS from the sale of {amount} conicoins.')
print(f'I will get {round(amount * xchange_rates[1], 2)} HNL from the sale of {amount} conicoins.')
print(f'I will get {round(amount * xchange_rates[2], 2)} AUD from the sale of {amount} conicoins.')
print(f'I will get {round(amount * xchange_rates[3], 2)} MAD from the sale of {amount} conicoins.')