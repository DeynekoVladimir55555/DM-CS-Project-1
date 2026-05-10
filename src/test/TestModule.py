from src.DataClasses.NaturalNumber import NaturalNumber
from src.DataClasses.IntNumber import IntNumber
from src.DataClasses.RationalNumber import RationalNumber
from src.DataClasses.Polinom import Polinom


def test_main():
    return test()


def test():
    pass


def get_operations():
    opers = {}
    opers['nat'] = get_nat()
    opers['int'] = get_int()
    opers['rat'] = get_rat()
    opers['pol'] = get_pol()
    return opers


def get_nat():
    nat = {}

    nat[1] = NaturalNumber.com_nn_d
    nat[2] = NaturalNumber.nzer_n_b
    nat[3] = NaturalNumber.add_1n_n
    nat[4] = NaturalNumber.add_nn_n
    nat[5] = sub_nn_n
    nat[6] = NaturalNumber.mul_nd_n
    nat[7] = NaturalNumber.mul_nk_n
    #nat[8] = mul_n_n
    #nat[9] = sub_ndn_n
    #nat[10] = div_nn_dk
    #nat[11] = div_nn_n
    #nat[12] = mod_nn_n
    #nat[13] = GCF
    #nat[14] = LMC


    return nat


def get_int():
    ints = {}

    # ints[1] =
    # ints[2] =
    # ints[3] =
    # ints[4] =
    # ints[5] =
    # ints[6] =
    # ints[7] =
    # ints[8] =
    # ints[9] =
    # ints[10] =

    return ints


def get_rat():
    rat = {}

    # rat[1] =
    # rat[2] =
    # rat[3] =
    # rat[4] =
    # rat[5] =
    # rat[6] =
    # rat[7] =
    # rat[8] =

    return rat


def get_pol():
    pol = {}

    # pol[1] =
    # pol[2] =
    # pol[3] =
    # pol[4] =
    # pol[5] =
    # pol[6] =
    # pol[7] =
    # pol[8] =
    # pol[9] =
    # pol[10] =
    # pol[11] =
    # pol[12] =
    # pol[13] =

    return pol


if __name__ == "__main__":
    test_main()