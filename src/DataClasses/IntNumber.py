from NaturalNumber import NaturalNumber


class IntNumber:
    """
    Реализация больших целых чисел
    Атрибуты:
        sign (int): знак числа, 1 - плюс, 0 - для числа 0, -1 - минус
        string (str): строковое представление числа,
        хранится в обратном порядке.
    Например, число '123' преобразуется в [3, 2, 1].
    """

    def __init__(self, sign: int = 0, string: list[str] | str = ""):
        self.n = len(string) - 1 if len(string) else 0
        self.sign = sign
        self.digits = [0]
        if string:
            self.digits = [int(digit) for digit in string[::-1]]

    def __str__(self):
        return (
            f"IntNumber: {{\n\t"
            f"Знак: {'-' if self.sign else '+'}\n\t"
            f"Старшая позиция: {self.n}, \n\t"
            f"Цифры: {[digit for digit in self.digits[::-1]]}\n"
            f"}}"
        )

    def to_str(self):
        return ''.join([str(digit) for digit in self.digits[::-1]])

    # Выполнил Килин Сергей 5381
    @staticmethod
    def trans_n_z(natural_num: NaturalNumber):
        """
        Преобразование натурального числа в целое
        Аргументы:
            natural_num (NaturalNumber): объект NaturalNumber
        """
        s = natural_num.to_str()
        return IntNumber(1, s)

    # Выполнила Зуева Екатерина 5381
    def trans_z_n(self) -> NaturalNumber:
        """
        Преобразование целого неотрицательного числа в натуральное
        """
        return NaturalNumber(self.to_str())

    # Выполнила Романенко Вика 5387
    def mul_zm_z(self):
        """
        Умножение целого числа на -1
        """
        self.sign *= -1

    # Выполнила Киселева Ева 5381
    def sgn_z_d(self):
        """
        Определение положительности числа
        """
        return self.sign

    # Выполнила Балаян Эдит 5381
    def abs_z_z(self):
        """
        Абсолютная величина числа
        """
        if self.sgn_z_d() == -1:
            self.sign = 1

    # Выполнил Килин Сергей 5381
    def add_zz_z(self, number2):
        """
        Сложение двух целых чисел.
        Аргументы:
            number2 (IntNumber): второе целое число
        Возвращает:
            Новое IntNumber — результат суммы
        """
        a = IntNumber(self.sign, self.to_str())
        a.abs_z_z()
        b = IntNumber(number2.sign, number2.to_str())
        b.abs_z_z()
        nat_a = a.trans_z_n()
        nat_b = b.trans_z_n()

        sign_a = self.sgn_z_d()
        sign_b = number2.sgn_z_d()
        if sign_a == sign_b:
            nat_result = nat_a.add_nn_n(nat_b)
            return IntNumber(sign_a, nat_result.to_str())
        cmp = nat_a.com_nn_d(nat_b)
        if cmp == 0:
            return IntNumber(0, "0")
        elif cmp == 2:
            digits = sub_nn_n(nat_a.digits, nat_b.digits)
            return IntNumber(sign_a, ''.join(map(str, digits[::-1])))
        else:
            digits = sub_nn_n(nat_b.digits, nat_a.digits)
            return IntNumber(sign_b, ''.join(map(str, digits[::-1])))


if __name__ == "__main__":
    intnumber = IntNumber(int(input()), input())
    print(intnumber)
    print(intnumber.to_str())
