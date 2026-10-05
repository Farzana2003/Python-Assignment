scores = [
    [78, 82, 91],
    [65, 70, 68],
    [90, 88, 94],
    [55, 61, 58]
]

averages = []
passes = 0

for i in range(len(scores)):
    total = 0

    for score in scores[i]:
        total += score

    average = total / 3
    averages.append(average)

    print("Student", i, "Total:", total, "Average:", round(average, 2))

    if average >= 60:
        passes += 1

highest = max(averages)
highest_index = averages.index(highest)

print("Passing students:", passes)
print("Highest average student index:", highest_index)