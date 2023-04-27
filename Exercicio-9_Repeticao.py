numbers = list(range(1, 51))
oddNumbers = []
print(numbers)

for i in numbers:
    if i % 2 == 1:
        oddNumbers.append(i)
print(oddNumbers)