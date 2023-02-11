number = int(input('Введить1 ціле число: '))
average = 0
counter = 0
summa = 0
chet = 0
ne_chet = 0
min_value = number

while True:
    if number < min_value:
        min_value = number
    number = int(input('Введить ціле число: '))
    if number == 0:
        break
    counter += 1
    summa += number
    average = summa / counter

    if number % 2 == 0:
        chet += 1
    if number % 2 != 0:
        ne_chet += 1


print(f'Тут відоброжаються результати:  {chet}, {ne_chet}, {summa}, {average}, {min_value}')
