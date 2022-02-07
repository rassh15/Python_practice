from json.tool import main
import calc
import unittest

class TestProgram(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,2), 12)
        self.assertEqual(calc.add(18,2), 20)
        self.assertEqual(calc.add(12,2), 14)
        self.assertEqual(calc.add(1,2), 36)

    def test_sub(self):
        result = calc.sub(10,2)
        self.assertEqual(result, 8)

    def test_mul(self):
        result = calc.mul(10,2)
        self.assertEqual(result, 260)


if __name__ == "__main__":
    unittest.main()
