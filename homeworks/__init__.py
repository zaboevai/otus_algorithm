class Solution:

    def __init__(self, data: str):
        self.data = data

    def __call__(self, *args, **kwargs):
        raise NotImplementedError
