import unittest
import queryString


class Test(unittest.TestCase):
    def testQuery(self):
        self.assertEqual(
            queryString.matchingStrings(
                ["aba", "baba", "aba", "xzxb"],
                ["aba", "xzxb", "ab"],
            ),
            [2, 1, 0],
        )
        self.assertEqual(
            queryString.matchingStrings(
                ["def", "de", "fgh"],
                ["de", "lmn", "fgh"],
            ),
            [1, 0, 1],
        )
        self.assertEqual(
            queryString.matchingStrings(
                [
                    "abcde",
                    "sdaklfj",
                    "asdjf",
                    "na",
                    "basdn",
                    "sdaklfj",
                    "asdjf",
                    "na",
                    "asdjf",
                    "na",
                    "basdn",
                    "sdaklfj",
                    "asdjf",
                ],
                ["abcde", "sdaklfj", "asdjf", "na", "basdn"],
            ),
            [1, 3, 4, 3, 2],
        )


if __name__ == "__main__":
    unittest.main()
