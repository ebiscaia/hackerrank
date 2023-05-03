import inverBits
import unittest


class Test(unittest.TestCase):
    def testNumbers(self):
        self.assertEqual(inverBits.flippingBits(10), 4294967295 - 10)
        self.assertEqual(inverBits.flippingBits(2147483647), 4294967295 - 2147483647)
        self.assertEqual(inverBits.flippingBits(2147483647), 2147483648)
        self.assertEqual(inverBits.flippingBits(3), 4294967295 - 3)

    def testOne(self):
        self.assertEqual(inverBits.flippingBits(1), 4294967295 - 1)

    def testZero(self):
        self.assertEqual(inverBits.flippingBits(0), 4294967295)

    def testUpperLimit(self):
        self.assertEqual(inverBits.flippingBits(4294967295), 0)


if __name__ == "__main__":
    unittest.main()
