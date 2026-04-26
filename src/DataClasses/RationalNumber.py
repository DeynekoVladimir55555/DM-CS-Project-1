from NaturalNumber import NaturalNumber
from IntNumber import IntNumber


class RationalNumber:
    """
    Реализация больших рациональных чисел
    Атрибуты:
        sign (int): знак числа, 1 - плюс, 0 - для числа 0, -1 - минус.
        nomer (str): строковое представление числителя.
        denomer (str): строковое представление знаменятеля.
    """
    def __init__(self, sign=0, nomer="", denomer=""):
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
    
    # Выполнила Бондаренко Полина 5381
    @staticmethod
    def trans_z_q(int_num: IntNumber):
        """
        Преобразование целого в дробное.
        Аргументы:
            integer_number - целое число (IntNumber).
        """
        return RationalNumber(int_num.sign, int_num.to_str(), "1")
    
if __name__ == "__main__":
    rn = RationalNumber(int(input()), input(), input())
    print(rn)