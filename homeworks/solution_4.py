import decimal
from functools import lru_cache

from homeworks import Solution


class Solution_4(Solution):

    def __init__(self, data, answer):
        super(Solution_4, self).__init__(data, answer)
        self.data = int(data[0])
        self.answer = int(self.answer[0])

    def __call__(self):
        return str(self._run(self.data)), str(self.answer)


class IterationSolutionFibo(Solution_4):

    def _run(self, n):
        if n == 0:
            return 0
        if n in (1, 2):
            return 1
        a, b = 1, 1
        for i in range(1, n):
            a, b = b, a + b
        return a


class RecursionSolutionFibo(Solution_4):

    @lru_cache()
    def _run(self, n):
        if n == 1 or n == 2:
            return 1

        return self._run(n-1) + self._run(n-2)

    def __call__(self):
        if self.data == 0:
            return '0', str(self.answer)
        if self.data == 1:
            return '1', str(self.answer)

        return super(RecursionSolutionFibo, self).__call__()


class PhiSolutionFibo(Solution_4):
    PHI = decimal.Decimal(1.6180339)

    # Fibonacci numbers upto n = 5
    f = [0, 1, 1, 2, 3, 5]

    def _run(self, n):
        decimal.getcontext().prec = 10000

        root_5 = decimal.Decimal(5).sqrt()
        phi = ((1 + root_5) / 2)

        a = ((phi ** n) - ((-phi) ** -n)) / root_5

        return round(a)
