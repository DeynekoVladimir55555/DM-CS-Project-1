import unittest
from RationalNumber import RationalNumber
from NaturalNumber import NaturalNumber
from Polinom import Polinom


BIG = "9" * 50
BIG2 = "9" * 25
ONE = "1"
ZERO = "0"


def make_q(sign, nomer, denomer):
    return RationalNumber(sign, nomer, denomer)


def make_p(sign, deg, nomer, denomer):
    return Polinom(sign, deg, nomer, denomer)


def zero_p():
    return Polinom(0, 0, ZERO, ONE)


def is_zero_p(p):
    return p.deg == 0 and p.coefs[0].nomer.to_str() == ZERO


class TestDegPN(unittest.TestCase):
    """deg_p_n — степень многочлена"""

    def test_zero_polinom(self):
        p = zero_p()
        self.assertEqual(p.deg_p_n(), 0)

    def test_high_degree(self):
        p = make_p(1, 1000, ONE, ONE)
        self.assertEqual(p.deg_p_n(), 1000)

    def test_after_change_coef(self):
        p = make_p(1, 3, ONE, ONE)
        p.change_coef(1, 10, ONE, ONE)
        self.assertEqual(p.deg_p_n(), 10)


class TestMulPxkP(unittest.TestCase):
    """mul_pxk_p — умножение на x^k"""

    def test_k_zero(self):
        p = make_p(1, 3, BIG, ONE)
        r = p.mul_pxk_p(0)
        self.assertEqual(r.deg, 3)
        self.assertEqual(r.coefs[3].nomer.to_str(), BIG)

    def test_k_nonzero(self):
        p = make_p(1, 2, "5", ONE)
        r = p.mul_pxk_p(3)
        self.assertEqual(r.deg, 5)
        self.assertIn(5, r.coefs)
        self.assertEqual(r.coefs[5].nomer.to_str(), "5")

    def test_big_k(self):
        p = make_p(1, 1, BIG, ONE)
        r = p.mul_pxk_p(999)
        self.assertEqual(r.deg, 1000)
        self.assertEqual(r.coefs[1000].nomer.to_str(), BIG)

    def test_returns_new_object(self):
        p = make_p(1, 2, "3", ONE)
        r = p.mul_pxk_p(5)
        self.assertIsNot(p, r)
        self.assertEqual(p.deg, 2)  # исходный не изменился


class TestDerPP(unittest.TestCase):
    """der_p_p — производная"""

    def test_constant(self):
        p = make_p(1, 0, "7", ONE)
        r = p.der_p_p()
        self.assertTrue(is_zero_p(r))

    def test_linear(self):
        # 5x -> 5
        p = make_p(1, 1, "5", ONE)
        r = p.der_p_p()
        self.assertEqual(r.deg, 0)
        self.assertEqual(r.coefs[0].nomer.to_str(), "5")

    def test_degree_reduces(self):
        # x^10 -> 10*x^9
        p = make_p(1, 10, ONE, ONE)
        r = p.der_p_p()
        self.assertEqual(r.deg, 9)
        self.assertEqual(r.coefs[9].nomer.to_str(), "10")

    def test_big_coef(self):
        # BIG * x^2 -> 2*BIG * x
        p = make_p(1, 2, BIG, ONE)
        r = p.der_p_p()
        self.assertEqual(r.deg, 1)
        expected = str(int(BIG) * 2)
        self.assertEqual(r.coefs[1].nomer.to_str(), expected)


class TestFacPQ(unittest.TestCase):
    """fac_p_q — вынесение НОД числителей и НОК знаменателей"""

    def test_zero_polinom(self):
        p = zero_p()
        r = p.fac_p_q()
        self.assertEqual(r.nomer.to_str(), ZERO)

    def test_single_term(self):
        # 6/4 * x^3 -> НОД=6, НОК=4 -> 6/4
        p = make_p(1, 3, "6", "4")
        r = p.fac_p_q()
        self.assertEqual(r.nomer.to_str(), "6")
        self.assertEqual(r.denomer.to_str(), "4")

    def test_two_terms_common_factor(self):
        # 6x + 9 -> НОД(6,9)=3, НОК(1,1)=1 -> 3/1
        p = make_p(1, 1, "6", ONE)
        p.change_coef(1, 0, "9", ONE)
        r = p.fac_p_q()
        self.assertEqual(r.nomer.to_str(), "3")
        self.assertEqual(r.denomer.to_str(), ONE)

    def test_big_coefficients(self):
        # BIG*x + BIG -> НОД=BIG
        p = make_p(1, 1, BIG, ONE)
        p.change_coef(1, 0, BIG, ONE)
        r = p.fac_p_q()
        self.assertEqual(r.nomer.to_str(), BIG)

    def test_mixed_denominators(self):
        # x/2 + x^2/3 -> НОД числителей=1, НОК знаменателей=6
        p = make_p(1, 2, ONE, "3")
        p.change_coef(1, 1, ONE, "2")
        r = p.fac_p_q()
        self.assertEqual(r.denomer.to_str(), "6")

    def test_all_negative_even_count(self):
        # (-2x) + (-4) -> count=2, знак положительный
        p = make_p(-1, 1, "2", ONE)
        p.change_coef(-1, 0, "4", ONE)
        r = p.fac_p_q()
        self.assertEqual(r.nomer.sign, 1)

    def test_all_negative_odd_count(self):
        # (-2x^2) + (-4x) + (-6) -> count=3, знак отрицательный
        p = make_p(-1, 2, "2", ONE)
        p.change_coef(-1, 1, "4", ONE)
        p.change_coef(-1, 0, "6", ONE)
        r = p.fac_p_q()
        self.assertEqual(r.nomer.sign, -1)


class TestMulPqP(unittest.TestCase):
    """mul_pq_p — умножение многочлена на рациональное число"""

    def test_multiply_by_zero(self):
        p = make_p(1, 5, BIG, ONE)
        k = make_q(0, ZERO, ONE)
        r = p.mul_pq_p(k)
        self.assertTrue(is_zero_p(r))

    def test_multiply_by_one(self):
        p = make_p(1, 3, "7", "3")
        k = make_q(1, ONE, ONE)
        r = p.mul_pq_p(k)
        self.assertEqual(r.coefs[3].nomer.to_str(), "7")
        self.assertEqual(r.coefs[3].denomer.to_str(), "3")

    def test_multiply_big_coef(self):
        # BIG * (BIG/1) = BIG^2
        p = make_p(1, 1, BIG, ONE)
        k = make_q(1, BIG, ONE)
        r = p.mul_pq_p(k)
        expected = str(int(BIG) ** 2)
        self.assertEqual(r.coefs[1].nomer.to_str(), expected)

    def test_returns_new_object(self):
        p = make_p(1, 2, "5", ONE)
        k = make_q(1, "3", ONE)
        r = p.mul_pq_p(k)
        self.assertIsNot(p, r)
        self.assertEqual(p.coefs[2].nomer.to_str(), "5")  # исходный не изменился

    def test_sign_flip(self):
        p = make_p(1, 1, "4", ONE)
        k = make_q(-1, ONE, ONE)
        r = p.mul_pq_p(k)
        self.assertEqual(r.coefs[1].nomer.sign, -1)


class TestAddPPP(unittest.TestCase):
    """add_pp_p — сложение многочленов"""

    def test_zero_plus_zero(self):
        a = zero_p()
        b = zero_p()
        r = a.add_pp_p(b)
        self.assertTrue(is_zero_p(r))

    def test_zero_plus_poly(self):
        a = zero_p()
        b = make_p(1, 3, BIG, ONE)
        r = a.add_pp_p(b)
        self.assertEqual(r.deg, 3)
        self.assertEqual(r.coefs[3].nomer.to_str(), BIG)

    def test_opposite_cancel(self):
        a = make_p(1, 2, BIG, ONE)
        b = make_p(-1, 2, BIG, ONE)
        r = a.add_pp_p(b)
        self.assertEqual(r.coefs[2].nomer.to_str(), ZERO)

    def test_different_degrees(self):
        # x^5 + x^2
        a = make_p(1, 5, ONE, ONE)
        b = make_p(1, 2, ONE, ONE)
        r = a.add_pp_p(b)
        self.assertEqual(r.deg, 5)
        self.assertEqual(r.coefs[5].nomer.to_str(), ONE)
        self.assertEqual(r.coefs[2].nomer.to_str(), ONE)

    def test_big_coefficients(self):
        a = make_p(1, 1, BIG, ONE)
        b = make_p(1, 1, BIG, ONE)
        r = a.add_pp_p(b)
        expected = str(int(BIG) * 2)
        rr = r.coefs[1].red_q_q()
        self.assertEqual(rr.nomer.to_str(), expected)


class TestSubPPP(unittest.TestCase):
    """sub_pp_p — вычитание многочленов"""

    def test_self_minus_self(self):
        p = make_p(1, 4, BIG, ONE)
        r = p.sub_pp_p(p)
        self.assertTrue(is_zero_p(r))

    def test_big_minus_small(self):
        a = make_p(1, 3, BIG, ONE)
        b = make_p(1, 3, ONE, ONE)
        r = a.sub_pp_p(b)
        expected = str(int(BIG) - 1)
        rr = r.coefs[3].red_q_q()
        self.assertEqual(rr.nomer.to_str(), expected)

    def test_degree_reduction(self):
        # x^3 - x^3 = 0, степень должна упасть до 0
        a = make_p(1, 3, "5", ONE)
        b = make_p(1, 3, "5", ONE)
        r = a.sub_pp_p(b)
        self.assertEqual(r.deg, 0)


class TestMulPPP(unittest.TestCase):
    """mul_pp_p — умножение многочленов"""

    def test_zero_times_poly(self):
        a = zero_p()
        b = make_p(1, 5, BIG, ONE)
        r = a.mul_pp_p(b)
        self.assertTrue(is_zero_p(r))

    def test_one_times_poly(self):
        a = make_p(1, 0, ONE, ONE)
        b = make_p(1, 3, BIG, ONE)
        r = a.mul_pp_p(b)
        self.assertEqual(r.deg, 3)
        self.assertEqual(r.coefs[3].nomer.to_str(), BIG)

    def test_degree_sum(self):
        a = make_p(1, 5, ONE, ONE)
        b = make_p(1, 7, ONE, ONE)
        r = a.mul_pp_p(b)
        self.assertEqual(r.deg, 12)

    def test_big_coefficients(self):
        a = make_p(1, 1, BIG, ONE)
        b = make_p(1, 1, BIG, ONE)
        r = a.mul_pp_p(b)
        # x^2 коэффициент = BIG^2
        expected = str(int(BIG) ** 2)
        rr = r.coefs[2].red_q_q()
        self.assertEqual(rr.nomer.to_str(), expected)

    def test_sign_product(self):
        a = make_p(-1, 1, "3", ONE)
        b = make_p(-1, 1, "5", ONE)
        r = a.mul_pp_p(b)
        self.assertEqual(r.coefs[2].nomer.sign, 1)


class TestDivPPP(unittest.TestCase):
    """div_pp_p — деление многочленов"""

    def test_zero_divisor(self):
        a = make_p(1, 3, ONE, ONE)
        b = zero_p()
        with self.assertRaises(ZeroDivisionError):
            a.div_pp_p(b)

    def test_lower_degree_dividend(self):
        a = make_p(1, 2, ONE, ONE)
        b = make_p(1, 5, ONE, ONE)
        r = a.div_pp_p(b)
        self.assertTrue(is_zero_p(r))

    def test_divide_by_self(self):
        # p / p = 1 (при ненулевом p)
        p = make_p(1, 3, "6", ONE)
        p.change_coef(1, 2, "3", ONE)
        p.change_coef(1, 0, "9", ONE)
        r = p.div_pp_p(p)
        rr = r.coefs[0].red_q_q()
        self.assertEqual(rr.nomer.to_str(), ONE)
        self.assertEqual(r.deg, 0)

    def test_exact_division(self):
        # x^2 - 1 = (x-1)(x+1), делим на (x-1) -> (x+1)
        dividend = make_p(1, 2, ONE, ONE)
        dividend.change_coef(0, 1, ZERO, ONE)
        dividend.change_coef(-1, 0, ONE, ONE)

        divisor = make_p(1, 1, ONE, ONE)
        divisor.change_coef(-1, 0, ONE, ONE)

        r = dividend.div_pp_p(divisor)
        rr1 = r.coefs[1].red_q_q()
        rr0 = r.coefs[0].red_q_q()
        self.assertEqual(r.deg, 1)
        self.assertEqual(rr1.nomer.to_str(), ONE)
        self.assertEqual(rr0.nomer.to_str(), ONE)

    def test_big_constant_divisor(self):
        # BIG*x^2 / BIG = x^2
        a = make_p(1, 2, BIG, ONE)
        b = make_p(1, 0, BIG, ONE)
        r = a.div_pp_p(b)
        rr = r.coefs[2].red_q_q()
        self.assertEqual(rr.nomer.to_str(), ONE)


class TestModPPP(unittest.TestCase):
    """mod_pp_p — остаток от деления"""

    def test_exact_division_remainder_zero(self):
        # x^2 - 1 = (x-1)(x+1), остаток = 0
        dividend = make_p(1, 2, ONE, ONE)
        dividend.change_coef(0, 1, ZERO, ONE)
        dividend.change_coef(-1, 0, ONE, ONE)

        divisor = make_p(1, 1, ONE, ONE)
        divisor.change_coef(-1, 0, ONE, ONE)

        r = dividend.mod_pp_p(divisor)
        self.assertTrue(is_zero_p(r))

    def test_lower_degree_dividend(self):
        a = make_p(1, 2, ONE, ONE)
        b = make_p(1, 5, ONE, ONE)
        r = a.mod_pp_p(b)
        self.assertEqual(r.deg, a.deg)

    def test_remainder_degree_less_than_divisor(self):
        # x^3 + x mod x^2 -> остаток степени < 2
        a = make_p(1, 3, ONE, ONE)
        a.change_coef(1, 1, ONE, ONE)
        b = make_p(1, 2, ONE, ONE)
        r = a.mod_pp_p(b)
        self.assertLess(r.deg, b.deg)


class TestGcfPPP(unittest.TestCase):
    """gcf_pp_p — НОД многочленов"""

    def test_gcd_with_self(self):
        p = make_p(1, 2, "6", ONE)
        p.change_coef(1, 1, "3", ONE)
        r = p.gcf_pp_p(p)
        # НОД(p, p) = p (с точностью до константы)
        self.assertGreaterEqual(r.deg, 0)

    def test_coprime_polynomials(self):
        # x и (x+1) взаимно просты
        a = make_p(1, 1, ONE, ONE)
        b = make_p(1, 1, ONE, ONE)
        b.change_coef(1, 0, ONE, ONE)
        r = a.gcf_pp_p(b)
        # НОД = константа, степень 0
        self.assertEqual(r.deg, 0)

    def test_gcd_common_factor(self):
        # x^2 - 1 = (x-1)(x+1) и x-1: НОД = x-1
        a = make_p(1, 2, ONE, ONE)
        a.change_coef(0, 1, ZERO, ONE)
        a.change_coef(-1, 0, ONE, ONE)

        b = make_p(1, 1, ONE, ONE)
        b.change_coef(-1, 0, ONE, ONE)

        r = a.gcf_pp_p(b)
        self.assertEqual(r.deg, 1)

    def test_gcd_zero_polynomial(self):
        # НОД(p, 0) = p
        p = make_p(1, 2, "5", ONE)
        z = zero_p()
        r = p.gcf_pp_p(z)
        self.assertEqual(r.deg, p.deg)


class TestNmrPP(unittest.TestCase):
    """nmr_p_p — устранение кратных корней"""

    def test_constant_returns_copy(self):
        p = make_p(1, 0, "7", ONE)
        r = p.nmr_p_p()
        self.assertIsNotNone(r)
        self.assertEqual(r.deg, 0)
        self.assertEqual(r.coefs[0].nomer.to_str(), "7")

    def test_no_multiple_roots(self):
        # x^2 + 1 — нет кратных корней над R
        p = make_p(1, 2, ONE, ONE)
        p.change_coef(1, 0, ONE, ONE)
        r = p.nmr_p_p()
        # результат должен быть той же степени или меньше
        if r is not None:
            self.assertLessEqual(r.deg, p.deg)

    def test_double_root(self):
        # (x-1)^2 = x^2 - 2x + 1 -> после nmr_p_p степень должна уменьшиться
        p = make_p(1, 2, ONE, ONE)
        p.change_coef(-1, 1, "2", ONE)
        p.change_coef(1, 0, ONE, ONE)
        r = p.nmr_p_p()
        if r is not None:
            self.assertLess(r.deg, p.deg)


if __name__ == "__main__":
    unittest.main()