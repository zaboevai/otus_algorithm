import decimal

from homeworks import Solution


class Solution_3(Solution):

    def __init__(self, data, answer):
        super(Solution_3, self).__init__(data, answer)
        self.data = [float(data) for data in data]
        self.answer = float(self.answer[0])


class IterateSolution(Solution_3):

    def _run(self):
        a, power = self.data
        b = a
        if power == 0:
            return 1

        for num in range(int(power) - 1):
            b = a * b

        return round(b, 11)


class Power2Solution(Solution_3):

    def _run(self):
        a, power = self.data
        power = int(power)

        p = decimal.Decimal(1)
        d = decimal.Decimal(a)

        while power >= 1:
            power = power // 2
            d = d * d
            if power % 2 == 1:
                p = p * d
        p = decimal.Decimal(p)
        return p

    def __call__(self, *args, **kwargs):
        self.answer = decimal.Decimal(self.answer)
        return round(self._run(), 11), round(self.answer, 11)


class BinSolution(Solution_3):

    def _run(self, a, b):
        if b == 0:
            return 1
        if b % 2 == 1:
            return self._run(a, b - 1) * a
        else:
            b = self._run(a, b / 2)
            return b * b

    def __call__(self, *args, **kwargs):
        a, b = self.data
        a, b = decimal.Decimal(a), decimal.Decimal(b)
        self.answer = decimal.Decimal(self.answer)
        return round(self._run(a, b), 11), round(self.answer, 11)
