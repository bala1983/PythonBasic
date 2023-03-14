# from random import randint
#
#
# cols = int(input("Введіть значення М: "))
# rows = cols
#
# matrix = [[randint(1, 10) for _ in range(cols)] for _ in range(rows)]
#
#
# def print_matrix(custom_matrix):
#     # if M < 6:
#     #     raise ValueError("Введіть значення М ")
#
#     for col in range(cols):
#         for row in custom_matrix:
#             print(f"{row[col]:<2}", end=" ")
#         print()
#
#
# print_matrix(matrix)
#
# sum_list = []
# for row_list in matrix:
#     sum_val = 0
#     for i in row_list:
#         sum_val += i
#     sum_list.append(sum_val)
#
# print(*sum_list)
#
#
# #
# def bubble_sort(list_to_sort):
#     for _ in range(0, len(list_to_sort) - 1):
#         for x in range(0, len(list_to_sort) - 1):
#             if list_to_sort[x] > list_to_sort[x + 1]:
#                 list_to_sort[x], list_to_sort[x + 1] = list_to_sort[x+1], list_to_sort[x]
#     return list_to_sort
#
#
# matrix_sorted = [bubble_sort(matrix[i]) if i % 2 == 0 else matrix[i] for i in range(len(matrix))]
#
# print_matrix(matrix_sorted)
# # print("\t".join([str(x) for x in sum_list]))
# print(*sum_list)
