from src.DataClasses.NaturalNumber import NaturalNumber


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
        s = ["-", "--", "+"]
        return (
            f"IntNumber: {{\n\t"
            f"Знак: {s[self.sign + 1]}\n\t"
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
        return IntNumber(1, natural_num.to_str())

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
        return IntNumber(-self.sign, self.to_str())

    # Выполнила Киселева Ева 5381
    def sgn_z_d(self):
        """
        Определение положительности числа
        """
        return self.sign

    # Выполнила Киселева Ева 5381
    def mul_zz_z(self, number2):
        """
            Умножение целых чисел
            Аргументы:
                number2 (IntNumber): второе целое число
            Возвращает:
                Новое IntNumber — результат произведение (result)
        """
        if self.sign == 0 or number2.sign == 0:
            return IntNumber()

        nat_a = self.trans_z_n()
        nat_b = number2.trans_z_n()
        ns = 1 if self.sign == number2.sign else -1
        return IntNumber(ns, nat_a.mul_nn_n(nat_b).to_str())

    # Выполнила Балаян Эдит 5381
    def abs_z_z(self):
        """
        Абсолютная величина числа
        """
        ns = 1 if self.sign == -1 else self.sign
        return IntNumber(ns, self.to_str())

    # Выполнила Балаян Эдит 5381
    def sub_zz_z(self, number2):
        """
          Вычитание целых чисел
        Аргументы:
            number2 - вычитаемое
        Возвращает:
            IntNumber — результат разности
        """
        b = IntNumber(number2.sign, number2.to_str())
        return self.add_zz_z(b.mul_zm_z())

    # Выполнила Балаян Эдит 5381
    def div_zz_z(self, number2):
        """
        Частное от деления целого на целое (делитель отличен от нуля)
        Аргументы:
            number2 - делитель
        Возвращает:
            IntNumber — частное
        """
        if number2.sign == 0:
            raise ZeroDivisionError("Деление на ноль!")

        if self.sign == 0:
            return IntNumber()

        nat_a = self.trans_z_n()
        nat_n = number2.trans_z_n()
        res = nat_a.div_nn_n(nat_n)

        if res.to_str() == "0":
            ns = 0
        elif self.sign == number2.sign:
            ns = 1
        else:
            ns = -1

        return IntNumber(ns, res.to_str())

    # Выполнила Бондаренко Полина 5381
    def mod_zz_z(self, number2):
        """
        Остаток от деления целого на целое (делитель отличен от нуля).
        Аргументы:
            number2 (IntNumber) – делитель (не равен нулю)
        Возвращает:
            IntNumber – остаток от деления self на other
        Использует:
            DIV_ZZ_Z, MUL_ZZ_Z, SUB_ZZ_Z
        """
        chastnoe = self.div_zz_z(number2)
        proizvedenie = number2.mul_zz_z(chastnoe)
        ostatok = self.sub_zz_z(proizvedenie)
        return ostatok

    # Выполнил Килин Сергей 5381
    def add_zz_z(self, number2):
        """
        Сложение двух целых чисел.
        Аргументы:
            number2 (IntNumber): второе целое число
        Возвращает:
            Новое IntNumber — результат суммы
        """
        nat_a = self.trans_z_n()
        nat_b = number2.trans_z_n()
        sign_a = self.sgn_z_d()
        sign_b = number2.sgn_z_d()

        if sign_a == sign_b:
            nat_result = nat_a.add_nn_n(nat_b)
            return IntNumber(sign_a, nat_result.to_str())

        cmp = nat_a.com_nn_d(nat_b)
        if cmp == 0:
            return IntNumber(0, "0")
        elif cmp == 2:
            digits = nat_a.sub_nn_n(nat_b).digits
            return IntNumber(sign_a, ''.join(map(str, digits[::-1])))
        else:
            digits = nat_b.sub_nn_n(nat_a).digits
            return IntNumber(sign_b, ''.join(map(str, digits[::-1])))


if __name__ == "__main__":
    int1 = IntNumber(int(input()), input())
    # int2 = IntNumber(int(input()), input())
    print(int1)
