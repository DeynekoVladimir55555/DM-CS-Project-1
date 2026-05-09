from src.DataClasses.NaturalNumber import NaturalNumber


funcs = {
    "nat":{
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
    }
}


def run(func, data_type, argv):
    print(func, data_type, argv)
    oper = funcs[data_type][func]
    result = None
    if data_type == 'nat':
        nat1 = NaturalNumber(argv[0])
        nat2 = NaturalNumber(argv[1])
        d = int(argv[2])
        k = int(argv[3])

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



"""
self.natCombo.addItems([
            
        ])
        self.intCombo.addItems([
            "abs A",
            "A com 0",
            "A * (-1)",
            "nat -> int",
            "int -> nat",
            "A + B",
            "A - B",
            "A * B",
            "A // B",
            "A % B"
        ])
        self.ratCombo.addItems([
            "red A",
            "A is int",
            "int -> rat",
            "rat -> int",
            "A + B",
            "A - B",
            "A * B",
            "A / B"
        ])
        self.polCombo.addItems([
            "A + B",
            "A - B",
            "A * q",
            "A * x^k",
            "led A",
            "deg A",
            "A(x) -> (c/d) * Q(x)",
            "A * B",
            "A // B",
            "A % B",
            "НОД",
            "A'(x)",
            "A -> A_red"
        ])
"""