list1 = [1, 2, 0, 6, 5, 6, 14, 8, 9, 10]
counter = 0

for num in range(1, len(list1)-1):
    if list1[num] > list1[num-1] and list1[num] > list1[num+1]:
        counter += 1
print("Кількість елементів ", counter)
