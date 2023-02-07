while True:
    user_input = input('Введить ціле число')
    if not user_input.isdigit():
        print("Ви ввели не ціле число, спробуйте ще раз")
    elif user_input == '0':
        break

