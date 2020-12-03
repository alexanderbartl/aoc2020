with open('input.txt') as f:
    numbers = [int(line) for line in f.readlines()]

for i, number1 in enumerate(numbers):
    for number2 in numbers[i:]:
        if number1 + number2 == 2020:
            print(number1, number2, number1 * number2)

for i, number1 in enumerate(numbers):
    for j, number2 in enumerate(numbers[i:]):
        if number1 + number2 > 2020:
            continue
        for number3 in numbers[i + j:]:
            if number1 + number2 + number3 == 2020:
                print(number1 * number2 * number3)