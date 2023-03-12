import random

M = int(input('Введіть матрицю МхМ '))


def sort_matrix(M):
    if M < 6:
        raise ValueError("Введіть матрицю МхМ ")

    random_numbers = [[random.randint(10, 50) for i in range(M)] for j in range(M)]
    summa_of_stolb = [sum(column) for column in zip(*random_numbers)]


    print("До сортування")
    for row in random_numbers:
        for element in row:
            print("{:<4}".format(element), end="")
        print("")
    for q in summa_of_stolb:
        print("{:<4}".format(q), end="")


    summa_dict = {}
    for j in range(M):
        summa_dict[j] = summa_of_stolb[j]


    sorted_summa_dict = {}
    for i in range(M):
        min_key = min(summa_dict, key=summa_dict.get)
        sorted_summa_dict[min_key] = summa_dict.pop(min_key)


    sorted_numbers = [[random_numbers[i][j] for j in sorted_summa_dict.keys()] for i in range(M)]


    for j in range(M):
        if j % 2 == 0:
            for i in range(1, M):
                key_item = sorted_numbers[i][j]
                k = i - 1
                while k >= 0 and sorted_numbers[k][j] < key_item:
                    sorted_numbers[k + 1][j] = sorted_numbers[k][j]
                    k -= 1
                sorted_numbers[k + 1][j] = key_item
        else:
            for i in range(1, M):
                key_item = sorted_numbers[i][j]
                k = i - 1
                while k >= 0 and sorted_numbers[k][j] > key_item:
                    sorted_numbers[k + 1][j] = sorted_numbers[k][j]
                    k -= 1
                sorted_numbers[k + 1][j] = key_item



    print("\nПісля сортування")
    for row in sorted_numbers:
        for element in row:
            print("{:<4}".format(element), end="")
        print("")
    for q in sorted_summa_dict.values():
        print("{:<4}".format(q), end="")


sort_matrix(M)
