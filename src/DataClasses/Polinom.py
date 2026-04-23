from RationalNumber import RationalNumber


class Polinom:
    """
    Реализация многочлена
    Аргументы:
        sign (int): 1 - минус, 0 - плюс.
        deg (int): степень члена
        nomer (str): числитель коэффициента
        denomer (str): знаменатель коэффициента
    """

    def __init__(self, sign=0, deg=0, nomer="", denomer=""):
        self.deg = deg
        self.coefs = {
            deg: RationalNumber(sign, nomer, denomer)
        }
        for i in range(deg - 1, -1, -1):
            self.coefs[i] = RationalNumber()

    def change_coef(self, sign=0, deg=0, nomer="", denomer=""):
        """
        Добавление нового члена в многочлен или изменение старого
        Аргументы как при инициализации:
            sign (int): 1 - минус, 0 - плюс.
            deg (int): степень члена
            nomer (str): числитель коэффициента
            denomer (str): знаменатель коэффициента
        """
        if deg > self.deg:
            self.change_deg(deg)

        self.coefs[deg] = RationalNumber(sign, nomer, denomer)

    def change_deg(self, new_deg):
        if self.deg > new_deg:
            for i in range(self.deg + 1, new_deg, -1):
                self.coefs.pop(i)
        else:
            for i in range(self.deg + 1, new_deg + 1):
                self.coefs[i] = RationalNumber()
        self.deg = new_deg

    def __str__(self):
        string = ""
        for i in range(self.deg + 1):
            coef = self.coefs[i]
            formatted_coef = str(coef).replace('\n', '\n\t\t')
            string += f"\tСтепень x^{i}:\n\t\t{formatted_coef}\n"

        return (
            f"Polinom: {{\n\t"
            f"Степень многочлена {self.deg}\n"
            f"{string}"
            f"}}"
        )

    def deg_p_n(self):  # Килин
        """
        Возвращает степень многочлена.
        """
        return self.deg


if __name__ == "__main__":
    p = Polinom(1, 3, "23457", "23712")
    p.change_coef(1, 3, "123", "123")
    p.change_coef(1, 5, "234", "54")
    p.change_coef(1, 2, "543", "23")
    print(p)
