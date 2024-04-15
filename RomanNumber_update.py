class RomanNumber:

    def __init__(self, number):
        if self.is_int(number):
            self.int_value = number
            self.rom_value = None
        elif self.is_roman(number):
            self.rom_value = number
            self.int_value = None
        else:
            self.rom_value = None
            self.int_value = None
            print('ошибка')

    def decimal_number(self):
        roman_equivalent = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0

        for i in range(len(self.rom_value) - 1):
            number += roman_equivalent[self.rom_value[i]]
            if roman_equivalent[self.rom_value[i]] < roman_equivalent[self.rom_value[i + 1]]:
                number -= roman_equivalent[self.rom_value[i]] * 2
        number += roman_equivalent[self.rom_value[-1]]

        return number

    def roman_number(self):


    @staticmethod
    def is_int(value):
        return type(value) == int and 0 < value < 4000

    @staticmethod
    def is_roman(value):
        roman_letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        subtraction_rule = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        value = str(value)

        for char in value:
            if char not in roman_letters:
                return False

        for i in ['X', 'C', 'M']:
            if value.count(i) > 4:
                return False

        for i in ['V', 'L', 'D']:
            if value.count(i) > 1:
                return False

        if value.count('I') > 3:
            return False

        for i in range(len(value) - 1):
            if roman_letters.index(value[i]) < roman_letters.index(value[i + 1]):
                if f'{value[i]}{value[i + 1]}' not in subtraction_rule:
                    return False
        return True

    def __str__(self):
        return str(self.rom_value)

    def __repr__(self):
        return self.__str__()
