readings = [21.5, None, 24.0, 31.2, -4.0, 28.5, None, 35.1]

clean_readings = []
alerts = []

for reading in readings:
    if reading is None or reading < 0 or reading > 50:
        continue

    clean_readings.append(reading)

    if reading > 30:
        alerts.append(reading)

average = sum(clean_readings) / len(clean_readings)

print("Clean readings:", clean_readings)
print("Average:", round(average, 2))
print("Alerts:", alerts)