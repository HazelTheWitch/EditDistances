import unittest
import editdistances as eds


class TestJaro(unittest.TestCase):
    def test_sameString(self):
        jaro = eds.Jaro()
        self.assertEqual(jaro.similarity('kitten', 'kitten'), 1)

    def test_differentStrings(self):
        jaro = eds.Jaro()
        self.assertAlmostEqual(jaro.similarity('CRATE', 'TARCE'), 0.622222222222, 6)
        self.assertAlmostEqual(jaro.similarity('CRATE', 'TRACE'), 0.733333333333, 6)
        self.assertAlmostEqual(jaro.similarity('DWAYNE', 'DUANE'), 0.822222222222, 6)


class TestJaroWinkler(unittest.TestCase):
    def test_sameString(self):
        jaroWinkler = eds.JaroWinkler()
        self.assertEqual(jaroWinkler.similarity('kitten', 'kitten'), 1)

    def test_differentStrings(self):
        jaroWinkler = eds.JaroWinkler()
        self.assertAlmostEqual(jaroWinkler.similarity('CRATE', 'TARCE'), 0.622222222222, 6)
        self.assertAlmostEqual(jaroWinkler.similarity('CRATE', 'TRACE'), 0.733333333333, 6)
        self.assertAlmostEqual(jaroWinkler.similarity('DWAYNE', 'DUANE'), 0.84, 6)


if __name__ == '__main__':
    unittest.main()
