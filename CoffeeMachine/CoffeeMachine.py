water = 200
milk = 50
coffee = 15
has_water = int(input("Write how many ml of water the coffee machine has:\n"))
has_milk = int(input("Write how many ml of milk the coffee machine has:\n"))
has_coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
need_cup_coffee = int(input("Write how many cups of coffee you will need:\n"))
cup_coffee = min([has_water // water, has_milk // milk, has_coffee // coffee])
if cup_coffee == need_cup_coffee:
    print("Yes, I can make that amount of coffee")
elif cup_coffee > need_cup_coffee:
    print(f'Yes, I can make that amount of coffee (and even {cup_coffee - need_cup_coffee} morethan that)')
else:
    print(f"No, I can make only {cup_coffee} cups of coffee")