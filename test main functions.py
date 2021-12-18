import unittest
import random
from Main_programm_TP_3 import num_min
from Main_programm_TP_3 import num_max
from Main_programm_TP_3 import num_sum
from Main_programm_TP_3 import num_multiply


class NumbersTest(unittest.TestCase):

    def test_min(self):
        a = []
        for i in range(10000):
            a.append(random.randrange(1, 100000))
        with self.subTest(i=a):
            self.assertEqual(min(a), num_min(a))

    def test_max(self):
        a = []
        for i in range(10000):
            a.append(random.randrange(1, 100000))
        with self.subTest(i=a):
            self.assertEqual(max(a), num_max(a))

    def test_sum(self):
        a = []
        for i in range(10000):
            a.append(random.randrange(1, 100000))
        print(a)
        with self.subTest(i=a):
            self.assertEqual(sum(a), num_sum(a))

    def test_multiply(self):
        a = []
        for j in range(10):
            a.append(random.randrange(1, 100))
        with self.subTest(i=a):
            self.assertEqual(num_multiply(a), num_multiply(a))


if __name__ == '__main__':
    unittest.main()
