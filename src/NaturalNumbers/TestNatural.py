import unittest
from src.DataClasses.NaturalNumber import NaturalNumber


BIG = "9" * 50
BIG2 = "9" * 25
BIG3 = "1" + "0" * 50  # 10^49
ONE = "1"
ZERO = "0"
TWO = "2"


def N(s):
    return NaturalNumber(s)


class TestNzerNB(unittest.TestCase):
    """nzer_n_b — проверка на ноль"""

    def test_zero(self):
        self.assertFalse(N(ZERO).nzer_n_b())

    def test_one(self):
        self.assertTrue(N(ONE).nzer_n_b())

    def test_big(self):
        self.assertTrue(N(BIG).nzer_n_b())

    def test_big_with_leading_zero_string(self):
        # NaturalNumber не должен сломаться на "0000...0001"
        self.assertTrue(N("1").nzer_n_b())


class TestComNND(unittest.TestCase):
    """com_nn_d — сравнение чисел"""

    def test_equal(self):
        self.assertEqual(N(BIG).com_nn_d(N(BIG)), 0)

    def test_greater(self):
        self.assertEqual(N(BIG).com_nn_d(N(BIG2)), 2)

    def test_less(self):
        self.assertEqual(N(BIG2).com_nn_d(N(BIG)), 1)

    def test_zero_vs_zero(self):
        self.assertEqual(N(ZERO).com_nn_d(N(ZERO)), 0)

    def test_zero_vs_big(self):
        self.assertEqual(N(ZERO).com_nn_d(N(BIG)), 1)

    def test_big_vs_zero(self):
        self.assertEqual(N(BIG).com_nn_d(N(ZERO)), 2)

    def test_same_length_differ_last_digit(self):
        a = "9" * 49 + "8"
        b = BIG
        self.assertEqual(N(a).com_nn_d(N(b)), 1)

    def test_power_of_ten_vs_big(self):
        # 10^49 < 9*10^49 + ...
        self.assertEqual(N(BIG3).com_nn_d(N(BIG)), 2)


class TestAdd1NN(unittest.TestCase):
    """add_1n_n — прибавление 1"""

    def test_zero_plus_one(self):
        n = N(ZERO)
        n = n.add_1n_n()
        self.assertEqual(n.to_str(), ONE)

    def test_nine_carry(self):
        n = N("9")
        n = n.add_1n_n()
        self.assertEqual(n.to_str(), "10")

    def test_all_nines_carry(self):
        # 999...9 + 1 = 1000...0
        n = N(BIG)
        n = n.add_1n_n()
        self.assertEqual(n.to_str(), BIG3)

    def test_big_no_carry(self):
        s = "9" * 49 + "8"
        n = N(s)
        n = n.add_1n_n()
        self.assertEqual(n.to_str(), BIG)


class TestAddNNN(unittest.TestCase):
    """add_nn_n — сложение"""

    def test_zero_plus_zero(self):
        r = N(ZERO).add_nn_n(N(ZERO))
        self.assertEqual(r.to_str(), ZERO)

    def test_zero_plus_big(self):
        r = N(ZERO).add_nn_n(N(BIG))
        self.assertEqual(r.to_str(), BIG)

    def test_big_plus_zero(self):
        r = N(BIG).add_nn_n(N(ZERO))
        self.assertEqual(r.to_str(), BIG)

    def test_big_plus_one(self):
        r = N(BIG).add_nn_n(N(ONE))
        self.assertEqual(r.to_str(), BIG3)

    def test_big_plus_big(self):
        r = N(BIG).add_nn_n(N(BIG))
        expected = str(int(BIG) * 2)
        self.assertEqual(r.to_str(), expected)

    def test_commutative(self):
        a = N(BIG)
        b = N(BIG2)
        r1 = a.add_nn_n(b)
        r2 = b.add_nn_n(a)
        self.assertEqual(r1.to_str(), r2.to_str())

    def test_different_lengths(self):
        r = N(BIG).add_nn_n(N(BIG2))
        expected = str(int(BIG) + int(BIG2))
        self.assertEqual(r.to_str(), expected)


class TestSubNNN(unittest.TestCase):
    """sub_nn_n — вычитание"""

    def test_equal_gives_zero(self):
        r = N(BIG).sub_nn_n(N(BIG))
        self.assertEqual(r.to_str(), ZERO)

    def test_big_minus_one(self):
        r = N(BIG).sub_nn_n(N(ONE))
        expected = str(int(BIG) - 1)
        self.assertEqual(r.to_str(), expected)

    def test_big_minus_big2(self):
        r = N(BIG).sub_nn_n(N(BIG2))
        expected = str(int(BIG) - int(BIG2))
        self.assertEqual(r.to_str(), expected)

    def test_power_of_ten_minus_one(self):
        # 10^49 - 1 = 999...9 (49 девяток)
        r = N(BIG3).sub_nn_n(N(ONE))
        self.assertEqual(r.to_str(), "9" * 50)

    def test_subtract_zero(self):
        r = N(BIG).sub_nn_n(N(ZERO))
        self.assertEqual(r.to_str(), BIG)


class TestMulNdN(unittest.TestCase):
    """mul_nd_n — умножение на цифру"""

    def test_multiply_by_zero(self):
        r = N(BIG).mul_nd_n(0)
        self.assertEqual(r.to_str(), ZERO)

    def test_multiply_by_one(self):
        r = N(BIG).mul_nd_n(1)
        self.assertEqual(r.to_str(), BIG)

    def test_multiply_by_nine(self):
        r = N(BIG).mul_nd_n(9)
        expected = str(int(BIG) * 9)
        self.assertEqual(r.to_str(), expected)

    def test_carry_propagation(self):
        # 999...9 * 2 = 1999...8
        r = N(BIG).mul_nd_n(2)
        expected = str(int(BIG) * 2)
        self.assertEqual(r.to_str(), expected)

    def test_zero_times_digit(self):
        r = N(ZERO).mul_nd_n(9)
        self.assertEqual(r.to_str(), ZERO)


class TestMulNkN(unittest.TestCase):
    """mul_nk_n — умножение на 10^k"""

    def test_k_zero(self):
        r = N(BIG).mul_nk_n(0)
        self.assertEqual(r.to_str(), BIG)

    def test_k_one(self):
        r = N("123").mul_nk_n(1)
        self.assertEqual(r.to_str(), "1230")

    def test_k_big(self):
        r = N(ONE).mul_nk_n(50)
        self.assertEqual(r.to_str(), "1" + "0" * 50)

    def test_zero_times_power(self):
        r = N(ZERO).mul_nk_n(50)
        self.assertEqual(r.to_str(), ZERO)

    def test_big_times_power(self):
        r = N(BIG).mul_nk_n(25)
        expected = BIG + "0" * 25
        self.assertEqual(r.to_str(), expected)


class TestMulNNN(unittest.TestCase):
    """mul_nn_n — умножение"""

    def test_zero_times_big(self):
        r = N(ZERO).mul_nn_n(N(BIG))
        self.assertEqual(r.to_str(), ZERO)

    def test_one_times_big(self):
        r = N(ONE).mul_nn_n(N(BIG))
        self.assertEqual(r.to_str(), BIG)

    def test_big_times_one(self):
        r = N(BIG).mul_nn_n(N(ONE))
        self.assertEqual(r.to_str(), BIG)

    def test_commutative(self):
        a = N(BIG2)
        b = N("12345678901234567890")
        r1 = a.mul_nn_n(b)
        r2 = b.mul_nn_n(a)
        self.assertEqual(r1.to_str(), r2.to_str())

    def test_big_times_big(self):
        r = N(BIG2).mul_nn_n(N(BIG2))
        expected = str(int(BIG2) ** 2)
        self.assertEqual(r.to_str(), expected)

    def test_power_of_ten(self):
        # 10^25 * 10^25 = 10^50
        r = N(BIG3[:26]).mul_nn_n(N(BIG3[:26]))
        expected = str(int(BIG3[:26]) ** 2)
        self.assertEqual(r.to_str(), expected)


class TestDivNNN(unittest.TestCase):
    """div_nn_n — целочисленное деление"""

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            N(BIG).div_nn_n(N(ZERO))

    def test_smaller_divided_by_bigger(self):
        r = N(ONE).div_nn_n(N(BIG))
        self.assertEqual(r.to_str(), ZERO)

    def test_equal_divided(self):
        r = N(BIG).div_nn_n(N(BIG))
        self.assertEqual(r.to_str(), ONE)

    def test_big_divided_by_one(self):
        r = N(BIG).div_nn_n(N(ONE))
        self.assertEqual(r.to_str(), BIG)

    def test_big_divided_by_two(self):
        r = N(BIG).div_nn_n(N(TWO))
        expected = str(int(BIG) // 2)
        self.assertEqual(r.to_str(), expected)

    def test_power_of_ten(self):
        # 10^50 / 10^25 = 10^25
        a = "1" + "0" * 50
        b = "1" + "0" * 25
        r = N(a).div_nn_n(N(b))
        self.assertEqual(r.to_str(), b)

    def test_exact_large_division(self):
        # (BIG2 * 7) / 7 = BIG2
        product = str(int(BIG2) * 7)
        r = N(product).div_nn_n(N("7"))
        self.assertEqual(r.to_str(), BIG2)


class TestModNNN(unittest.TestCase):
    """mod_nn_n — остаток от деления"""

    def test_big_mod_self(self):
        r = N(BIG).mod_nn_n(N(BIG))
        self.assertEqual(r.to_str(), ZERO)

    def test_big_mod_one(self):
        r = N(BIG).mod_nn_n(N(ONE))
        self.assertEqual(r.to_str(), ZERO)

    def test_big_mod_two_even(self):
        # BIG = 999...9 нечётное, BIG+1 = 10^50 чётное
        even = str(int(BIG) + 1)
        r = N(even).mod_nn_n(N(TWO))
        self.assertEqual(r.to_str(), ZERO)

    def test_big_mod_two_odd(self):
        r = N(BIG).mod_nn_n(N(TWO))
        self.assertEqual(r.to_str(), ONE)

    def test_smaller_mod_bigger(self):
        r = N(ONE).mod_nn_n(N(BIG))
        self.assertEqual(r.to_str(), ONE)

    def test_exact_remainder(self):
        # (BIG2 * 3 + 7) mod 3 = 7 mod 3 = 1
        dividend = str(int(BIG2) * 3 + 7)
        r = N(dividend).mod_nn_n(N("3"))
        self.assertEqual(r.to_str(), "1")

    def test_consistency_with_div(self):
        # a = (a // b) * b + (a % b)
        a = N(BIG)
        b = N("123456789")
        q = a.div_nn_n(b)
        r = a.mod_nn_n(b)
        reconstructed = b.mul_nn_n(q).add_nn_n(r)
        self.assertEqual(reconstructed.to_str(), BIG)


class TestGcfNNN(unittest.TestCase):
    """gcf_nn_n — НОД"""

    def test_gcd_self(self):
        r = N(BIG).gcf_nn_n(N(BIG))
        self.assertEqual(r.to_str(), BIG)

    def test_gcd_with_one(self):
        r = N(BIG).gcf_nn_n(N(ONE))
        self.assertEqual(r.to_str(), ONE)

    def test_gcd_commutative(self):
        a = N(BIG)
        b = N(BIG2)
        r1 = a.gcf_nn_n(b)
        r2 = b.gcf_nn_n(a)
        self.assertEqual(r1.to_str(), r2.to_str())

    def test_gcd_multiples(self):
        # НОД(2*BIG2, 4*BIG2) = 2*BIG2
        a = str(int(BIG2) * 2)
        b = str(int(BIG2) * 4)
        r = N(a).gcf_nn_n(N(b))
        self.assertEqual(r.to_str(), a)

    def test_gcd_coprime(self):
        # два последовательных числа взаимно просты
        r = N(BIG).gcf_nn_n(N(str(int(BIG) + 1)))
        self.assertEqual(r.to_str(), ONE)

    def test_gcd_powers_of_two(self):
        # НОД(2^100, 2^50) = 2^50
        a = str(2 ** 100)
        b = str(2 ** 50)
        r = N(a).gcf_nn_n(N(b))
        self.assertEqual(r.to_str(), b)


class TestLcmNNN(unittest.TestCase):
    """lcm_nn_n — НОК"""

    def test_lcm_self(self):
        r = N(BIG2).lcm_nn_n(N(BIG2))
        self.assertEqual(r.to_str(), BIG2)

    def test_lcm_with_one(self):
        r = N(BIG).lcm_nn_n(N(ONE))
        self.assertEqual(r.to_str(), BIG)

    def test_lcm_commutative(self):
        a = N("12345678901234567890")
        b = N("98765432109876543210")
        r1 = a.lcm_nn_n(b)
        r2 = b.lcm_nn_n(a)
        self.assertEqual(r1.to_str(), r2.to_str())

    def test_lcm_multiples(self):
        # НОК(2, 4) = 4
        r = N(TWO).lcm_nn_n(N("4"))
        self.assertEqual(r.to_str(), "4")

    def test_lcm_coprime(self):
        # НОК(a, b) = a*b если взаимно просты
        a = "17"
        b = "19"
        r = N(a).lcm_nn_n(N(b))
        expected = str(17 * 19)
        self.assertEqual(r.to_str(), expected)

    def test_lcm_powers_of_two(self):
        # НОК(2^50, 2^100) = 2^100
        a = str(2 ** 50)
        b = str(2 ** 100)
        r = N(a).lcm_nn_n(N(b))
        self.assertEqual(r.to_str(), b)

    def test_lcm_identity(self):
        # НОД * НОК = a * b
        a = N("123456789012345678")
        b = N("987654321098765432")
        gcd = a.gcf_nn_n(b)
        lcm = a.lcm_nn_n(b)
        lhs = gcd.mul_nn_n(lcm)
        rhs = a.mul_nn_n(b)
        self.assertEqual(lhs.to_str(), rhs.to_str())


if __name__ == "__main__":
    unittest.main()