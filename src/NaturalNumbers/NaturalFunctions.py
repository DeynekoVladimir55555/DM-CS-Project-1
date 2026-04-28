from src.DataClasses.NaturalNumber import NaturalNumber
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

