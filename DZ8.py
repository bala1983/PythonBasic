s = input("Введіть рядок: ")
ch = input("Введіть символ для пошуку: ")
count = 0

while True:
    search = s.find(ch, count)
    if search == -1:
        break

    count = search +1
    print(search)


