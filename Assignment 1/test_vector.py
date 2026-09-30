import unittest
from vec import Vec


class TestVec(unittest.TestCase):

    def test_mean(self):
        v = Vec([1, 2, 3, 4, 5])

        self.assertEqual(v.mean(), 3.0)

    def test_demean(self):
        v = Vec([1, 2, 3, 4, 5])

        result = v.demean()

        self.assertEqual(result.elements, [-2.0, -1.0, 0.0, 1.0, 2.0])

    def test_demean_mean_is_zero(self):
        v = Vec([10, 20, 30])

        result = v.demean()

        self.assertAlmostEqual(result.mean(), 0.0)

    def test_std(self):
        v = Vec([1, 2, 3, 4, 5])

        self.assertAlmostEqual(v.std(), 1.41421356237)

    def test_constant_vector_std_is_zero(self):
        v = Vec([5, 5, 5, 5])

        self.assertEqual(v.std(), 0.0)


if __name__ == "__main__":
    unittest.main()