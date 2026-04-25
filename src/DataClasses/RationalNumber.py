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
    #Выолнила: Бондаренко Полина 5381
    def trans_z_q(self, integer_number):
        """
        Преобразование целого в дробное.
        Аргументы:
            integer_number - целое число (IntNumber).
        """
        self.nomer = integer_number
        self.denomer = NaturalNumber("1")

    #Выолнила: Бондаренко Полина 5381
    def trans_q_z(self):
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