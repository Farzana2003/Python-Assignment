
values = [12, -5, 0, 7, -3, 0, 18, -1]

positive_values = []
negative_values = []
zero_values = []

for value in values:
    if value > 0:
        positive_values.append(value)
    elif value < 0:
        negative_values.append(value)
    else:
        zero_values.append(value)

print("Positive:", positive_values)
print("Negative:", negative_values)
print("Zero:", zero_values)
print("Counts:", len(positive_values), len(negative_values), len(zero_values))