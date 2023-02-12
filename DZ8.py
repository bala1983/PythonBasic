s = input("Введіть рядок:")
ch = input("Введіть символ:")
count = 0
while True:
    search = s.find(ch, count)
    count += 1
    print(s, ch)
    break

