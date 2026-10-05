numbers = [4, 7, 2, 7, 9, 7, 1]
target = 7

positions = []

for i in range(len(numbers)):
    if numbers[i] == target:
        positions.append(i)

for i in range(len(numbers)):
    if numbers[i] == target:
        first_occurrence = i
        break

print("Target:", target)
print("Positions:", positions)
print("Number of occurrences:", len(positions))

if first_occurrence is not None:
    print("First occurrence:", first_occurrence)
else:
    print("First occurrence: Not found")