items = ["pen", "book", "pen", "bag", "book", "ruler", "pen"]

unique_items = []
repeated_occurrences = []

for item in items:
    if item in unique_items:
        repeated_occurrences.append(item)
    else:
        unique_items.append(item)

print("Unique items:", unique_items)
print("Repeated occurrences:", repeated_occurrences)