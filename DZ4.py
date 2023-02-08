number = int(input('Enter the 3 digit number:'))
n1 = number // 100
n2 = number % 100 // 10
n3 = number % 10
print(n3,n2,n1)