# GitHub.com/AliRezaJoodi

import budget
from unittest import main

food = budget.Category("Food")
food.deposit(100, "Initial deposit")
food.withdraw(11.31, "Apple")
food.withdraw(21.22, "Restaurant")
#print("Balance for food: ", food.get_balance())
#print(food.ledger[1])
#print(food.ledger[2])

clothing = budget.Category("Clothing")
clothing.deposit(100, "Initial deposit")
clothing.withdraw(25.55, "T-shirt")
clothing.withdraw(100, "Jacket")  # Unsuccessful withdraw
#print("Balance for clothing: ", clothing.get_balance())

car = budget.Category("Car")
car.deposit(100, "Initial deposit")
food.transfer(50, car)
car.withdraw(15, "car wash")
#print("Balance for auto: ", auto.get_balance())

print("\n")
print(food)
print(clothing)
print(car)

print(budget.create_spend_chart([food, clothing, car]))

main(module='test_module', exit=False)  # Run unittests
