from fraction import Fraction
import unittest

class TestInit(unittest.TestCase):
    # several of these will need to check to see if an exception is raised

    def test_divZero(self):
        with self.assertRaises(ZeroDivisionError, msg="Denominator of zero fails to raise DivByZero"):
            a = Fraction(1, 0)
            self.assertFalse(a.denominator == 0, "Denominator is zero")

    def test_default(self):
        # will the 0 argument version of the constructor produce the correct fraction?
        a = Fraction()
        self.assertEqual(a, Fraction(0, 1), "Default fraction is invalid")

    def test_oneArg(self):
        # will the 1 argument version of the constructor produce the correct fraction?
        a = Fraction(2)
        self.assertEqual(a, Fraction(2, 1), "One arg fraction is invalid")
        a = Fraction(5)
        self.assertEqual(a, Fraction(5, 1), "One arg fraction is invalid")

    def test_twoArg(self):
        # will the 2 argument version of the constructor produce the correct fraction?
        a = Fraction(2, 3)
        self.assertEqual(a, Fraction(2, 3), "Two arg fraction is invalid")
        a = Fraction(5, 2)
        self.assertEqual(a, Fraction(5, 2), "Two arg fraction is invalid")

    def test_invalidArg(self):
        # will constructor through an exception if non-numeric data is passed?
        with self.assertRaises(TypeError, msg="Incorrect type fails to raise Invalid type"):
            a = Fraction("cat", "dog")
            self.assertIsInstance(a.denominator, int, "Invalid numerator type")
            self.assertIsInstance(a.numerator, int, "Invalid denominator type")

    def test_reduced(self):
        # if the inputs share a factor, is the fraction reduced? i.e. 2/4 = 1/2
        a = Fraction(2, 4)
        self.assertEqual(a, Fraction(1, 2), "Reduced fraction is invalid")
        a = Fraction(6, 3)
        self.assertEqual(a, Fraction(2, 1), "Reduced fraction is invalid")


class TestStr(unittest.TestCase):
    def test_displayFraction(self):
        a = Fraction(1, 2)
        self.assertEqual(" 1/2 ", a.__str__(), "Fraction displayed incorrectly")

    def test_displayInt(self):
        # if the denominator is 1, does display omit the /1?
        a = Fraction(2, 1)
        self.assertEqual(" 2 ", a.__str__(), "Integer fraction is invalid")

    def test_displayZero(self):
        # if the denominator is 0, does display omit the denominator?
        a = Fraction(0, 2)
        self.assertEqual(" 0 ", a.__str__(), "Zero fraction is invalid")

    def test_displayNeg(self):
        # if the fraction is negative, is it possible to erroneously have it display 1/-2, vs -1/2?
        a = Fraction(1, -2)
        self.assertEqual(" -1/2 ", a.__str__(), "Negative fraction is invalid")

    def test_displayNegToPos(self):
        a = Fraction(-1, -2)
        self.assertEqual(" 1/2 ", a.__str__(), "Negative to positive fraction is invalid")

class TestFloat(unittest.TestCase):
    def test_displayDecimal(self):
        a = Fraction(1/2)
        self.assertEqual(0.5, a.__float__(), "Fraction float is incorrect")

    def test_displayRepeating(self):
        a = Fraction(1/3)
        self.assertEqual(0.33333333333333333, a.__float__(), "Repeating float is incorrect")

    def test_displayWhole(self):
        a = Fraction(2/1)
        self.assertEqual(2, a.__float__(), "Float whole number is incorrect")

class TestAdd(unittest.TestCase):
    def test_addDenominator(self):
        a = Fraction(1, 2)
        b = Fraction(1, 3)
        self.assertEqual(Fraction(5, 6), a.__add__(b), "Denominator addition is incorrect")

    def test_addNumerator(self):
        a = Fraction(1, 3)
        b = Fraction(4, 3)
        self.assertEqual(Fraction(5, 3), a.__add__(b), "Numerator addition is incorrect")

    def test_addSimplify(self):
        a = Fraction(1, 2)
        b = Fraction(1, 2)
        self.assertEqual(Fraction(1, 1), a.__add__(b), "Simplify after addition is incorrect")

class TestSub(unittest.TestCase):
    def test_denominatorSub(self):
        a = Fraction(1, 2)
        b = Fraction(1, 3)
        self.assertEqual(Fraction(1, 6), a.__sub__(b), "Denominator subtraction is incorrect")

    def test_numeratorSub(self):
        a = Fraction(2, 3)
        b = Fraction(1, 3)
        self.assertEqual(Fraction(1, 3), a.__sub__(b), "Numerator subtraction is incorrect")

    def test_simplifySub(self):
        a = Fraction(3, 2)
        b = Fraction(1, 2)
        self.assertEqual(Fraction(1, 1), a.__sub__(b), "Simplify after subtraction is incorrect")

class TestMul(unittest.TestCase):
    def test_fractionMul(self):
        a = Fraction(1/2)
        b = Fraction(1/3)
        self.assertEqual(Fraction(1, 6), a.__mul__(b), "Fraction multiplication is incorrect")

    def test_simplifyMul(self):
        a = Fraction(1/2)
        b = Fraction(2/3)
        self.assertEqual(Fraction(1, 3), a.__mul__(b), "Simplify after multiplication is incorrect")

class TestDiv(unittest.TestCase):
    def test_fractionDiv(self):
        a = Fraction(1, 2)
        b = Fraction(1/3)
        self.assertEqual(Fraction(3, 2), a.__truediv__(b), "Fraction division is incorrect")

    def test_simplifyDiv(self):
        a = Fraction(1/2)
        b = Fraction(1/2)
        self.assertEqual(Fraction(1, 1), a.__mul__(b), "Simplify after division is incorrect")

    def test_divByZero(self):
        a = Fraction(1, 2)
        b = Fraction(0)
        self.assertRaises(ZeroDivisionError, a.__truediv__(b), "Fraction division by zero is invalid")
