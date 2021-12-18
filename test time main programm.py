import unittest
import time
from Main_programm_TP_3 import pro_on


class NumbersTest(unittest.TestCase):

    def test_time(self):

        start1 = time.process_time()
        pro_on("file numbers.txt")
        end1 = time.process_time() - start1

        start2 = time.process_time()
        pro_on("test2 numbers.txt")
        end2 = time.process_time() - start2

        self.assertLess(end2 / 1.45, end1)

    def test_max_time(self):
        start1 = time.time()
        pro_on("test2 numbers.txt")
        end1 = time.time() - start1
        self.assertLess(end1, 10)


if __name__ == '__main__':
    unittest.main()
