class Buffer:
    def __init__(self):
        self.numbers = []

    # def add(self, *a):
    #     self.numbers += list(a)
    #     while len(self.numbers) >= 5:
    #         print(sum(self.numbers[:5]))
    #         self.numbers = self.numbers[5:]

    def add(self, *a):
        for i in a:
            self.numbers.append(i)
            # print(self.numbers)
            if len(self.numbers) == 5:
                print(sum(self.numbers))
                self.numbers = []

    def get_current_part(self):
        return sum(self.numbers)


if __name__ == "__main__":
    buf = Buffer()
    buf.add(5, 5, 6)
    buf.get_current_part()
    buf.add(1, 11, 5, 8, 6, 4)
    buf.get_current_part()
    buf.add(1, 2)
    buf.get_current_part()
    buf.add(1, 2, 3, 4)
    buf.get_current_part()
    buf.add(15, 24, 45, 89)
    buf.get_current_part()
