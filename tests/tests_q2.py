import unittest
from typing import List
from data_structures.array_list import ArrayList
from Q2 import time_required_to_buy
from ed_utils.decorators import number


def AL(lst: List) -> ArrayList:
    res = ArrayList(len(lst))
    for num in lst:
        res.append(num)
    return res


class Test_Q2(unittest.TestCase):
    @number("2.1")
    def test_examples(self):
        self.assertEqual(time_required_to_buy(AL([2,3,2]), 2), 6)
        self.assertEqual(time_required_to_buy(AL([2,3,2]), 1), 7)
        self.assertEqual(time_required_to_buy(AL([2, 3, 4, 5]), 0), 5)
    
    @number("2.2")
    def test_extra(self):
        self.assertEqual(time_required_to_buy(AL([5,1,1,1]), 0), 8)
        self.assertEqual(time_required_to_buy(AL([2, 3, 4, 5]), 1), 9)
        self.assertEqual(time_required_to_buy(AL([2, 3, 4, 5]), 2), 12)
        self.assertEqual(time_required_to_buy(AL([2, 3, 4, 5]), 3), 14)

if __name__ == '__main__':
    unittest.main()