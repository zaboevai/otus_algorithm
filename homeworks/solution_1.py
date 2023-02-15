import math

from homeworks import Solution


class Solution_1(Solution):

    def __init__(self, data, answer):
        super(Solution_1, self).__init__(data, answer)
        self.data: list[int] = [int(data) for data in self.data]


class RecursionSolution(Solution_1):
    counter = 0

    def _run(self, remaining_digits: int, sum_a: int, sum_b: int):
        if remaining_digits == 0:
            if sum_a == sum_b:
                RecursionSolution.counter += 1
            return RecursionSolution.counter

        for a in range(10):
            for b in range(10):
                self._run(remaining_digits - 1, sum_a + a, sum_b + b)
        return RecursionSolution.counter

    def __call__(self):
        RecursionSolution.counter = 0
        return str(self._run(self.data[0], 0, 0)), str(self.answer[0])


class FastSolution(Solution_1):

    def __init__(self, data, answer):
        super(FastSolution, self).__init__(data, answer)
        self.answer = int(self.answer[0])

    @classmethod
    def get_next_array(cls, prev_arr):
        new_len = len(prev_arr) + 9
        arr = []
        for i in range(new_len):
            q = 0
            for j in range(10):
                index = i - j
                if 0 <= index < len(prev_arr):
                    q += prev_arr[index]
            arr.insert(i, q)
        return arr

    def _run(self, ticket_length):
        result = []
        arr = [1 for i in range(10)]
        for i in range(ticket_length - 1):
            arr = self.get_next_array(arr)

        for j in arr:
            result.append(int(math.pow(j, 2)))
        return sum(result)

    def __call__(self):
        return str(self._run(*self.data)), str(self.answer)
