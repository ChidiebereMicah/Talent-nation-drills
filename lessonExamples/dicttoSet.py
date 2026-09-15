supermarket = {
    "Rice": 25000,
    "Beans": 18000,
    "Milk": 3500,
    "Bread": 2000,
    "Eggs": 4500,
    "Sugar": 3000,
    "Salt": 1000,
    "Cooking Oil": 7000,
    "Pasta": 2500,
    "Tomatoes": 3000,
    "Potatoes": 4000,
    "Onions": 2500,
    "Chicken": 12000,
    "Beef": 15000,
    "Fish": 8000,
    "Cheese": 6000,
    "Cereal": 5500,
    "Biscuits": 2000,
    "Juice": 3500,
    "Water": 1000
}

# low_budget = {supermarket.key() in supermarket if supermarket.values() <= 2000}
# print(low_budget)

print(supermarket['Rice'])
low_budget1 = {key for key in supermarket if supermarket[key] <= 2000}

print(low_budget1)

#to_buy = ["buy" if supermarket[key] <= 2000 else "forget" for key in supermarket]
#print(to_buy)
# print(low_budget2)

valuation = {key:["expensive", supermarket[key]] if supermarket[key] > 2000 else ("cheap",supermarket[key]) for key in supermarket}
#print(valuation)

valuation2 = {key:f'expensive, {supermarket[key]}' if supermarket[key] > 2000 else f'cheap,{supermarket[key]}' for key in supermarket}
print(valuation2)

extract = {key:valuation[key][1] for key in valuation}
print('\n\n\n')
print(extract)