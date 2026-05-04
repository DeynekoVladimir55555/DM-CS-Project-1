from ..DataClasses.NaturalNumber import NaturalNumber


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

    final_number = NaturalNumber(result)

    return final_number

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
        return NaturalNumber("0")

    copy_delimoe = NaturalNumber(self.to_str())
    delitel = number2

    razrad = []

    while copy_delimoe.com_nn_d(delitel) != 1:
        digit, k = copy_delimoe.div_nn_dk(delitel)

        while len(razrad) <= k:
            razrad.append(0)
        razrad[k] = digit

        temp = NaturalNumber(delitel.to_str())
        temp.mul_nd_n(digit)
        temp.mul_nk_n(k)
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
