list1 = (1, 2, 3, 4, 5, 9)
list2 = (3, 4, 5, 6, 7, 8)

method_set = len(set(list1) & set(list2))
print("Кількість унікальних елементів ", method_set)
