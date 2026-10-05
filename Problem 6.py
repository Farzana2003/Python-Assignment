numbers = [14, 8, 21, 21, 5, 17, 14]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

if len(unique_numbers) < 2:
    print("Fewer than two distinct values are present")
else:
    largest = max(unique_numbers)
    unique_numbers.remove(largest)
    second_largest = max(unique_numbers)

    print("Largest distinct value:", largest)
    print("Second-largest distinct value:", second_largest)