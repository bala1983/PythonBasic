#beg = 4.2
#for minets in range(10, 31, 1):
#    kalories = beg * minets
#    print((round(kalories, 2)))

#Сожженные калории. Бег на беговой дорожке позволяет сжигать 4,2 калорий в минуту.
#Напишите программу, которая применяет цикл для вывода количества калорий, сожженных после 10, 15, 20, 25 и 30 минут бега.


num = int(input("type1 num:"))

min_value = num

while True:
    if num < min_value:
        min_value = num
    num = int(input("type num:"))
    if num == 0:
        break

print("Min value:", min_value)