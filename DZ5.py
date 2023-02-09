average = 0
counter = 0
summa = 0
chet = 0
nechet = 0

while True:
    number = int(input('Введить ціле число: '))
    if number == 0:
        break
    counter += 1
    summa += number
    average = summa / counter

    if number % 2 == 0:
        chet += 1
    if number % 2 != 0:
        nechet += 1


print(f'Тут відоброжаються результати:  {chet}, {nechet}, {summa}, {average}')

