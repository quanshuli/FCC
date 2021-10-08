# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:35:21 2021

@author: peace
"""

# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main
'''
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(101.5, "withdraw")
#food.withdraw(15.89, "withdraw")
#print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(500,"initial deposit")
clothing.withdraw(255.5)
#clothing.withdraw(100)

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(800)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
'''
# Run unit tests automatically

main(module='test_module', exit=False)