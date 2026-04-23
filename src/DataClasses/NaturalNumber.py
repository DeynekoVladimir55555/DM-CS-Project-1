class NaturalNumber:
    """
    Реализация больших натуральных чисел
    Атрибуты:
        string (str): строковое представление числа,
        хранится в обратном порядке.
        Например число '123' преобразуется в [3, 2, 1].
    """

    def __init__(self, string=""):
        self.n = len(string) - 1 if len(string) else 0
        self.digits = [0]
        if string:
            self.digits = [int(digit) for digit in string[::-1]]

    def __str__(self):
        return (
            f"NaturalNumber: {{\n\t"
            f"Старшая позиция: {self.n}\n\t"
            f"Цифры: {[digit for digit in self.digits[::-1]]}\n"
            f"}}"
        )

    def to_str(self):
        return ''.join([str(digit) for digit in self.digits[::-1]])
    def nzer_n_b(self):  # Является ли число нулём? - Бабаян
        if self.digits[0] != 0:
            return "да"
        return "нет"
    def add_1n_n(number):  # Прибавление к натуральному числу единицы - Бабаян
        number.digits.reverse()
        if number.digits[-1] == 9:
            for i in range(number.n, -1, -1):
                if number.digits[i] == 9 and i != 0:
                    number.digits[i] = 0
                elif number.digits[i] == 9 and i == 0:
                    number.digits[i] = 0
                    number.digits.append(1)
                else:
                    number.digits[i] += 1
                    break
            return number
        number.digits[-1] += 1
        return number

def COM_NN_D(number1, number2):  # Сравнение двух натуральных чисел - Бабаян
    if number1.n > number2.n:
        return 2
    elif number1.n < number2.n:
        return 1
    for i in range(number1.n + 1):
        if number1.digits[i] > number2.digits[i]:
            return 2
        elif number1.digits[i] == number2.digits[i]:
            continue
        else:
            return 1
    return 0

def ADD_NN_N(number1, number2): # Сумма двух натуральных чисел - Бабаян
    tmp = 0
    result = []
    if COM_NN_D(number1, number2) == 2:
        min_length = number2.n + 1
        max_length = number1.n + 1
    elif COM_NN_D(number1, number2) == 1:
        min_length = number1.n + 1
        max_length = number2.n + 1
    else:
        min_length = number1.n + 1
        max_length = number2.n + 1
    number1.digits.reverse()
    number2.digits.reverse()
    for i in range(-1, (-1) * min_length - 1, -1):
        if (number1.digits[i] + number2.digits[i] + tmp) >= 10:
            result.append(int(list(str(number1.digits[i] + number2.digits[i] + tmp))[1]))
            tmp = 1
        else:
            result.append(int(list(str(number1.digits[i] + number2.digits[i] + tmp))[0]))
            tmp = 0
    for j in range(max_length - min_length - 1, -1, -1):
        if number1.n > number2.n:
            result.append(number1.digits[j] + tmp)
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
    print(nn)
    print(nn.to_str())

