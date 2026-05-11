import unittest
from src.DataClasses.IntNumber import IntNumber


class TestIntNumberLarge(unittest.TestCase):

    # --- trans_n_z ---
    def test_trans_n_z_large(self):
        from NaturalNumber import NaturalNumber
        nat = NaturalNumber("123456789012345678901234567890")
        result = IntNumber.trans_n_z(nat)
        self.assertEqual(result.sign, 1)
        self.assertEqual(result.to_str(), "123456789012345678901234567890")

    # --- trans_z_n ---
    def test_trans_z_n_large(self):
        z = IntNumber(1, "999999999999999999999999999999")
        result = z.trans_z_n()
        self.assertEqual(result.to_str(), "999999999999999999999999999999")

    # --- mul_zm_z ---
    def test_mul_zm_z_large_positive(self):
        z = IntNumber(1, "123456789012345678901234567890")
        result = z.mul_zm_z()
        self.assertEqual(result.sign, -1)
        self.assertEqual(result.to_str(), "123456789012345678901234567890")

    def test_mul_zm_z_large_negative(self):
        z = IntNumber(-1, "123456789012345678901234567890")
        result = z.mul_zm_z()
        self.assertEqual(result.sign, 1)

    # --- abs_z_z ---
    def test_abs_z_z_large_negative(self):
        z = IntNumber(-1, "987654321098765432109876543210")
        result = z.abs_z_z()
        self.assertEqual(result.sign, 1)
        self.assertEqual(result.to_str(), "987654321098765432109876543210")

    def test_abs_z_z_large_positive(self):
        z = IntNumber(1, "987654321098765432109876543210")
        result = z.abs_z_z()
        self.assertEqual(result.sign, 1)
        self.assertEqual(result.to_str(), "987654321098765432109876543210")

    # --- add_zz_z ---
    def test_add_large_both_positive(self):
        a = IntNumber(1, "999999999999999999999999999999")
        b = IntNumber(1, "000000000000000000000000000001")
        result = a.add_zz_z(b)
        self.assertEqual(result.to_str(), "1000000000000000000000000000000")

    def test_add_large_opposite_signs(self):
        a = IntNumber(1,  "999999999999999999999999999999")
        b = IntNumber(-1, "999999999999999999999999999998")
        result = a.add_zz_z(b)
        self.assertEqual(result.sign, 1)
        self.assertEqual(result.to_str(), "1")

    def test_add_large_cancel(self):
        a = IntNumber(1,  "123456789012345678901234567890")
        b = IntNumber(-1, "123456789012345678901234567890")
        result = a.add_zz_z(b)
        self.assertEqual(result.sign, 0)

    def test_add_large_both_negative(self):
        a = IntNumber(-1, "500000000000000000000000000000")
        b = IntNumber(-1, "500000000000000000000000000000")
        result = a.add_zz_z(b)
        self.assertEqual(result.sign, -1)
        self.assertEqual(result.to_str(), "1000000000000000000000000000000")

    # --- sub_zz_z ---
    def test_sub_large_basic(self):
        a = IntNumber(1, "1000000000000000000000000000000")
        b = IntNumber(1, "999999999999999999999999999999")
        result = a.sub_zz_z(b)
        self.assertEqual(result.sign, 1)
        self.assertEqual(result.to_str(), "1")

    def test_sub_large_self(self):
        a = IntNumber(1, "123456789012345678901234567890")
        result = a.sub_zz_z(a)
        self.assertEqual(result.sign, 0)

    def test_sub_large_negative_result(self):
        a = IntNumber(1, "1")
        b = IntNumber(1, "999999999999999999999999999999")
        result = a.sub_zz_z(b)
        self.assertEqual(result.sign, -1)
        self.assertEqual(result.to_str(), "999999999999999999999999999998")

    def test_sub_large_negative_minus_positive(self):
        a = IntNumber(-1, "500000000000000000000000000000")
        b = IntNumber(1,  "500000000000000000000000000000")
        result = a.sub_zz_z(b)
        self.assertEqual(result.sign, -1)
        self.assertEqual(result.to_str(), "1000000000000000000000000000000")

    # --- mul_zz_z ---
    def test_mul_large_both_positive(self):
        a = IntNumber(1, "123456789012345678901234567890")
        b = IntNumber(1, "1")
        self.assertEqual(a.mul_zz_z(b).to_str(), "123456789012345678901234567890")

    def test_mul_large_opposite_signs(self):
        a = IntNumber(1,  "100000000000000000000000000000")
        b = IntNumber(-1, "100000000000000000000000000000")
        result = a.mul_zz_z(b)
        self.assertEqual(result.sign, -1)
        self.assertEqual(result.to_str(), "10000000000000000000000000000000000000000000000000000000000")

    def test_mul_large_both_negative(self):
        a = IntNumber(-1, "999999999999999999999999999999")
        b = IntNumber(-1, "999999999999999999999999999999")
        result = a.mul_zz_z(b)
        self.assertEqual(result.sign, 1)
        expected = str(999999999999999999999999999999 ** 2)
        self.assertEqual(result.to_str(), expected)

    def test_mul_large_by_zero(self):
        a = IntNumber(1, "999999999999999999999999999999")
        b = IntNumber(0, "0")
        result = a.mul_zz_z(b)
        self.assertEqual(result.sign, 0)

    # --- div_zz_z ---
    def test_div_large_both_positive(self):
        a = IntNumber(1, "1000000000000000000000000000000")
        b = IntNumber(1, "1000000000000000000000000000000")
        result = a.div_zz_z(b)
        self.assertEqual(result.to_str(), "1")

    def test_div_large_opposite_signs(self):
        a = IntNumber(1,  "1000000000000000000000000000000")
        b = IntNumber(-1, "10")
        result = a.div_zz_z(b)
        self.assertEqual(result.sign, -1)
        self.assertEqual(result.to_str(), "100000000000000000000000000000")

    def test_div_large_smaller_by_larger(self):
        a = IntNumber(1, "1")
        b = IntNumber(1, "999999999999999999999999999999")
        result = a.div_zz_z(b)
        self.assertEqual(result.sign, 1)
        self.assertEqual(result.to_str(), "0")

    def test_div_zero_by_large(self):
        a = IntNumber(0, "0")
        b = IntNumber(1, "999999999999999999999999999999")
        result = a.div_zz_z(b)
        self.assertEqual(result.sign, 0)

    def test_div_large_by_zero_raises(self):
        a = IntNumber(1, "999999999999999999999999999999")
        b = IntNumber(0, "0")
        with self.assertRaises(ZeroDivisionError):
            a.div_zz_z(b)

    # --- mod_zz_z ---
    def test_mod_large_no_remainder(self):
        a = IntNumber(1, "1000000000000000000000000000000")
        b = IntNumber(1, "10")
        result = a.mod_zz_z(b)
        self.assertEqual(result.sign, 0)

    def test_mod_large_with_remainder(self):
        a = IntNumber(1, "1000000000000000000000000000007")
        b = IntNumber(1, "10")
        result = a.mod_zz_z(b)
        self.assertEqual(result.to_str(), "7")

    def test_mod_large_by_one(self):
        a = IntNumber(1, "987654321098765432109876543210")
        b = IntNumber(1, "1")
        result = a.mod_zz_z(b)
        self.assertEqual(result.sign, 0)

    def test_mod_large_smaller_by_larger(self):
        a = IntNumber(1, "7")
        b = IntNumber(1, "999999999999999999999999999999")
        result = a.mod_zz_z(b)
        self.assertEqual(result.to_str(), "7")


if __name__ == "__main__":
    unittest.main()
