import unittest
import twoArrays


class Test(unittest.TestCase):
    def testCases(self):
        self.assertEqual(twoArrays.twoArrays(1, [0, 1], [0, 2]), "YES")
        self.assertEqual(twoArrays.twoArrays(10, [2, 1, 3], [7, 8, 9]), "YES")
        self.assertEqual(twoArrays.twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]), "NO")
        self.assertEqual(
            twoArrays.twoArrays(
                15, [0, 5, 2, 12, 9, 3, 5, 8], [7, 5, 7, 16, 13, 11, 12, 20]
            ),
            "YES",
        )
        self.assertEqual(
            twoArrays.twoArrays(
                15, [0, 5, 2, 12, 9, 3, 5, 8], [7, 5, 7, 16, 13, 11, 12, 2]
            ),
            "NO",
        )


if __name__ == "__main__":
    unittest.main()
