temperatures = [29.5, 31.0, None, 33.5, 34.0, 32.0, 35.5,
                36.0, None, 30.5, 28.0, 37.0, 38.0, 34.5]

clean = []

for temp in temperatures:
    if temp is not None:
        clean.append(temp)

mean = sum(clean) / len(clean)

above_mean = []
hot_days = 0

for temp in clean:
    if temp > mean:
        above_mean.append(temp)

    if temp >= 35:
        hot_days += 1

current = 0
longest = 0

for temp in temperatures:
    if temp is not None and temp >= 35:
        current += 1
        if current > longest:
            longest = current
    else:
        current = 0

missing = []

for i in range(len(temperatures)):
    if temperatures[i] is None:
        missing.append(i)

print("Mean:", round(mean, 2))
print("Minimum:", min(clean))
print("Maximum:", max(clean))
print("Above mean:", above_mean)
print("Hot days:", hot_days)
print("Longest hot run:", longest)
print("Missing indices:", missing)