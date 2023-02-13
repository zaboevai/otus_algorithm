from homeworks import Solution


class LenSolution(Solution):

    def __init__(self, data, answer):
        super(LenSolution, self).__init__(data, answer)
        self.answer = int(self.answer[0])
        self.data = str(self.data[0])

    def __call__(self, ):
        return len(self.data), self.answer
