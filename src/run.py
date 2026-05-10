from src.DataClasses.NaturalNumber import NaturalNumber
from src.DataClasses.IntNumber import IntNumber
from src.DataClasses.RationalNumber import RationalNumber
from src.DataClasses.Polinom import Polinom


funcs = {
    "nat": {
        "A com B": NaturalNumber.com_nn_d,
        "A != 0": NaturalNumber.nzer_n_b,
        "A + 1": NaturalNumber.add_1n_n,
        "A + B": NaturalNumber.add_nn_n,
        "|A - B|": NaturalNumber.sub_nn_n,
        "A * d": NaturalNumber.mul_nd_n,
        "A * 10^k": NaturalNumber.mul_nk_n,
        "A * B": NaturalNumber.mul_nn_n,
        "A - B * d": NaturalNumber.sub_ndn_n,
        "A / B -> d*10^k": NaturalNumber.div_nn_dk,
        "A // B": NaturalNumber.div_nn_n,
        "A % B": NaturalNumber.mod_nn_n,
        "НОД": NaturalNumber.gcf_nn_n,
        "НОК": NaturalNumber.lcm_nn_n
    },
    "int": {
            "abs A": IntNumber.abs_z_z,
            "sign A": IntNumber.sgn_z_d,
            "A * (-1)": IntNumber.mul_zm_z,
            "nat A -> int": IntNumber.trans_n_z,
            "int A -> nat": IntNumber.trans_z_n,
            "A + B": IntNumber.add_zz_z,
            "A - B": IntNumber.sub_zz_z,
            "A * B": IntNumber.mul_zz_z,
            "A // B": IntNumber.div_zz_z,
            "A % B": IntNumber.mod_zz_z
    },
    "rat": {
            "red A": RationalNumber.red_q_q,
            "A is int": RationalNumber.int_q_b,
            "int A -> rat": RationalNumber.trans_z_q,
            "rat A -> int": RationalNumber.trans_q_z,
            "A + B": RationalNumber.add_qq_q,
            "A - B": RationalNumber.sub_qq_q,
            "A * B": RationalNumber.mul_qq_q,
            "A / B": RationalNumber.div_qq_q
    },
    "pol": {# q rat, k nat
            "A + B": Polinom.add_pp_p,
            "A - B": Polinom.sub_pp_p,
            "A * q": Polinom.mul_pq_p,
            "A * x^k": Polinom.mul_pxk_p,
            "led A": Polinom.led_p_q,
            "deg A": Polinom.deg_p_n,
            "A(x) -> (c/d) * Q(x)": Polinom.fac_p_q,
            "A * B": Polinom.mul_pp_p,
            "A // B": Polinom.div_pp_p,
            "A % B": Polinom.mod_pp_p,
            "НОД": Polinom.gcf_pp_p,
            "A'(x)": Polinom.der_p_p,
            "A -> A_red": Polinom.nmr_p_p
    }
}


def run(func, data_type, argv):
    for arg in argv:
        if type(arg) == str and not arg.isdigit():
            return "Некорректные данные"

    print(func, data_type, argv)
    oper = funcs[data_type][func]
    result = None
    if data_type == 'nat':
        nat1 = NaturalNumber(argv[0])
        nat2 = NaturalNumber(argv[1])
        d = int(argv[2])
        k = int(argv[3])
        if d >= 10 or d < 0:
            return "d должна быть цифрой"

        try:
            if func in ["A != 0", "A + 1"]:
                result = oper(nat1)
            elif func == "A * d":
                result = oper(nat1, d)
            elif func == "A * 10^k":
                result = oper(nat1, k)
            elif func == "A - B * d":
                result = oper(nat1, nat2, d)
            else:
                result = oper(nat1, nat2)
        except ZeroDivisionError:
            return "Невозможно делить на 0"
        except ValueError:
            return "Вычитаемое больше уменьшаемого"

        if type(result) == NaturalNumber:
            return result.to_str()
        if type(result) == tuple:
            return f"{result[0]}*10^{result[1]}"
        return str(result)
    elif data_type == 'int':
        sign1 = 0 if argv[0] == '0' else [1, -1][argv[-1][0]]
        sign2 = 0 if argv[1] == '0' else [1, -1][argv[-1][1]]
        #print(sign1, sign2)
        int1 = IntNumber(sign1, argv[0])
        int2 = IntNumber(sign2, argv[1])

        try:
            if func in ["abs A", "sign A", "A * (-1)", "nat A -> int", "int A -> nat"]:
                result = oper(int1)
            else:
                result = oper(int1, int2)

            if type(result) == NaturalNumber:
                return result.to_str()
            elif type(result) == int:
                return ['0', 'Плюс', 'Минус'][result]
            else:
                #print(result.sign)
                return f"{['', '+', '-'][result.sign]}{result.to_str()}"\
                        if result.sign != 0 else\
                        f"{result.to_str()}"
        except ZeroDivisionError:
            return "Деление на 0 невозможно"
    elif data_type == 'rat':
        if argv[1] == "0" or argv[3] == "0":
            return "Знаменатель не может равнятся 0"
        sign1 = 0 if argv[0] == '0' else [1, -1][argv[-1][0]]
        sign2 = 0 if argv[1] == '0' else [1, -1][argv[-1][1]]
        rat1 = RationalNumber(sign1, argv[0], argv[1])
        rat2 = RationalNumber(sign2, argv[2], argv[3])

        try:
            if func == "int A -> rat":
                result = oper(rat1.nomer)
            elif func in ["red A", "A is int", "rat A -> int"]:
                result = oper(rat1)
            else:
                result = oper(rat1, rat2)
            if type(result) == RationalNumber:
                return result.to_str()
            elif type(result) == IntNumber:
                return f"{['', '+', '-'][result.sign]}{result.to_str()}"\
                            if result.sign != 0 else\
                            f"{result.to_str()}"
            else:
                return str(result)
        except ValueError:
            return "Знаменатель не равен 1"
    else:
        q = RationalNumber(argv[-1], argv[3], argv[4])
        k = int(argv[2])

        try:
            if func == "A * q":
                result = oper(argv[0], q)
            elif func == "A * x^k":
                result = oper(argv[0], k)
            elif func in ["led A", "deg A", "A(x) -> (c/d) * Q(x)", "A'(x)", "A -> A_red"]:
                result = oper(argv[0])
            else:
                result = oper(argv[0], argv[1])
        except Exception:
            return "some error"
        if type(result) == Polinom:
            return print_polynom(result)
        elif type(result) == RationalNumber:
            return result.to_str()
        else:
            return str(result)


def print_polynom(polinom):
    result = []
    print('1')
    parts = polinom.coefs.keys()
    for part in parts:
        coef = polinom.coefs[part]
        if coef.nomer.digits != [0]:
            coef_str = f"({['', '+', '-'][coef.nomer.sign]}{coef.nomer.to_str()}/{coef.denomer.to_str()})*x^{part}"
            result.append(coef_str)
    return " + ".join(result)