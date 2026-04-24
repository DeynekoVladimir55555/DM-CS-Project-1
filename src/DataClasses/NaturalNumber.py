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

    #Выполнил Бабаян Александр 5381
    def nzer_n_b(self):
        """
            Проверка, является ли натуральное число нулём
            Аргументы:
                self - объект натурального числа
            Возвращает:
                True - если число не ноль
                False - если число равно нулю
        """
        if self.digits[0] != 0:
            return True
        return False

    # Выполнил Бабаян Александр 5381
    def add_1n_n(self):
        """
            Увеличение натурального числа на 1
            Аргументы:
                number - объект натурального числа
            Возвращает:
                number - изменённый объект (увеличенный на 1)
        """
        self.digits.reverse()
        if self.digits[-1] == 9:
            for i in range(self.n, -1, -1):
                if self.digits[i] == 9 and i != 0:
                    self.digits[i] = 0
                elif self.digits[i] == 9 and i == 0:
                    self.digits[i] = 0
                    self.digits.append(1)
                else:
                    self.digits[i] += 1
                    break
            return self

        self.digits[-1] += 1
        self.digits.reverse()

    # Выполнила Киселева Ева 5381
    def mul_nd_n(self):
        print(self.digits[0])


if __name__ == "__main__":
    nn = NaturalNumber(input())
    print(nn)
    print(nn.to_str())


