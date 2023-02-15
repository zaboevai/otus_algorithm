import math

from homeworks import Solution


class Solution_5(Solution):

    def __init__(self, data, answer):
        super(Solution_5, self).__init__(data, answer)
        self.data = int(data[0])
        self.answer = int(self.answer[0])

    def _run(self):
        counter = 0
        for n in range(1, self.data + 1):
            if self.is_prime(n):
                counter += 1
        return counter

    def __call__(self, *args, **kwargs):
        return str(self._run()), str(self.answer)


class IterationSolutionPrimes1(Solution_5):

    @staticmethod
    def is_prime(value):
        divider_count = 0
        for number in range(1, value + 1):
            if value % number == 0:
                divider_count += 1
        return divider_count == 2


class IterationSolutionPrimes2(Solution_5):
    @staticmethod
    def is_prime(value):
        if value == 1:
            return False
        if value == 2:
            return True
        if value % 2 == 0:
            return False

        for number in range(3, value, 2):
            if value % number == 0:
                return False
        return True


class IterationSolutionPrimes3(Solution_5):
    @staticmethod
    def is_prime(value):
        if value == 1:
            return False
        if value == 2:
            return True
        if value % 2 == 0:
            return False

        for number in range(3, value // 2, 2):
            if value % number == 0:
                return False
        return True


class IterationSolutionPrimes4(Solution_5):
    @staticmethod
    def is_prime(value):
        if value == 1:
            return False
        if value == 2:
            return True
        if value % 2 == 0:
            return False

        for number in range(3, round(math.sqrt(value)) + 1, 2):
            if value % number == 0:
                return False
        return True
