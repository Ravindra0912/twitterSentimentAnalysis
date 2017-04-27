class hello:
    def __init__(self):
        self.n=5

    def increment(self):
        self.n = self.n +1

h =hello()
class bye(hello):
    print(h.n)
    def decrement(self):
        h.n = h.n+1

b = bye()
h.increment()
b.decrement()
print(h.n)