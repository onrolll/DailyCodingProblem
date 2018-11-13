import unittest
from day5 import firstMissingPositiveInteger as f

class TestFirstMissingPositiveInteger(unittest.TestCase):
        def testNoPositiveIntegers(self):
            a = [-10, -3, -22, 0]
            assert f(a) == 1
        def testOnlyPositiveIntegers(self):
            a = [1, 2, 3, 4]
            b = [1, 3, 8, 5, 6]
            c = [4, 8, 9, 15, 22]
            
            assert f(a) == 5
            assert f(b) == 2
            assert f(c) == 1
        
        def testIndexError(self):
            a = []
            assert f(a) == 1
        


