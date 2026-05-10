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
        self.n = len(self.digits) - 1

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
        res = NaturalNumber(self.to_str())
        plus_n = 1

        for i in range(len(res.digits)):
            sm = res.digits[i] + plus_n
            res.digits[i] = sm % 10
            plus_n = sm // 10
            if plus_n == 0:
                break

        if plus_n:
            res.digits.append(plus_n)
            res.n += 1

        return res

    # Выполнила Киселева Ева 5381
    def mul_nd_n(self, number: int):
        """
        Умножение натурального числа на цифру
        Аргументы:
            number (int): цифра на которую умножают натуральное число.
        Переменные:
            plus_n (int): число, которое идет на следующий разряд.
        """
        res = NaturalNumber()

        if number == 0:
            return res

        res.digits = self.digits
        plus_n = 0
        for i in range(self.n + 1):
            multi = self.digits[i] * number + plus_n
            res.digits[i] = multi % 10
            plus_n = multi // 10
        if plus_n > 0:
            res.digits.append(plus_n)
        res.n = len(res.digits) - 1

        return res

    # Выполнила Киселева Ева 5381
    def mod_nn_n(self, num2):
        """
        Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)
        Аргументы:
            num2: второе натуральное число(делитель != 0)
        Возвращает:
            result - объект NaturalNumber, остаток
        """
        chasnoe = self.div_nn_n(num2)
        op = num2.mul_nn_n(chasnoe)
        result = self.sub_nn_n(op)
        return result

    # Выполнила Романенко Вика 5387
    def div_nn_n(self, number2):
        """
        Неполное частное от деления первого натурального числа на второе с остатком
        Аргументы:
            number2 (NaturalNumber): делитель (отличен от нуля)
        Возвращает:
            NaturalNumber: неполное частное
        """
        if not number2.nzer_n_b():
            raise ZeroDivisionError("Деление на ноль!")

        if self.com_nn_d(number2) == 1:
            return NaturalNumber()

        copy_delimoe = NaturalNumber(self.to_str())
        delitel = NaturalNumber(number2.to_str())

        razrad = []

        while copy_delimoe.com_nn_d(delitel) != 1:
            digit, k = copy_delimoe.div_nn_dk(delitel)

            while len(razrad) <= k:
                razrad.append(0)
            razrad[k] = digit

            temp = NaturalNumber(delitel.to_str())
            temp = temp.mul_nd_n(digit).mul_nk_n(k)
            copy_delimoe = copy_delimoe.sub_ndn_n(temp, 1)

        razrad.reverse()
        result_str = ''.join(map(str, razrad))

        return NaturalNumber(result_str)

    # Выполнила Романенко Вика 5387
    def lcm_nn_n(self, number2):
        """
        НОК (наименьшее общее кратное) натуральных чисел
        Аргументы:
            number2 (NaturalNumber): второе натуральное число
        Возвращает:
            NaturalNumber: НОК двух чисел
        """
        gcd = self.gcf_nn_n(number2)
        product = self.mul_nn_n(number2)
        result = product.div_nn_n(gcd)
        return result

    # Выполнила Романенко Вика 5387
    def sub_nn_n(self, number2):
        """
        Вычитание двух натуральных чисел (из большего вычитаем меньшее)
        Аргументы:
            self - уменьшаемое
            number2 - вычитаемое
        Возвращает:
            final_number - объект NaturalNumber, результат вычитания
        """
        tmp = 0
        result = []

        if self.com_nn_d(number2) == 2:
            min_length = number2.n + 1
            max_length = self.n + 1
            big = self
            small = number2
        elif self.com_nn_d(number2) == 1:
            min_length = self.n + 1
            max_length = number2.n + 1
            big = number2
            small = self
        else:
            return NaturalNumber("0")

        big.digits.reverse()
        small.digits.reverse()

        for i in range(-1, (-1) * min_length - 1, -1):
            diff = big.digits[i] - tmp - small.digits[i]

            if diff < 0:
                diff += 10
                tmp = 1
            else:
                tmp = 0

            result.append(diff)

        for j in range(max_length - min_length - 1, -1, -1):
            diff = big.digits[j] - tmp

            if diff < 0:
                diff += 10
                tmp = 1
            else:
                tmp = 0

            result.append(diff)

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result.reverse()

        big.digits.reverse()
        small.digits.reverse()

        final_number = NaturalNumber(list(map(str, result)))

        return final_number

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

        for i in range(self.n, -1, -1):
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

    # Выполнил Бабаян Александр 5381
    def gcf_nn_n(self, number2):
        """
        НОД натуральных чисел
        Аргументы:
            number2 - второе натуральное число
        Возвращает:
            result - объект NaturalNumber, НОД
        """
        result = NaturalNumber(self.to_str())
        b = NaturalNumber(number2.to_str())

        while b.nzer_n_b():
            r = result.mod_nn_n(b)
            result = b
            b = r

        return result

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
            n3 = n3.mul_nk_n(k)
        k -= 1
        s = NaturalNumber()
        s.digits = bs.digits[:]
        s.n = bs.n
        n3 = NaturalNumber()
        n3.digits = s.digits[:]
        n3.n = s.n
        n3 = n3.mul_nk_n(k)
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
    nn1 = NaturalNumber(input())
    nn2 = NaturalNumber(input())

    print(nn1.gcf_nn_n(nn2))
