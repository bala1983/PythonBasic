k1 = int(input("Введить кількість учнів у класі №1:"))
k2 = int(input("Введить кількість учнів у класі №2:"))
k3 = int(input("Введить кількість учнів у класі №3:"))
p = int(2)  # Кількість учнів за однією партою
print("Кількість учнів у всіх класах", k1 + k2 + k3)
print("Кількість парт для всіх учнів", ((k1 + k2 + k3) // p + (k1 + k2 + k3) % p))
