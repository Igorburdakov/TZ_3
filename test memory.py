import unittest
import sys
from Main_programm_TP_3 import pro_on

# Тест проверяющий, не использует ли файл, который в 1.45 раз больше, более чем в 1,45 раз больше памяти


class NumbersTest(unittest.TestCase):

    def test_memory(self):
        a = pro_on("file numbers.txt")
        b = pro_on("test2 numbers.txt")
        self.assertLessEqual(sys.getsizeof(b[4]) / 1.45, sys.getsizeof(a[4]))
        print(sys.getsizeof(b[4]) / 1.45, sys.getsizeof(a[4]))


if __name__ == '__main__':
    unittest.main()
