items = ["Notebook", "Pen", "Calculator", "Folder"]
prices = [120.0, 15.0, 850.0, 80.0]
quantities = [2, 5, 1, 3]

subtotal = 0

for i in range(len(items)):
    total = prices[i] * quantities[i]
    print(items[i], ":", format(total, ".2f"))
    subtotal = subtotal + total

if subtotal >= 1000:
    discount = subtotal * 0.10
elif subtotal >= 500:
    discount = subtotal * 0.05
else:
    discount = 0

if subtotal - discount >= 1000:
    delivery = 0
else:
    delivery = 60

final_total = subtotal - discount + delivery

print("Subtotal:", format(subtotal, ".2f"))
print("Discount:", format(discount, ".2f"))
print("Delivery charge:", format(delivery, ".2f"))
print("Final total:", format(final_total, ".2f"))