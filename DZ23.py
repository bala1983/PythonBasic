class Counter:

    def __init__(self, start, min_value, max_value):
        self.current_value = start
        self.min = min_value
        self.max = max_value

    def min(self, min_value):
        self.min = min_value

    def max(self, max_value):
        self.max = max_value

    def start(self, start):
        self.current_value = start

    def increment(self):
        if self.current_value < self.max:
            self.current_value += 1
        else:
            print("Max Value ", max)

    def current(self):
        return self.current_value


counter = Counter(start=0, min_value=0, max_value=10)
counter.increment()
value = counter.current()
print(value)
