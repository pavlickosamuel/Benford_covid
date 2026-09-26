import csv

counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
total = 0

with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        value = row[5]
        if value == "NA":
            continue  
        first_digit = int(str(abs(float(value)))[0])
        if first_digit in counts:
            counts[first_digit] += 1
            total += 1

for digit, count in counts.items():
    percent = count / total * 100
    print(f"Digit {digit}: {count} ({percent:.1f}%)")