import os
import time

from homeworks.solution_0 import LenSolution
from homeworks.solution_1 import *
from homeworks.solution_2 import *
from homeworks.solution_3 import *
from homeworks.solution_4 import *
from homeworks.solution_5 import *


class CheckHomework:
    ROOT = 'homeworks'
    homeworks = []

    def __init__(self, homework):
        self.homework, _solution = homework
        self.path = os.path.join(self.ROOT, self.homework)
        self.solution: Solution = _solution

    def run(self, show_results=False):
        print(f'{self.homework} - {self.solution.__name__!r} result:')
        for root, dirs, files in os.walk(self.path):
            test_files = self._get_task_files(files)
            for data_file, test_data, expected_answer in self._get_test_data(root, test_files):
                answer, prepared_expected_answer, elapsed_time = \
                    self._calculate_elapsed_time(self.solution)(test_data, expected_answer)

                result = "OK" if answer == (prepared_expected_answer or expected_answer) else "NOK"
                results = f'{answer:>30} = {prepared_expected_answer}' if show_results else ''
                print(f'{data_file + ":"}  {result:>10} {elapsed_time:>20} {results}')

    def _get_task_files(self, files):
        in_files = self._sort_file([file for file in files if file.endswith('in')])
        out_files = self._sort_file([file for file in files if file.endswith('out')])
        test_files = list(zip(in_files, out_files))
        return test_files

    @staticmethod
    def _get_test_data(root, test_files):
        for data_file, answer_file in test_files:
            data_file_path = os.path.join(root, data_file)
            answer_file_path = os.path.join(root, answer_file)
            with open(data_file_path) as data_, open(answer_file_path) as answer_:
                expected_answer = [line.strip('\n') for line in answer_.readlines()]
                test_data = [line.strip('\n') for line in data_.readlines()]
                yield data_file, test_data, expected_answer

    @staticmethod
    def _sort_key(file):
        return int(file.split('.')[1])

    def _sort_file(self, files: list):
        return sorted(files, key=self._sort_key)

    @classmethod
    def _calculate_elapsed_time(cls, func):
        def __calculate_elapsed_time(data, answer):
            bt = time.monotonic()
            result = func(data, answer)()
            _elapsed_time = time.monotonic() - bt
            return *result, round(_elapsed_time, 4)

        return __calculate_elapsed_time


if __name__ == '__main__':
    homeworks = [
        ('0.String', LenSolution),
        # ('1.Tickets', RecursionSolution),
        ('1.Tickets', FastSolution),
        # ('2.GCD', EvklidSubtraction),
        ('2.GCD', EvklidRemains),
        # ('2.GCD', StainAlgorithm),  # не понял алгоритм
        ('3.Power', IterateSolution),
        # ('3.Power', Power2Solution),
        ('3.Power', BinSolution),
        # ('4.Fibo', RecursionSolutionFibo),
        # ('4.Fibo', IterationSolutionFibo),
        ('4.Fibo', PhiSolutionFibo),
        # ('5.Primes', IterationSolutionPrimes1),
        # ('5.Primes', IterationSolutionPrimes2),
        # ('5.Primes', IterationSolutionPrimes3),
        ('5.Primes', IterationSolutionPrimes4),
    ]

    homework_num = 4
    CheckHomework(homework=homeworks[homework_num]).run(show_results=True)

    # for homework in homeworks:
    #     CheckHomework(homework=homework).run(show_results=False)
