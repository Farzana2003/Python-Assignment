marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]

valid_marks = []

A = 0
B = 0
C = 0
F = 0

for mark in marks:
    if mark < 0 or mark > 100:
        continue

    valid_marks.append(mark)

    if mark >= 80:
        A += 1
    elif mark >= 70:
        B += 1
    elif mark >= 60:
        C += 1
    else:
        F += 1

average = sum(valid_marks) / len(valid_marks)

print("Valid marks:", valid_marks)
print("Grade counts: A =", A, ", B =", B, ", C =", C, ", F =", F)
print("Average:", format(average, ".2f"))
print("Highest:", max(valid_marks))
print("Lowest:", min(valid_marks))