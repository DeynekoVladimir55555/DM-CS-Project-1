class NaturalNumber:
    """
    Реализация больших натуральных чисел
    Атрибуты:
        string (str): строковое представление числа,
        хранится в обратном порядке.
        Например, число '123' преобразуется в [3, 2, 1].
    """

    def __init__(self, string=""):
        self.digits = list(map(int, string[::-1])) if string else [0]
        self.n = len(self.digits)

    def __str__(self):
        return (
            f"NaturalNumber: {{\n\t"
            f"Старшая позиция: {self.n}\n\t"
            f"Цифры: {[digit for digit in self.digits[::-1]]}\n"
            f"}}"
        )

    def to_str(self):
        return ''.join([str(digit) for digit in self.digits[::-1]])

    # Выполнил Бабаян Александр 5381
    def nzer_n_b(self):
        """
            Проверка, является ли натуральное число нулём
            Аргументы:
                self - объект натурального числа
            Возвращает:
                True - если число не ноль
                False - если число равно нулю
        """
        return self.digits != [0]

    # Выполнил Бабаян Александр 5381
    def add_1n_n(self):
        """
            Увеличение натурального числа на 1
        """
        self.digits[0] += 1
        self.digits.append(0)

        for i in range(self.n):
            if self.digits[i] // 10:
                self.digits[i] = 0
                self.digits[i + 1] += 1

        if self.digits[-1]:
            self.n += 1
        else:
            self.digits = self.digits[:-1]

    # Выполнила Киселева Ева 5381
    def mul_nd_n(self, number):
        """
            Умножение натурального числа на цифру
            Аргументы:
                number - цифра на которую умножают натуральное число.
            Переменные(возможно не понятные):
                plus_n - число, которое идет на следующий разряд.
        """
        if number == 0:
            self.digits = [0]
            self.n = 0
        else:
            plus_n = 0
            for i in range(len(self.digits)):
                multi = self.digits[i] * number + plus_n
                self.digits[i] = multi % 10
                plus_n = multi // 10
                if plus_n > 0 and self.digits[i] == self.digits[-1]:
                    self.digits.append(plus_n)
            self.n = len(self.digits) - 1

    # Выполнила Балаян Эдит 5381
    def mul_nk_n(self, k):
        """
            Умножение натурального числа на 10^k,
            k - натуральное (не длинное)
            Аргументы:
                k - число, в которое возводится 10
            Возвращает:
                num - результат умножения на 10^k
        """
        self.digits = [0] * k + self.digits
        self.n += k


if __name__ == "__main__":
    nn = NaturalNumber(input())
    print(nn.n)
    nn.add_1n_n()
    print(nn)
    print(nn.to_str())
