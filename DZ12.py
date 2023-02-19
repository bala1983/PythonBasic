text = "У єдиному У рядку У записаний текст текст текст"
words = text.split()
slovar = {}
for word in words:
    if word in slovar:
        slovar[word] += 1
    else:
        slovar[word] = 1

print(slovar)
