# list1 = [1, 2, 0, 6, 5, 6, 14, 8, 9, 10]
# counter = 0
#
# for num in range(1, len(list1)-1):  # числа
#     if list1[num] > list1[num-1] and list1[num] > list1[num+1]:# num в квадратных скобках становится индектом 1, число которого 2
#         # 1и, это число 2 > 1-1 = 0и, а 0и = 1 and 1+1 =2и, а 2и = 0
#         # 2и, это число 0 > 2-1 = 1и, а 1и = 2 and 2+1 =3и, а 3и = 4
#         # 3и, это число 4 > 3-1 = 2и, а 2и = 0 and 3+1 =4и, а 4и = 5
#         counter += 1
# print("Кількість елементів ", counter)
#
#
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 5
# #1list1 = list1[:k] + list1[k+1:]
# #2b = list1[k]
# #2list1.remove(b)
# #3del list1[k]
# print(list1)
#
#
#
#
# You will be given a sequence of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return:
#
# true if all of the following continents / geographic zones will be represented by at least one developer: 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
# false otherwise.
# For example, given the following input array:
#
# list1 =  [
#   { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
#   { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
#   { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
#   { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
#   { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
#   ]




# s = input('stroka')
# b = input('simvol')
# c = list(s)
#
# for a in range(len(c)):
#     if c[a] == b:
#         print(a)

# В компании было подсчитано, что ее ежегодная прибыль, как правило, составляет 23% от
# общего объема продаж. Напишите программу, которая просит пользователя ввести плановую
# сумму общего объема продаж и затем показывает прибыль, которая будет получена
# от этой суммы.
# Подсказка: для представления 23% используйте значение 0.23.

# god = int(input("Обьём продаж: "))
# procent = 0.23
# pribyl = god*procent
# print(pribyl)


# Расчет площади земельного участка. Один акр земли эквивалентен квадратным метрам.
# Напишите программу, которая просит пользователя ввести общее количество квадратных
# метров участка земли и вычисляет количество акров в этом участке.
# Подсказка: разделите введенное количество на 4047, чтобы получить количество акров.

# metry_kv = int(input("количество квадратных метров: "))
# akr = 4047
# kol_akr = metry_kv/4047
# print(round(kol_akr, 2))

# Налоr с продаж. Напишите программу, которая попросит пользователя ввести величину
# покупки. Затем программа должна вычислить федеральный и региональный налог с продаж.
# Допустим, что федеральный налог с продаж составляет 5%, а региональный - 2.5%.
# Программа должна показать сумму покупки, федеральный налог с продаж, региональный
# налог с продаж, общий налог с продаж и общую сумму продажи (т. е. сумму покупки и
# общего налога с продаж).
# Подсказка: для представления 2.5% используйте значение 0.025, для представления
# 5% - 0.05.

# summa = int(input("ввести величину покупки: "))
# fed = 0.05
# reg = 0.025
# summa_fed = summa * fed
# summa_reg = summa * reg
# summa_fed_reg = summa_reg+summa_fed
# print(summa_fed, summa_reg, summa_fed_reg)


# Классификатор возраста. Напишите программу, которая просит пользователя ввести
# возраст человека. Программа должна определить, к какой категории этот человек принадлежит:
# младенец, ребенок, подросток или взрослый, и вывести соответствующее сообщение.
# Ниже приведены возрастные рекомендации:
# • если возраст 1 год или меньше, то он или она - младенец;
# • если возраст старше l года, но моложе 13 лет, то он или она- ребенок;
# • если возраст не менее 13 лет, но моложе 20 лет, то он или она - подросток;
# • если возраст более 20 лет, то он или она- взрослый.

# vozrast = int(input("ввести возраст: "))
# if vozrast <= 1:
#     print("Младенец ",)
# if 1 < vozrast <= 13:
#     print ("ребенок ")
# if 13 < vozrast <= 20:
#     print("Подросток ")
# else:
#     print("Взрослый ")


# Цвета колеса рулетки. На колесе рулетки карманы пронумерованы от О до 36. Ниже
# приведены цвета карманов:
# • карман О- зеленый;
# • для карманов с 1 по 1 О карманы с нечетным номером имеют красный цвет, карманы
# с четным номером - черный;
# • для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы
# с четным номером - красный;
# • для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы
# с четным номером - черный;
# • для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы
# с четным номером - красный.
# Напишите программу, которая просит пользователя ввести номер кармана и показывает,
# является ли этот карман зеленым, красным или черным. Программа должна вывести
# сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона
# ОТ 0 ДО 36


#nomer_karmana = int(input("ввести номер кармана: "))
# if nomer_karmana == 0:
#     print("Зеленый ",)
# if 1 < nomer_karmana <= 10 and nomer_karmana % 2 == 0:
#     print("Черный ")
# if 1 < nomer_karmana <= 10 and nomer_karmana % 2 != 0:
#     print("Красный ")
# else:
#     print("число лежит вне диапазона, введите число еще раз")
#     nomer_karmana = int(input("ввести номер кармана: "))


# ex = "d"
# while ex == "d":
#     nomer_karmana = int(input("ввести номер кармана: "))
#     if nomer_karmana > 10:
#         print("число лежит вне диапазона, введите число еще раз")
#         ex = input("Для посторного ввода числа нажмите d, или другой любой символ  ")
#
#     if nomer_karmana == 0:
#         print("Зеленый ",)
#     if 1 < nomer_karmana <= 10 and nomer_karmana % 2 == 0:
#         print("Черный ")
#     if 1 < nomer_karmana <= 10 and nomer_karmana % 2 != 0:
#         print("Красный ")

#
# height = int(input("Введите высоту треугольника: "))
#
# for row in range(height):
#     for col in range(height*2-1):
#         if col >= height-1-row and col <= height-1+row:
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     print()
#
# for i in range(height):
#     for x in range(height*2-1):
#         if i == x or i == height*2-2-x or x == height-1:
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     print()
#
#
#
# height = int(input("Введите высоту треугольника: "))
#
#
# for row in range(height):
#     for col in range(height*2-1):
#         if col >= height-1-row and col <= height-1+row:
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     print()
#
#
# for row in range(height-2, -1, -1):
#     for col in range(height*2-1):
#         if col == height-1-row or col == height-1+row:
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     print()


h = int(input("Введить висоту фігури: "))

for i in range(h):
    for x in range(h*2-1):
        if x >= h-1-i and x <= h-1+i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()


for i in range(h-2, -1, -1):
    for x in range(h*2-1):
        if x == h-1-i or x == h-1+i or x == h*2-2-x:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
