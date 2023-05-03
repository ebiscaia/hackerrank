import unittest
import timeConv


class Tests(unittest.TestCase):
    def testNormalTimeAM(self):
        self.assertEqual(timeConv.timeConversion("10:22:09AM"), "10:22:09")
        self.assertEqual(timeConv.timeConversion("06:44:29AM"), "06:44:29")

    def testNormalTimePM(self):
        self.assertEqual(timeConv.timeConversion("10:22:09PM"), "22:22:09")
        self.assertEqual(timeConv.timeConversion("06:44:29PM"), "18:44:29")

    def testMidnightAndBeyond(self):
        self.assertEqual(timeConv.timeConversion("12:00:00AM"), "00:00:00")
        self.assertEqual(timeConv.timeConversion("12:15:35AM"), "00:15:35")

    def testMiddayAndBeyond(self):
        self.assertEqual(timeConv.timeConversion("12:00:00PM"), "12:00:00")
        self.assertEqual(timeConv.timeConversion("12:15:35PM"), "12:15:35")


if __name__ == "__main__":
    unittest.main()
