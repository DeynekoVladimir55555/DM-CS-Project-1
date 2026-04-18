class IntNumber:
    """
    Реализация больших целых чисел
    Атрибуты:
        sign (int): знак числа, 1 - минус, 0 - плюс.
        string (str): строковое представление числа,
        хранится в обратном порядке.
        Например число '123' преобразуется в [3, 2, 1].
    """
    def __init__(self, sign, string=""):
        self.n = len(string) - 1
        self.sign = sign
        self.digits = [0]
        if string:
            self.digits = [int(digit) for digit in string[::-1]]

    def __str__(self):
        return (
            f"IntNumber: {{\n\t"
            f"Знак: {"'-'" if self.sign else '+'}\n\t"
            f"старшая позиция: {self.n}, \n\t"
            f"цифры: {[digit for digit in self.digits[::-1]]}\n"
            f"}}"
        )


if __name__ == "__main__":
    intnumber = IntNumber(int(input()), input())
    print(intnumber)