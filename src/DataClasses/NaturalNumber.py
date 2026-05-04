from ..NaturalNumbers.NaturalFunctions import sub_nn_n


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
        if self.com_nn_d(number2) == 2:
            min_length = number2.n + 1
            max_length = self.n + 1
            number2.digits = number2.digits + [0] * (max_length - min_length)
        elif self.com_nn_d(number2) == 1:
            min_length = self.n + 1
            max_length = number2.n + 1
            self.digits = self.digits + [0] * (max_length - min_length)
        else:
            max_length = number2.n + 1

        result = []
        tmp = 0

        for i in range(max_length):
            result.append((self.digits[i] + number2.digits[i] + tmp) % 10)
            tmp = (self.digits[i] + number2.digits[i] + tmp) // 10
        if tmp == 1:
            result.append(1)
        final_result = NaturalNumber(''.join(map(str, result[::-1])))

        return final_result

    # Выполнила Килина Софья 5381
    def div_nn_dk(self, number):
        """
        Возвращает кортеж (count, k), где
        count – первая цифра частного,
        k – номер позиции этой цифры.
        count * number * 10^k <= self < (count + 1) * number * 10^k
        Аргументы:
            number (NaturalNumber): делитель
        """
        cmp = self.com_nn_d(number)
        if cmp == 0:
            return 1, 0
        if cmp == 1:
            b = NaturalNumber()
            b.digits = number.digits[:]
            b.n = number.n
            s = NaturalNumber()
            s.digits = self.digits[:]
            s.n = self.n
        else:
            b = NaturalNumber()
            b.digits = self.digits[:]
            b.n = self.n
            s = NaturalNumber()
            s.digits = number.digits[:]
            s.n = number.n
        k = 0
        bs = NaturalNumber()
        bs.digits = s.digits[:]
        bs.n = s.n
        n3 = NaturalNumber()
        n3.digits = s.digits[:]
        n3.n = s.n
        while b.com_nn_d(n3) == 2:
            k += 1
            n3.digits = bs.digits[:]
            n3.n = bs.n
            n3.mul_nk_n(k)
        k -= 1
        s = NaturalNumber()
        s.digits = bs.digits[:]
        s.n = bs.n
        n3 = NaturalNumber()
        n3.digits = s.digits[:]
        n3.n = s.n
        n3.mul_nk_n(k)
        s = n3

        count = 1
        tm = NaturalNumber()
        tm.digits = s.digits[:]
        tm.n = s.n
        n3 = NaturalNumber()
        n3.digits = s.digits[:]
        n3.n = s.n
        while b.com_nn_d(n3) == 2:
            count += 1
            n3.digits = tm.digits[:]
            n3.n = tm.n
            n3.mul_nd_n(count)
        if b.com_nn_d(n3) != 0:
            count -= 1
        if count == 10:
            count = 1
            k += 1

        return count, k

    # Выполнила Килина Софья 5381
    def sub_ndn_n(self, number, digit):
        """
            Вычитает из текущего числа (self) число (number * digit).
        """
        copy = NaturalNumber()
        copy.digits = number.digits[:]
        copy.n = number.n

        copy.mul_nd_n(digit)

        cmp = self.com_nn_d(copy)
        if cmp == 2 or cmp == 0:
            self.digits = sub_nn_n(self.digits, copy.digits)
            self.n = len(self.digits) - 1
            if len(self.digits) == 1 and self.digits[0] == 0:
                self.n = 0
            return self
        else:
            raise ValueError("number больше чем текущее число!")

    # Выполнил Килин Сергей 5381
    def mul_nn_n(self, number2):
        """
        Умножение двух натуральных чисел.
        Аргументы:
            number2 (NaturalNumber): второе натуральное число
        Возвращает:
            Новое NaturalNumber — результат произведения
        """
        result = NaturalNumber("0")
        for i, digit in enumerate(number2.digits):
            temp = NaturalNumber()
            temp.digits = self.digits[:]
            temp.n = self.n
            temp.mul_nd_n(digit)
            temp.mul_nk_n(i)
            result = result.add_nn_n(temp)

        return result


if __name__ == "__main__":
    nn = NaturalNumber(input())
    print(nn.n)
    nn.add_1n_n()
    print(nn)
    print(nn.to_str())
