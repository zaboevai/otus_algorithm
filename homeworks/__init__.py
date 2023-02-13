class Solution:

    def __init__(self, data: list[str], answer: list[str]):
        self.data = data
        self.answer = answer

    def _run(self, *args, **kwargs):
        raise NotImplementedError

    def __call__(self):
        return self._run(), self.answer
