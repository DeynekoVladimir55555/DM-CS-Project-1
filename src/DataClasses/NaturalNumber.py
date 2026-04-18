class NaturalNumber:
    """
    Реализация больших натуральных чисел
    Атрибуты:
        string (str): строковое представление числа,
        хранится в обратном порядке.
        Например число '123' преобразуется в [3, 2, 1].
    """
    def __init__(self, string=""):
        self.n = len(string) - 1
        self.digits = [0]
        if string:
            self.digits = [int(digit) for digit in string[::-1]]

    def __str__(self):
        return (
            f"NaturalNumber: {{\n\t"
            f"Старшая позиция: {self.n}\n\t"
            f"цифры: {[digit for digit in self.digits[::-1]]}\n"
            f"}}"
        )


if __name__ == "__main__":
    nn = NaturalNumber(input())
    print(nn)