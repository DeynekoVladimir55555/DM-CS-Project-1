class NaturalNumber:
    """
    Реализация больших натуральных чисел
    Атрибуты:
        string (str): строковое представление числа,
        хранится в обратном порядке.
    Например, число '123' преобразуется в [3, 2, 1].
    """

    def __init__(self, string: list[str] | str = ""):
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
    def mul_nd_n(self, number: int):
        """
        Умножение натурального числа на цифру
        Аргументы:
            number (int): цифра на которую умножают натуральное число.
        Переменные:
            plus_n (int): число, которое идет на следующий разряд.
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
            k (int): степень числа 10
        """
        self.digits = [0] * k + self.digits
        self.n += k
        
    # Выполнил Бабаян Александр 5381
    def com_nn_d(self, number2):
        """
        Сравнение двух натуральных чисел
        Аргументы:
            number2 (NaturalNumber): второе натуральное число
        Возвращает:
            2 - если первое число больше второго
            1 - если второе число больше первого
            0 - если числа равны
        """
        if self.n > number2.n:
            return 2
        elif self.n < number2.n:
            return 1

        for i in range(self.n + 1):
            if self.digits[i] > number2.digits[i]:
                return 2
            elif self.digits[i] == number2.digits[i]:
                continue
            else:
                return 1

        return 0

    # Выполнил Бабаян Александр 5381
    def add_nn_n(self, number2):
        """
        Сложение двух натуральных чисел
        Аргументы:
            number2 (NaturalNumber): второе слагаемое
        Возвращает:
            final_number (NaturalNumber): результат сложения
        """
        tmp = 0
        result = []
        if self.com_nn_d(number2) == 2:
            min_length = number2.n + 1
            max_length = self.n + 1
        elif self.com_nn_d(number2) == 1:
            min_length = self.n + 1
            max_length = number2.n + 1
        else:
            min_length = self.n + 1
            max_length = number2.n + 1

        self.digits.reverse()
        number2.digits.reverse()

        for i in range(-1, (-1) * min_length - 1, -1):
            if (self.digits[i] + number2.digits[i] + tmp) >= 10:
                result.append(int(list(str(self.digits[i] + number2.digits[i] + tmp))[1]))
                tmp = 1
            else:
                result.append(int(list(str(self.digits[i] + number2.digits[i] + tmp))[0]))
                tmp = 0

        for j in range(max_length - min_length - 1, -1, -1):
            if self.n > number2.n:
                result.append(self.digits[j] + tmp)
                tmp = 0
            else:
                result.append(number2.digits[j] + tmp)
                tmp = 0
        if tmp == 1:
            result.append(1)
        result.reverse()
        final_number = NaturalNumber(result)

        return final_number


if __name__ == "__main__":
    nn = NaturalNumber(input())
    print(nn.n)
    nn.add_1n_n()
    print(nn)
    print(nn.to_str())
