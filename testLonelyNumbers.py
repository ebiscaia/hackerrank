import unittest
import lonelyNumber


class Test(unittest.TestCase):
    def testUniqueInTheMiddleOfTheList(self):
        self.assertEqual(lonelyNumber.lonelyinteger([1, 2, 3, 4, 3, 2, 1]), 4)
        self.assertEqual(
            lonelyNumber.lonelyinteger([10, 20, 50, 3, 8, 10, 20, 50, 3]), 8
        )

    def testLonelySomewhere(self):
        self.assertEqual(
            lonelyNumber.lonelyinteger(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 2, 8, 7, 9, 5, 4]
            ),
            6,
        )
        self.assertEqual(
            lonelyNumber.lonelyinteger([500, 40, 300, 80, 300, 500, 80]), 40
        )

    def testLonelyIsFirst(self):
        self.assertEqual(lonelyNumber.lonelyinteger([5, 10, 10]), 5)
        self.assertEqual(lonelyNumber.lonelyinteger([16, 30, 45, 80, 45, 80, 30]), 16)

    def testLonelyIsLast(self):
        self.assertEqual(lonelyNumber.lonelyinteger([10, 10, 5]), 5)
        self.assertEqual(lonelyNumber.lonelyinteger([30, 45, 80, 45, 80, 30, 16]), 16)


if __name__ == "__main__":
    unittest.main()
