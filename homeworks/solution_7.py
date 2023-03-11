import random
import time


class Sort:

    def __init__(self, n):
        self.n = n
        self.a = []
        self.b = []
        self.asg = 0
        self.cmp = 0

    def set_random(self):
        self.a = [random.randint(0, 9) for _ in range(self.n)]

    @staticmethod
    def timed(func):
        def _timed(self, ):
            bt = time.monotonic()
            func(self, )
            elapsed = time.monotonic() - bt
            print(round(elapsed, 4))

        return _timed

    @timed
    def shell_sort(self):
        a = self.a.copy()

        h = self.n // 2
        while h > 0:
            for i in range(h, self.n):
                t = a[i]
                j = i
                while j >= h and a[j - h] > t:
                    a[j] = a[j - h]
                    j -= h
                a[j] = t
            h = h // 2

        self.b = a

    @timed
    def insertion_sort(self):
        a = self.a.copy()

        for j in range(0, self.n):
            for i in range(0, j)[::-1]:
                self.cmp += 1
                if a[i] < a[i + 1]:
                    break
                self.asg += 2
                a[i], a[i + 1] = a[i + 1], a[i]
        self.b = a

    @timed
    def bubble_sort(self):
        a = self.a.copy()
        for j in range(0, self.n)[::-1]:
            for i in range(0, self.n):
                if i >= j:
                    break
                self.cmp += 1
                if a[i] > a[i + 1]:
                    self.asg += 2
                    a[i + 1], a[i] = a[i], a[i + 1]
        self.b = a

    def __str__(self):
        if sorted(self.a) == self.b:
            return f'N={self.n}, {self.cmp=}, {self.asg=}'
        else:
            return f'N={self.n}, !! wrong sort !!'


s = Sort(10000)
s.set_random()
print(f'{s.a=}')
s.shell_sort()
print(s)
s.insertion_sort()
print(s)
s.bubble_sort()
print(s)
