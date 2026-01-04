import pulp

model = pulp.LpProblem("Drink_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + juice, "Maximize_total_drinks"

model += 2 * lemonade + 1 * juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "Lemon_juice"
model += 2 * juice <= 40, "Fruit_puree"

model.solve()

print("Status:", pulp.LpStatus[model.status])
print("Lemonade:", lemonade.value())
print("Fruit juice:", juice.value())
print("Total drinks:", lemonade.value() + juice.value())