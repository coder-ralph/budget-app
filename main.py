# budget app
from budget import Category
from helper import create_spend_chart

food = Category("Food")
food.deposit(1000, "Initial deposit")
food.withdraw(10.15, "Groceries")
food.withdraw(15.89, "Restaurant and more food")
print(food)

clothing = Category("Clothing")
clothing.deposit(500, "Initial deposit")
clothing.withdraw(50.75, "Clothes")
clothing.withdraw(100, "Shoes")
print(clothing)

auto = Category("Auto")
auto.deposit(1000, "Initial deposit")
auto.withdraw(15, "Fuel")
auto.withdraw(150, "Service and maintenance")
print(auto)

print(create_spend_chart([food, clothing, auto]))
