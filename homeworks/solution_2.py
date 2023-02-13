from homeworks import Solution


class Solution_2(Solution):

    def __init__(self, data, answer):
        super(Solution_2, self).__init__(data, answer)
        self.data = [int(data) for data in data]
        self.answer = int(self.answer[0])


class EvklidSubtraction(Solution_2):

    def _run(self):
        a, b = self.data
        while a > 0 and b > 0:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a or b


class EvklidRemains(Solution_2):

    def _run(self):
        a, b = self.data
        while a > 0 and b > 0:
            if a > b:
                reminder = a % b
                a = reminder
            else:
                reminder = b % a
                b = reminder

        return a or b


class StainAlgorithm(Solution_2):
    def _run(self, a, b):
        # GCD(0, b) == b; GCD(a, 0) == a,
        # GCD(0, 0) == 0
        if a == 0:
            return b

        if b == 0:
            return a

        # Finding K, where K is the
        # greatest power of 2 that
        # divides both a and b.
        k = 0

        while ((a | b) & 1) == 0:
            a = a >> 1
            b = b >> 1
            k = k + 1

        # Dividing a by 2 until a becomes odd
        while a & 1 == 0:
            a = a >> 1

        # From here on, "a" is always odd.
        while b != 0:

            # If b is even, remove all
            # factor of 2 in b
            while (b & 1) == 0:
                b = b >> 1

            # Now a and b are both odd. Swap if
            # necessary so a <= b, then set
            # b = b - a (which is even).
            if a > b:
                # Swap u and v.
                temp = a
                a = b
                b = temp

            b = (b - a)

        # restore common factors of 2
        return a << k

    def __call__(self, *args, **kwargs):
        return self._run(*self.data), self.answer
