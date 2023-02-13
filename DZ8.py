s = input("Введіть рядок: ")
ch = input("Введіть символ для пошуку: ")
index = -1

while True:
    index = s.find(ch, index + 1)
    if index == -1:
        break
    print(index, end=" ")
