class Counter:

    def __init__(self, start, min_value, max_value):
        self.start_value = start
        self.min = min_value
        self.max = max_value

    def min(self, min_value):
        self.min = min_value

    def max(self, max_value):
        self.max = max_value

    def start(self, start):
        self.start_value = start

    def increment(self):
        if self.start_value < self.max:
            self.start_value +=1
        else:
            print("Max Value ", max)

    def rotation(self):
        return self.start_value


counter = Counter(start=0, min_value=0, max_value=10)
counter.increment()
value = counter.rotation()
print(value)
