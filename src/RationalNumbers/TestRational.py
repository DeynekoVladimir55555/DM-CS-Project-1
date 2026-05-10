import unittest
from ..DataClasses.RationalNumber import RationalNumber
from ..DataClasses.NaturalNumber import NaturalNumber
from ..DataClasses.IntNumber import IntNumber


BIG = "9" * 50
BIG2 = "9" * 25
ONE = "1"
ZERO = "0"


def make_q(sign, nomer, denomer):
    return RationalNumber(sign, nomer, denomer)


class TestRedQQ(unittest.TestCase):
    """red_q_q — сокращение дроби"""

    def test_zero_nomer(self):
        # 0/anything -> 0/1
        q = make_q(0, ZERO, BIG)
        r = q.red_q_q()
        self.assertEqual(r.nomer.to_str(), ZERO)
        self.assertEqual(r.denomer.to_str(), ONE)

    def test_already_irreducible(self):
        # 1/2 — уже несократима
        q = make_q(1, ONE, "2")
        r = q.red_q_q()
        self.assertEqual(r.nomer.to_str(), ONE)
        self.assertEqual(r.denomer.to_str(), "2")

    def test_big_equal_numer_denom(self):
        # N/N = 1/1 для большого N
        q = make_q(1, BIG, BIG)
        r = q.red_q_q()
        self.assertEqual(r.nomer.to_str(), ONE)
        self.assertEqual(r.denomer.to_str(), ONE)

    def test_big_reducible(self):
        # (2 * BIG2) / (4 * BIG2) = 1/2
        n = str(int(BIG2) * 2)
        d = str(int(BIG2) * 4)
        q = make_q(1, n, d)
        r = q.red_q_q()
        self.assertEqual(r.nomer.to_str(), ONE)
        self.assertEqual(r.denomer.to_str(), "2")

    def test_negative_big(self):
        n = str(int(BIG2) * 3)
        d = str(int(BIG2) * 9)
        q = make_q(-1, n, d)
        r = q.red_q_q()
        self.assertEqual(r.nomer.to_str(), ONE)
        self.assertEqual(r.denomer.to_str(), "3")
        self.assertEqual(r.nomer.sign, -1)

    def test_returns_new_object(self):
        q = make_q(1, "6", "4")
        r = q.red_q_q()
        self.assertIsNot(q, r)
        # исходный не изменился
        self.assertEqual(q.nomer.to_str(), "6")
        self.assertEqual(q.denomer.to_str(), "4")


class TestIntQB(unittest.TestCase):
    """int_q_b — проверка на целое"""

    def test_integer(self):
        q = make_q(1, BIG, ONE)
        self.assertTrue(q.int_q_b())

    def test_not_integer(self):
        q = make_q(1, BIG, "2")
        self.assertFalse(q.int_q_b())

    def test_zero_is_integer(self):
        q = make_q(0, ZERO, ONE)
        self.assertTrue(q.int_q_b())


class TestMulQQQ(unittest.TestCase):
    """mul_qq_q — умножение дробей"""

    def test_zero_times_big(self):
        a = make_q(0, ZERO, ONE)
        b = make_q(1, BIG, BIG2)
        r = a.mul_qq_q(b)
        self.assertEqual(r.nomer.to_str(), ZERO)

    def test_one_times_big(self):
        a = make_q(1, ONE, ONE)
        b = make_q(1, BIG, BIG2)
        r = a.mul_qq_q(b)
        self.assertEqual(r.nomer.to_str(), BIG)
        self.assertEqual(r.denomer.to_str(), BIG2)

    def test_sign_minus_times_minus(self):
        a = make_q(-1, "3", "4")
        b = make_q(-1, "5", "7")
        r = a.mul_qq_q(b)
        self.assertEqual(r.nomer.sign, 1)

    def test_big_times_big(self):
        a = make_q(1, BIG, ONE)
        b = make_q(1, BIG, ONE)
        r = a.mul_qq_q(b)
        expected = str(int(BIG) ** 2)
        self.assertEqual(r.nomer.to_str(), expected)

    def test_returns_new_object(self):
        a = make_q(1, "3", "4")
        b = make_q(1, "5", "7")
        r = a.mul_qq_q(b)
        self.assertIsNot(a, r)
        self.assertIsNot(b, r)


class TestAddQQQ(unittest.TestCase):
    """add_qq_q — сложение дробей"""

    def test_zero_plus_big(self):
        a = make_q(0, ZERO, ONE)
        b = make_q(1, BIG, BIG2)
        r = a.add_qq_q(b)
        # результат = BIG/BIG2, после сокращения нужно проверять знаменатель
        self.assertNotEqual(r.nomer.to_str(), ZERO)

    def test_same_denom(self):
        a = make_q(1, "1", "3")
        b = make_q(1, "1", "3")
        r = a.add_qq_q(b)
        rr = r.red_q_q()
        self.assertEqual(rr.nomer.to_str(), "2")
        self.assertEqual(rr.denomer.to_str(), "3")

    def test_opposite_signs_cancel(self):
        a = make_q(1, BIG, ONE)
        b = make_q(-1, BIG, ONE)
        r = a.add_qq_q(b)
        self.assertEqual(r.nomer.to_str(), ZERO)

    def test_big_different_denom(self):
        # BIG/2 + BIG/3 = 5*BIG/6
        a = make_q(1, BIG, "2")
        b = make_q(1, BIG, "3")
        r = a.add_qq_q(b)
        rr = r.red_q_q()
        # проверяем равенство через перекрёстное умножение: nomer * 6 == 5*BIG * denomer
        lhs = int(rr.nomer.to_str()) * 6
        rhs = int(BIG) * 5 * int(rr.denomer.to_str())
        self.assertEqual(lhs, rhs)
        self.assertEqual(rr.nomer.sign, 1)


class TestSubQQQ(unittest.TestCase):
    """sub_qq_q — вычитание дробей"""

    def test_self_minus_self(self):
        a = make_q(1, BIG, BIG2)
        r = a.sub_qq_q(a)
        self.assertEqual(r.nomer.to_str(), ZERO)

    def test_big_minus_small(self):
        a = make_q(1, BIG, ONE)
        b = make_q(1, ONE, ONE)
        r = a.sub_qq_q(b)
        expected = str(int(BIG) - 1)
        rr = r.red_q_q()
        self.assertEqual(rr.nomer.to_str(), expected)

    def test_result_negative(self):
        a = make_q(1, ONE, ONE)
        b = make_q(1, BIG, ONE)
        r = a.sub_qq_q(b)
        rr = r.red_q_q()
        self.assertEqual(rr.nomer.sign, -1)


class TestDivQQQ(unittest.TestCase):
    """div_qq_q — деление дробей"""

    def test_divide_by_one(self):
        a = make_q(1, BIG, BIG2)
        b = make_q(1, ONE, ONE)
        r = a.div_qq_q(b)
        rr = r.red_q_q()
        ar = a.red_q_q()
        self.assertEqual(rr.nomer.to_str(), ar.nomer.to_str())
        self.assertEqual(rr.denomer.to_str(), ar.denomer.to_str())

    def test_divide_self_by_self(self):
        a = make_q(1, BIG, BIG2)
        r = a.div_qq_q(a)
        rr = r.red_q_q()
        self.assertEqual(rr.nomer.to_str(), ONE)
        self.assertEqual(rr.denomer.to_str(), ONE)

    def test_sign_minus_divide_minus(self):
        a = make_q(-1, BIG, BIG2)
        b = make_q(-1, BIG, BIG2)
        r = a.div_qq_q(b)
        rr = r.red_q_q()
        self.assertEqual(rr.nomer.sign, 1)

    def test_big_divided_by_big(self):
        a = make_q(1, BIG, ONE)
        b = make_q(1, BIG2, ONE)
        r = a.div_qq_q(b)
        rr = r.red_q_q()
        expected = str(int(BIG) // int(BIG2))
        self.assertEqual(rr.nomer.to_str(), expected)
        self.assertEqual(rr.denomer.to_str(), ONE)


if __name__ == "__main__":
    unittest.main()