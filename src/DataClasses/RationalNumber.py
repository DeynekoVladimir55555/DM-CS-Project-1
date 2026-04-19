from src.DataClasses.NaturalNumber import NaturalNumber
from src.DataClasses.IntNumber import IntNumber


class RationalNumber:
    """
    Реализация больших рациональных чисел
    Атрибуты:
        sign (int): знак числа, 1 - минус, 0 - плюс.
        nomer (str): строковое представление числителя.
        denomer (str): строковое представление знаменятеля.
    """
    def __init__(self, sign, nomer, denomer):
        self.nomer = IntNumber(sign, nomer)
        self.denomer = NaturalNumber(denomer)

    def __str__(self):
        str_nomer = str(self.nomer).replace('\n', '\n\t')
        str_denomer = str(self.denomer).replace('\n', '\n\t')

        return (
            "RationalNumber: {\n\t"
            f"Числитель {str_nomer}, \n\t"
            f"Знаменатель {str_denomer}\n"
            "}"
        )


if __name__ == "__main__":
    rn = RationalNumber(int(input()), input(), input())
    print(rn)