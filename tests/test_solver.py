import unittest

from src.solver import DieNSolver


class TestDieNSolver(unittest.TestCase):

    def test_find_optimal_policy_value(self):
        tests = [
            ([1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0], 6.314),
            ([1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0], 7.3799),
            ([1, 1, 1, 0, 0, 0], 2.5833)
        ]
        solver = DieNSolver()
        for test in tests:
            badSides = test[0]
            expected = test[1]
            actual = solver.find_optimal_policy_value(badSides)
            self.assertAlmostEqual(actual, expected, places=3)
