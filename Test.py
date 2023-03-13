import random

M = int(input("Введіть значення М: "))


def sort_matrix(M):
    if M < 6:
        raise ValueError("Введіть значення М ")

    matrix = [[random.randint(10, 50) for j in range(M)] for i in range(M)]
    print("До сортування:")
    for row in matrix:
        print(row)

    column_sums = [0] * M
    for i in range(M):
        for j in range(M):
            column_sums[j] += matrix[i][j]
    print(column_sums)

    for j in range(M):
        if j % 2 == 0:
            column = [matrix[i][j] for i in range(M)]
            column.sort()
            for i in range(M):
                matrix[i][j] = column[i]
        else:
            column = [matrix[i][j] for i in range(M)]
            column.sort(reverse=True)
            for i in range(M):
                matrix[i][j] = column[i]

    print("Після сортування:")
    for row in matrix:
        print(row)
    print(column_sums)


sort_matrix(M)
