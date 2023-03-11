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
    def selection_sort(self):
        a = self.a.copy()

        for i in range(self.n):
            mini = min(a[i:])
            min_index = a[i:].index(mini)
            a[i + min_index] = a[i]
            a[i] = mini

        self.b = a

    @timed
    def heap_sort(self):
        a = self.a.copy()

        def swap(i, j):
            nonlocal a
            a[i], a[j] = a[j], a[i]

        def heapify(end, i):
            nonlocal a
            l = 2 * i + 1
            r = 2 * (i + 1)
            max = i
            if l < end and a[i] < a[l]:
                max = l
            if r < end and a[max] < a[r]:
                max = r
            if max != i:
                swap(i, max)
                heapify(end, max)

        start = self.n // 2 - 1
        for i in range(start, -1, -1):
            heapify(self.n, i)
        for i in range(self.n - 1, 0, -1):
            swap(i, 0)
            heapify(i, 0)

        self.b = a

    def __str__(self):
        if sorted(self.a) == self.b:
            return f'N={self.n}, {self.cmp=}, {self.asg=}'
        else:
            return f'N={self.n}, !! wrong sort !!'


s = Sort(10_000)
s.set_random()
s.selection_sort()
print(s)
s.heap_sort()
print(s)
