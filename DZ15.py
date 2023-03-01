buh = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

# for zakaz in buh:
#     summa = zakaz[2]*zakaz[3]
#     if summa < 100:
#         summa += 10
#     print("Order number: ", zakaz[0], "Price: ", round(summa, 2))

summa = list(map(lambda zakaz: ("Order number: ", zakaz[0], "Price: ",
                                round(zakaz[2]*zakaz[3] if zakaz[2]*zakaz[3] >= 100
                                      else zakaz[2]*zakaz[3] + 10, 2)), buh))
print(summa)
