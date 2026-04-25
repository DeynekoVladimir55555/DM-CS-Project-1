class IntNumber:
    """
    Реализация больших целых чисел
    Атрибуты:
        sign (int): знак числа, 1 - минус, 0 - плюс.
        string (str): строковое представление числа,
        хранится в обратном порядке.
        Например число '123' преобразуется в [3, 2, 1].
    """

    def __init__(self, sign=0, string=""):
        self.n = len(string) - 1 if len(string) else 0
        self.sign = sign
        self.digits = [0]
        if string:
            self.digits = [int(digit) for digit in string[::-1]]

    def __str__(self):
        return (
            f"IntNumber: {{\n\t"
            f"Знак: {'-' if self.sign else '+'}\n\t"
            f"Старшая позиция: {self.n}, \n\t"
            f"Цифры: {[digit for digit in self.digits[::-1]]}\n"
            f"}}"
        )

    def to_str(self):
        return ''.join([str(digit) for digit in self.digits[::-1]])

    # Килин Сергей 5381
    def trans_n_z(self, natural_number):
        """
        Преобразование натурального числа в целое
        Аргументы:
            natural_number (NaturalNumber): объект NaturalNumber
        """
        s = natural_number.to_str()
        return IntNumber(0, s)

    # Романенко Вика 5387
    def mul_zm_z(self): 
        """
            Умножение целого числа на -1
        """
        self.sign = 1 - self.sign 

if __name__ == "__main__":
    intnumber = IntNumber(int(input()), input())
    print(intnumber)
    print(intnumber.to_str())
