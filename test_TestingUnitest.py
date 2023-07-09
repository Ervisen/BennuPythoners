import unittest
from TestingUnitest import area
from math import pi
class TestArea(unittest.TestCase):
    def test_area(self):
        print('----Test valores de resultado conocido----')
        self.assertAlmostEqual(area(1), pi)
        self.assertAlmostEqual(area(0), 1)
        self.assertAlmostEqual(area(3), pi*(3**2))
        