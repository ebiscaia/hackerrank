import testing
import timeConv
import minMaxSum
import unittest


class TestMultipy(unittest.TestCase):
    def testWithTwoPositives(self):
        self.assertEqual(testing.multiplyWithLoop(15, 13), 15 * 13)
        self.assertEqual(testing.multiplyWithLoop(13, 15), 13 * 15)

    def testZeroNumber(self):
        self.assertEqual(testing.multiplyWithLoop(0, 13), 0)

    def testNumberZero(self):
        self.assertEqual(testing.multiplyWithLoop(13, 0), 0)

    def testZeroZero(self):
        self.assertEqual(testing.multiplyWithLoop(0, 0), 0)

    # def testNegativePositive(self):
    #     self.assertEqual(testing.multiplyWithLoop(-5, 3), -5 * 3)

    def testPositiveNegative(self):
        self.assertEqual(testing.multiplyWithLoop(5, -3), 5 * (-3))

    def testAllEqual(self):
        self.assertEqual(minMaxSum.miniMaxSum([5, 5, 5, 5, 3]), "18 20")

    def testAllEqual2(self):
        self.assertEqual(minMaxSum.miniMaxSum([-5, -5, -5, -5, 3]), "-20 -12")


    def testRandomTimeAm(self):
        self.assertEqual(timeConv.timeConversion("10:26:44AM"), "10:26:44")

    def testDiffNumberUnordered(self):
        self.assertEqual(minMaxSum.miniMaxSum([150, 300, 25, -50, 250]), "375 725")



if __name__ == "__main__":
    unittest.main()
