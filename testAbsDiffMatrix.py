import unittest
import absDiffMatrix


class Test(unittest.TestCase):
    def testOrderThreeMatrix(self):
        self.assertEqual(
            absDiffMatrix.diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]), 2
        )
        self.assertEqual(
            absDiffMatrix.diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15
        )

    def testHighOrderMatrix(self):
        self.assertEqual(
            absDiffMatrix.diagonalDifference(
                [
                    [8, 0, 1, -5, 0, 1, 2, 0],
                    [0, 3, -10, -20, 20, 1, 5, 0],
                    [3, 2, 1, 1, 1, -3, 8, 2],
                    [2, 1, 0, -8, -6, -2, 1, -5],
                    [-2, 2, 4, 5, -3, 4, -5, 0],
                    [0, 3, 4, 0, 1, -1, 5, 5],
                    [2, 3, 1, 0, 0, 1, 3, 2],
                    [0, 6, 2, 1, 1, 7, 9, 4],
                ]
            ),
            1,
        )

    def testOrderTwoMatrix(self):
        self.assertEqual(absDiffMatrix.diagonalDifference([[1, 2], [4, 5]]), 0)
        self.assertEqual(absDiffMatrix.diagonalDifference([[1, 2], [4, -5]]), 10)

    def testOrderOneMatrix(self):
        self.assertEqual(absDiffMatrix.diagonalDifference([[1]]), 0)
        self.assertEqual(absDiffMatrix.diagonalDifference([[-5]]), 0)


if __name__ == "__main__":
    unittest.main()
