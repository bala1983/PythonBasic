number = int(input('Enter the number:'))
kvadrat = 0
while kvadrat ** 2 < number:
    kvadrat += 1
    if kvadrat **2 <= number:
        print(kvadrat, end = ' ')
