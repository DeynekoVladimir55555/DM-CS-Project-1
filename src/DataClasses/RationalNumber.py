from src.DataClasses.NaturalNumber import NaturalNumber
from src.DataClasses.IntNumber import IntNumber


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

    def to_str(self):
        sign = ['', '+', '-'][self.nomer.sign]
        return f"{sign}{self.nomer.to_str()}/{self.denomer.to_str()}"

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
            rat_num = RationalNumber(1, str(other), "1")
            mul = self.mul_qq_q(rat_num)
            return mul.red_q_q()

        return None

    # Выполнила Зуева Екатерина 5381
    def red_q_q(self):
        """
        Сокращение дроби.
        Нахождение НОД, затем сокращение
        числителя и знаменателя на НОД.
        """
        if self.nomer.to_str() == "0":
            result = RationalNumber()
            result.nomer = self.nomer
            result.denomer = NaturalNumber("1")
            return result

        sign = self.nomer.sign
        a = IntNumber.trans_z_n(self.nomer)
        b = self.denomer

        nod = a.gcf_nn_n(b)

        result = RationalNumber()
        if nod.to_str() != "1":
            result.nomer = IntNumber(sign, (a.div_nn_n(nod).to_str()))
            result.denomer = b.div_nn_n(nod)
        else:
            result.nomer = self.nomer
            result.denomer = self.denomer

        return result

    # Выполнила Зуева Екатерина 5381
    def int_q_b(self):
        """
        Проверка сокращенного дробного на целое.
        Если рациональное число является целым,
        то возвращает True, иначе - False.
        """
        return self.denomer.to_str() == "1"

    # Выполнила Бондаренко Полина 5381
    @staticmethod
    def trans_z_q(int_num: IntNumber):
        """
        Преобразование целого в дробное.
        Аргументы:
            int_num (IntNumber): целое число
        """
        return RationalNumber(int_num.sign, int_num.to_str(), "1")

    # Выполнила Бондаренко Полина 5381
    def trans_q_z(self) -> IntNumber:
        """
        Преобразование сокращенного дробного
        в целое (если знаменатель равен 1)
        """
        if not self.int_q_b():
            raise ValueError("Знаменатель не равен 1, преобразование невозможно")

        return self.nomer

    # Выполнила Бондаренко Полина 5381
    def mul_qq_q(self, other):
        """
        Умножение двух рациональных чисел.
        Аргументы:
            other (RationalNumber): второй множитель
        Возвращает:
            RationalNumber – новое рациональное число (несокращённое)
        Используется: mul_zz_z, mul_nn_n.
        """
        new_nomer = self.nomer.mul_zz_z(other.nomer)
        new_denomer = self.denomer.mul_nn_n(other.denomer)
        result = RationalNumber()
        result.nomer = new_nomer
        result.denomer = new_denomer
        return result

    # Выполнила Романенко Вика 5387
    def sub_qq_q(self, other):
        """
        Вычитание дробей: self - other.
        Возвращает новый объект RationalNumber.
        """
        if self.nomer.to_str() == "0" and other.nomer.to_str() == "0":
            return RationalNumber(0, "0", "1")

        if self.nomer.to_str() == "0":
            result = RationalNumber()
            result.nomer = other.nomer.mul_zm_z()
            result.denomer = other.denomer
            return result

        if other.nomer.to_str() == "0":
            result = RationalNumber()
            result.nomer = self.nomer
            result.denomer = self.denomer
            return result

        lcm = self.denomer.lcm_nn_n(other.denomer)

        k1 = lcm.div_nn_n(self.denomer)
        k2 = lcm.div_nn_n(other.denomer)

        a = self.nomer.mul_zz_z(IntNumber.trans_n_z(k1))
        b = other.nomer.mul_zz_z(IntNumber.trans_n_z(k2))
        new_nomer = a.sub_zz_z(b)

        result = RationalNumber()
        result.nomer = new_nomer
        result.denomer = lcm

        return result

    # Выполнил Килин Сергей 5381
    def add_qq_q(self, number2):
        """
        Сложение двух рациональных чисел.
        Аргументы:
            number2 (RationalNumber): второе рациональное число
        Возвращает:
            Новое RationalNumber - результат суммы
        """
        if self.nomer.sign == 0 and number2.nomer.sign == 0:
            return RationalNumber(0, "0", "1")

        if self.nomer.sign == 0:
            result = RationalNumber()
            result.nomer = number2.nomer
            result.denomer = number2.denomer
            return result

        if number2.nomer.sign == 0:
            result = RationalNumber()
            result.nomer = self.nomer
            result.denomer = self.denomer
            return result

        lcm = self.denomer.lcm_nn_n(number2.denomer)
        k1 = lcm.div_nn_n(self.denomer)
        k2 = lcm.div_nn_n(number2.denomer)

        a = self.nomer.mul_zz_z(IntNumber.trans_n_z(k1))
        b = number2.nomer.mul_zz_z(IntNumber.trans_n_z(k2))
        new_nomer = a.add_zz_z(b)
        result = RationalNumber()
        result.nomer = new_nomer
        result.denomer = lcm

        return result

    # Выполнила Балаян Эдит 5381
    def div_qq_q(self, other):
        """
        Деление дробей (делитель отличен от нуля)
        Аргументы:
            other - делитель
        Возвращает:
            RationalNumber – результат деления
        """
        b = RationalNumber(
            other.nomer.sign,
            other.denomer.to_str(),
            other.nomer.to_str()
        )
        return self.mul_qq_q(b)


if __name__ == "__main__":
    rn1 = RationalNumber(int(input()), input(), input())
    rn2 = RationalNumber(int(input()), input(), input())
    print(rn1.sub_qq_q(rn2))
