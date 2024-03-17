import unittest
from Q1 import merge
from ed_utils.decorators import number
from data_structures.array_list import ArrayList
from typing import List


def AL(lst: List) -> ArrayList:
    res = ArrayList(len(lst))
    for num in lst:
        res.append(num)
    return res


def toList(al: ArrayList):
    out = []
    for i in range(len(al)):
        out.append(al[i])
    return out


class Test_Q1(unittest.TestCase):
    def assertResultEqual(self, expected: List, actual: List):
        if len(actual) < len(expected):
            self.fail('Length of output is too short')
        
        for i in range(len(expected)):
            if actual[i] != expected[i]:
                self.fail(f"Results did not match: {toList(expected)}, {toList(actual)}")
            
    @number("1.1")
    def test_examples(self):
        self.assertResultEqual(merge(AL([1,2,4]), AL([1,3,4])), AL([1,1,2,3,4,4]))
        
    @number("1.2")
    def test_extra(self):
        self.assertResultEqual(merge(AL([-1, 3, 5, 7, 9]), AL([2, 4, 6])), AL([-1, 2, 3, 4, 5, 6, 7, 9]))
        self.assertResultEqual(merge(AL([]), AL([1,3])), AL([1,3]))
        self.assertResultEqual(merge(AL([]), AL([])), AL([]))

if __name__ == '__main__':
    unittest.main()