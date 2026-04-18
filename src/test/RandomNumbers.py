from src.DataClasses.NaturalNumber import NaturalNumber
from src.DataClasses.IntNumber import IntNumber
from src.DataClasses.RationalNumber import RationalNumber
from src.DataClasses.Polinom import Polinom
from random import randint

#Выполнил Дейнеко Владимир 5381
def generator(key=0):
    """
    Генератор случайных чисел
    Аргументы:
        key (int): выполняет генерацию
            0 - натуральное число
            1 - целое число
            2 - рациональное число
            иначе - многочлен
    """
    if key == 0:
        return rd_nat_num()
    if key == 1:
        return rd_int_num()
    if key == 2:
        return rd_rat_num()
    return rd_pol()


def rd_str():
    ln = randint(9, 15)
    rd_num = ''
    for i in range(ln):
        rd_num += str(randint(0, 9))
    return rd_num


def rd_sn():
    return randint(0, 1)


def rd_nat_num():
    return NaturalNumber(rd_str())


def rd_int_num():
    return IntNumber(rd_sn(), rd_str())


def rd_rat_num():
    return RationalNumber(rd_sn(), rd_str(), rd_str())


def rd_pol():
    pass