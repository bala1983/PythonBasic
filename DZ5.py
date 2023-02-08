chet = 0
nechet = 0
counter = 0
summa = 0
while True:
    number = int(input('Введить ціле число'))
    summa += number

    if number % 2 == 0:
        nechet += 1
    if number / 2 == 0:
        chet += 1
    if number == 0:
        break

print(chet, nechet, summa)
