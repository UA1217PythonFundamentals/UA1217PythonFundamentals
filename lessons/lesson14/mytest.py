import unittest


def f(a,b,c):
    d = b**2 -4*a*c
    if d < 0:
        return None
    elif d == 0:
        return -b/(2*a)
    else:
        return (-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a) 
    

class TestF(unittest.TestCase):
    def test_1(self):
        actual = f(1,2,-3)
        expected = (1.0, -3.0)
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = f(1,0,1)
        expected = None
        self.assertEqual(actual, expected)
    def test_3(self):
        actual = f(1,2,1)
        expected = -1.0
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
