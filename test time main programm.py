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
        start1 = time.process_time()
        pro_on("test2 numbers.txt")
        end1 = time.process_time() - start1
        a = pro_on("test2 numbers.txt")
        start3 = time.process_time()
        min(a[4])
        max(a[4])
        v = 0
        for i in a[4]:
            i = int(i)
            v += i
        v = 1
        for i in a[4]:
            i = int(i)
            v *= i
        end3 = time.process_time() - start3
        self.assertLess(end1, end3)


if __name__ == '__main__':
    unittest.main()
