from homeworks import Solution


class LenSolution(Solution):

    def __init__(self, data, answer):
        super(LenSolution, self).__init__(data, answer)
        self.answer = int(self.answer[0])
        self.data = str(self.data[0])

    def _run(self):
        return len(self.data)

    def __call__(self, ):
        return str(self._run()), str(self.answer)
