# text = "Hello there thanks for trying my Kata"
text = input("Введіть рядок: ")


def hesh(text):
    if not text:
        raise AttributeError("text must be")
        # return "str"
    if len(text) > 140:
        return False
    words = text.split()
    words1 = [a.capitalize() for a in words]
    words2 = "#" + "".join(words1)
    return words2


print(hesh(text))
