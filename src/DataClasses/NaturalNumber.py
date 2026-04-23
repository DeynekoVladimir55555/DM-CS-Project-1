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
            return True
        return False

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
        number.digits.reverse()

        return number


if __name__ == "__main__":
    nn = NaturalNumber(input())
    print(nn)
    print(nn.to_str())

