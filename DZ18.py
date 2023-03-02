num = int(input("Введить число "))


def expanded_form(num):
    if num <= 0:
        raise ZeroDivisionError("zero division")
        # return "zero division"
    number = str(num)
    if num <= 9:
        return num
    else:
        value = sum(int(i) for i in number)
        return expanded_form(value)


print(expanded_form(num))
