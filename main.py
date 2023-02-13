import os
import time

from homeworks import Solution
from homeworks.solution_0 import LenSolution
from homeworks.solution_1 import FastSolution


class CheckHomework:
    ROOT = 'homeworks'
    homeworks = []

    @classmethod
    def set_homeworks(cls, homeworks_):
        cls.homeworks = homeworks_

    def __init__(self, num):
        self.homework, _solution = self.homeworks[num]
        self.path = os.path.join(self.ROOT, self.homework)
        self.solution: Solution = _solution

    def run(self):
        print(f'{self.homework} - {self.solution.__name__}result:')
        for root, dirs, files in os.walk(self.path):
            test_files = self._get_task_files(files)
            for data_file, test_data, expected_answer in self._get_test_data(root, test_files):
                answer, prepared_expected_answer, elapsed_time  = \
                    self._calculate_elapsed_time(self.solution)(test_data, expected_answer)

                result = "OK" if answer == (prepared_expected_answer or expected_answer) else "NOK"
                print(f'{data_file + ":"}  {result:>10} {elapsed_time:>20} '
                      f'{answer:>30} = {prepared_expected_answer}')

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
        ('1.Tickets', FastSolution),
    ]
    CheckHomework.set_homeworks(homeworks)

    homework_num = 0
    CheckHomework(num=homework_num).run()
