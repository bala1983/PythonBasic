number = int(input('Введить ціле число окрім 0: '))
average = 0
counter = 0
summa = 0
chet = 0
ne_chet = 0
min_value = max_value = number

while True:
    if number == 0:
        break
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number
    counter += 1
    summa += number
    average = summa / counter

    if number % 2 == 0:
        chet += 1
    if number % 2 != 0:
        ne_chet += 1
    number = int(input('Введить ціле число: '))
print(f'Тут відоброжаються результати:  {chet}, {ne_chet}, {summa}, {average}, {min_value}, {max_value}')
