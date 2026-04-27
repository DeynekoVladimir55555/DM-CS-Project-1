from NaturalNumber import NaturalNumber
from IntNumber import IntNumber
from ..IntNumbers.IntFunctions import mul_z_z


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

    def __mul__(self, other):
        if isinstance(other, int):
            mul = IntNumber(1, str(other))
            res = RationalNumber(self.nomer.sign, "", self.denomer.to_str())
            res.nomer = mul_z_z(mul, self.nomer)

            return res

        return None

    # Выполнила Зуева Екатерина 5381
    def red_q_q(self):
        """
        Сокращение дроби. (в процессе)
        """

    # Выполнила Зуева Екатерина 5381
    def int_q_b(self):
        """
        Проверка сокращенного дробного на целое.
        Если рациональное число является целым,
        то возвращает True, иначе - False.
        """
        self.red_q_q()
        return self.denomer.to_str() == "1"
    
    # Выполнила Бондаренко Полина 5381
    def trans_z_q(self, int_num: IntNumber):
        """
        Преобразование целого в дробное.
        Аргументы:
            int_num (IntNumber): целое число
        """
        self.nomer = int_num
        self.denomer = NaturalNumber("1")

    # Выполнила Бондаренко Полина 5381
    def trans_q_z(self) -> IntNumber:
        """
        Преобразование сокращенного дробного
        в целое (если знаменатель равен 1)
        """
        if self.denomer.to_str() != "1":
            raise ValueError("Знаменатель не равен 1, преобразование невозможно")

        return self.nomer
    
if __name__ == "__main__":
    rn = RationalNumber(int(input()), input(), input())
    print(rn)