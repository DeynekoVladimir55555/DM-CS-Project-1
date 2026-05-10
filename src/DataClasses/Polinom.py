from src.DataClasses.RationalNumber import RationalNumber
from src.DataClasses.NaturalNumber import NaturalNumber


class Polinom:
    """
    Реализация многочлена
    Аргументы:
        sign (int): 1 - плюс, 0 - для числа 0, -1 - минус.
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
            sign (int): 1 - плюс, 0 - для числа 0, -1 - минус.
            deg (int): степень члена
            nomer (str): числитель коэффициента
            denomer (str): знаменатель коэффициента
        """
        if deg > self.deg:
            self.change_deg(deg)

        self.coefs[deg] = RationalNumber(sign, nomer, denomer)

    def change_deg(self, new_deg):
        if self.deg > new_deg:
            for i in range(self.deg, new_deg, -1):
                self.coefs.pop(i, None)
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

    # Выполнил Килин Сергей 5381
    def deg_p_n(self):
        """
        Возвращает степень многочлена.
        """
        return self.deg

    # Выполнила Зуева Екатерина 5381
    def mul_pxk_p(self, k: int):
        """
        Умножает многочлен на x^k. Если k != 0, создаёт и
        заполняет новый словарь для коэффициентов,
        чтобы доступ к элементам был корректен.
        Аргументы:
            k (int): степень x
                k >= 0
        """
        result = Polinom()
        result.deg = self.deg

        if k == 0:
            result.coefs = dict(self.coefs)
            return result

        result.coefs = {}
        for deg, coef in self.coefs.items():
            result.coefs[deg + k] = coef
        result.deg = self.deg + k

        return result

    # Выполнила Килина Софья 5381
    def der_p_p(self):
        """
        Возвращает новый многочлен - производную от текущего
        """
        res = Polinom(0, 0, "0", "1")

        if self.deg == 0:
            return res

        res.change_deg(self.deg - 1)

        for i in range(1, self.deg + 1):
            coeff = self.coefs[i]
            if coeff.nomer.sign == 0:
                continue
            new_coeff = coeff * i

            res.change_coef(
                sign=new_coeff.nomer.sign,
                deg=i - 1,
                nomer=new_coeff.nomer.to_str(),
                denomer=new_coeff.denomer.to_str()
            )
        
        while res.deg > 0 and res.coefs[res.deg].nomer.sign == 0:
            res.change_deg(res.deg - 1)

        return res

    # Выполнила Килина Софья 5381
    def fac_p_q(self):
        """
            Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей.
        """
        nod = None
        nok = None
        count = 0

        for i in range(self.deg + 1):
            coeff = self.coefs[i]
            if coeff.nomer.sign == 0:
                continue

            num = NaturalNumber(coeff.nomer.to_str())
            den = coeff.denomer

            if nod is None:
                nod = num
                nok = den
            else:
                nod = nod.gcf_nn_n(num)
                nok = nok.lcm_nn_n(den)

            if coeff.nomer.sign == -1:
                count += 1

        if nod is None:
            return RationalNumber(0, "0", "1")

        sign = -1 if (count % 2) else 1
        if nod.to_str() == "0":
            sign = 0

        return RationalNumber(sign, nod.to_str(), nok.to_str())

    # Выполнила Килина Софья 5381
    def mul_pp_p(self, polinom2):
        """
        Умножение многочленов.
        """
        deg1 = self.deg + polinom2.deg
        res = Polinom(0, 0, "0", "1")
        res.change_deg(deg1)

        for i in range(self.deg + 1):
            coef1 = self.coefs[i]
            if coef1.nomer.sign == 0:
                continue
            for j in range(polinom2.deg + 1):
                coef2 = polinom2.coefs[j]
                if coef2.nomer.sign == 0:
                    continue
                prod = coef1.mul_qq_q(coef2)
                cur = res.coefs[i + j]
                ncoef = cur.add_qq_q(prod)
                res.change_coef(
                    sign=ncoef.nomer.sign,
                    deg=i + j,
                    nomer=ncoef.nomer.to_str(),
                    denomer=ncoef.denomer.to_str()
                )
        while res.deg > 0 and res.coefs[res.deg].nomer.sign == 0:
            res.change_deg(res.deg - 1)
        return res

    # Выполнила Киселева Ева 5381
    def led_p_q(self):
        """
        Возвращает старший коэффициент многочлена
        """
        return self.coefs[self.deg]

    # Выполнила Киселева Ева 5381
    def div_pp_p(self, delitel):
        """
            Частное от деления многочлена на многочлен при делении с остатком
            Аргументы:
                delitel (Polinom) - делитель
            Возвращает:
                result (Polinom) - частное от деления
        """
        if delitel.deg == 0 and delitel.coefs[0].nomer.sign == 0:
            raise ZeroDivisionError

        if self.deg < delitel.deg:
            return Polinom(0, 0, "0", "1")

        a = self
        b = delitel
        result = Polinom(0, 0, "0", "1")
        while a.deg >= b.deg and not a.coefs[a.deg].nomer.sign == 0:
            c = a.led_p_q().div_qq_q(b.led_p_q())
            term = Polinom(c.nomer.sign, a.deg - b.deg, c.nomer.to_str(), c.denomer.to_str())
            if result.deg == 0 and result.coefs[0].nomer.sign == 0:
                result = term
            else:
                result = result.add_pp_p(term)
            a = a.sub_pp_p(b.mul_pp_p(term))
            while a.deg > 0 and a.coefs[a.deg].nomer.sign == 0:
                a.change_deg(a.deg - 1)
        return result

    # Выполнила Бондаренко Полина 5381
    def sub_pp_p(self, polinom2):
        """
        Вычитание многочленов: self - polinom2
        Возвращает: новый многочлен (Polinom)
        Используется: sub_qq_q для коэффициентов
        """
        max_deg = max(self.deg, polinom2.deg)
        result = Polinom(0, 0, "0", "1")

        for i in range(max_deg + 1):
            if i <= self.deg:
                coef1 = self.coefs[i]
            else:
                coef1 = RationalNumber(0, "0", "1")
            if i <= polinom2.deg:
                coef2 = polinom2.coefs[i]
            else:
                coef2 = RationalNumber(0, "0", "1")

            diff = coef1.sub_qq_q(coef2)
            if diff.nomer.sign != 0:
                result.change_coef(
                    sign=diff.nomer.sign,
                    deg=i,
                    nomer=diff.nomer.to_str(),
                    denomer=diff.denomer.to_str()
                )

        while result.deg > 0:
            if result.deg not in result.coefs:
                result.deg -= 1
            else:
                coeff = result.coefs[result.deg]
                if coeff.nomer.sign == 0:
                    result.coefs.pop(result.deg)
                    result.deg -= 1
                else:
                    break
        return result

    # Выполнила Романенко Вика 5387
    def mod_pp_p(self, other):
        """
        Остаток от деления многочлена на многочлен при делении с остатком
        Аргументы:
            other (Polinom): делитель (многочлен)
        Возвращает:
            Polinom: остаток от деления
        """
        dividend = Polinom(0, 0, "0", "1")
        for deg, coef in self.coefs.items():
            if coef.nomer.sign != 0:
                dividend.change_coef(
                    sign=coef.nomer.sign,
                    deg=deg,
                    nomer=coef.nomer.to_str(),
                    denomer=coef.denomer.to_str()
                )

        divisor = other

        if dividend.deg_p_n() < divisor.deg_p_n():
            return dividend

        quotient = dividend.div_pp_p(divisor)
        product = divisor.mul_pp_p(quotient)
        remainder = dividend.sub_pp_p(product)
        return remainder

    # выполнила Балаян Эдит 5381
    def add_pp_p(self, other):
        """
        Сложение многочленов
        Аргументы:
            other (Polinom): второй многочлен
        Возвращает:
            res (Polinom) — результат сложения
        """
        max_deg = max(self.deg, other.deg)
        res = Polinom(0, max_deg, "0", "1")

        for i in range(max_deg + 1):
            coef1 = self.coefs.get(i, RationalNumber(0, "0", "1"))
            coef2 = other.coefs.get(i, RationalNumber(0, "0", "1"))
            res.coefs[i] = coef1.add_qq_q(coef2)

        return res

    # Выполнила Зуева Екатерина 5381
    def mul_pq_p(self, k: RationalNumber):
        """
        Умножение многочлена на рациональное число.
        Возвращает новый многочлен.
        Аргумент:
            k (RationalNumber): рациональное число,
            на которое умножается каждый коэффициент многочлена.
        """
        result = Polinom()
        result.deg = self.deg
        result.coefs = {}

        if k.nomer.to_str() == "0":
            result.coefs = {0: RationalNumber(0, "0", "1")}
            result.deg = 0
            return result

        for deg in range(self.deg + 1):
            result.coefs[deg] = self.coefs[deg].mul_qq_q(k)

        return result

    # Выполнила Зуева Екатерина 5381
    def nmr_p_p(self):
        """
        Преобразование многочлена с кратными корнями в многочлен с простыми корнями.
        Q(x) = P(x) / НОД(P(x), P'(x))
        Возвращает новый многочлен.
        """
        if self.deg == 0:
            result = Polinom()
            result.deg = self.deg
            result.coefs = dict(self.coefs)
            return result

        der_p = self.der_p_p()
        nod = self.gcf_pp_p(der_p)

        if nod.deg != 0 or nod.coefs[0].nomer.to_str() != "1":
            return self.div_pp_p(nod)

        result = Polinom()
        result.deg = self.deg
        result.coefs = dict(self.coefs)
        return result

    # Выполнил Бабаян Александр 5381
    def gcf_pp_p(self, number2):
        """
        Находит наибольший общий делитель (НОД) двух многочленов
        с использованием алгоритма Евклида.
        Аргументы:
            self - первый многочлен
            number2 - второй многочлен
        Возвращает:
            result - НОД многочленов.
        """
        a = self
        b = number2

        while b.deg > 0 or b.coefs[0].nomer.to_str() != "0":
            r = a.mod_pp_p(b)
            a = b
            b = r

        return a


if __name__ == "__main__":
    p = Polinom(1, 3, "23457", "23712")
    p.change_coef(1, 3, "123", "123")
    p.change_coef(1, 5, "234", "54")
    p.change_coef(1, 2, "543", "23")
    print(p)
    