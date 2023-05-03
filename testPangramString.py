import unittest
import pangramString


class Test(unittest.TestCase):
    def testShortStrint(self):
        self.assertEqual(pangramString.pangrams("cavaloBoi"), "not pangram")

    def testFullRandomAlfabet(self):
        self.assertEqual(
            pangramString.pangrams("ajsoepQyMcnRDzwxIvTkGlHbuf"), "pangram"
        )

    def testChallenge(self):
        self.assertEqual(
            pangramString.pangrams(
                "We promptly judged antique ivory buckles for the next prize"
            ),
            "pangram",
        )
        self.assertEqual(
            pangramString.pangrams(
                "We promptly judged antique ivory buckles for the prize"
            ),
            "not pangram",
        )


if __name__ == "__main__":
    unittest.main()
