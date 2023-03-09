import random

stroka = int(input('Введіть кількість рядків '))
stolbets = int(input('Введіть кількість колонок '))

matrix_MN = [[random.randint(10, 51) for i in range(stolbets)] for j in range(stroka)]

summa_stroka = []
for i in range(stroka):
    summ_stroka = 0
    for j in range(stolbets):
        summ_stroka += matrix_MN[i][j]
    summa_stroka.append(summ_stroka)

summa_stolbets = []
for i in range(stolbets):
    summ_stolbets = 0
    for j in range(stroka):
        summ_stolbets += matrix_MN[j][i]
    summa_stolbets.append(summ_stolbets)

for i in range(stroka):
    for j in range(stolbets):
        print("{:<4}".format(matrix_MN[i][j]), end=" ")
    print("{:<4}".format(summa_stroka[i]))

for i in range(stolbets):
    summ_stolbets = summa_stolbets[i]
    print("{:<4} ".format(summ_stolbets), end="")
