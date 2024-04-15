class RomanNumber:
    """
    The `RomanNumber` class represents a Roman numeral and provides methods to convert it to a decimal number, vice versa,
    and perform arithmetic operations with other RomanNumber objects.

    Attributes:
    int_value (int): The decimal value stored as an integer.
    rom_value (str): The Roman numeral value stored as a string.

    Methods:
    __init__(number): Initializes a new `RomanNumber` object with the provided number.
    decimal_number(): Converts the Roman numeral to a decimal number.
    roman_number(): Converts the decimal number to a Roman numeral.
    is_int(value): Checks if the provided value is a valid integer for a Roman numeral conversion.
    is_roman(value): Checks if the provided value is a valid Roman numeral.
    __add__(other): Adds two RomanNumber objects.
    __sub__(other): Subtracts one RomanNumber object from another.
    __mul__(other): Multiplies two RomanNumber objects.
    __truediv__(other): Divides one RomanNumber object by another, returns the result as a RomanNumber object if possible.
    __floordiv__(other): Divides one RomanNumber object by another, returns the integer division result as a RomanNumber object.
    __mod__(other): Computes the modulo of two RomanNumber objects.
    __pow__(other): Raises one RomanNumber object to the power of another.
    __str__(): Returns a string representation of the Roman numeral.
    __repr__(): Returns a string representation of the Roman numeral.
    """

    def __init__(self, number):
        """
        Initializes a new `RomanNumber` object with the provided number.

        Parameters:
        number (int or str): The number to be stored. It can be an integer or a Roman numeral string.
        """
        if self.is_int(number):
            self.int_value = number
            self.rom_value = self.roman_number()
        elif self.is_roman(number):
            self.rom_value = number
            self.int_value = self.decimal_number()
        else:
            self.rom_value = None
            self.int_value = None
            print('ошибка')

    def decimal_number(self):
        """
        Converts the Roman numeral to a decimal number.

        Returns:
        int: The decimal equivalent of the Roman numeral.
        """
        roman_equivalent = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0

        for i in range(len(self.rom_value) - 1):
            number += roman_equivalent[self.rom_value[i]]
            if roman_equivalent[self.rom_value[i]] < roman_equivalent[self.rom_value[i + 1]]:
                number -= roman_equivalent[self.rom_value[i]] * 2
        number += roman_equivalent[self.rom_value[-1]]

        return number

    def roman_number(self):
        """
        Converts the decimal number to a Roman numeral.

        Returns:
        str: The Roman numeral equivalent of the decimal number.
        """
        roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                         'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                         'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        roman = ''
        number = self.int_value
        for letter, value in roman_numbers.items():
            while number >= value:
                roman += letter
                number -= value
        return roman

    @staticmethod
    def is_int(value):
        """
        Checks if the provided value is a valid integer for a Roman numeral conversion.

        Parameters:
        value (int): The value to be checked.

        Returns:
        bool: True if the value is a valid integer, False otherwise.
        """
        return type(value) == int and 0 < value < 4000

    @staticmethod
    def is_roman(value):
        """
        Checks if the provided value is a valid Roman numeral.

        Parameters:
        value (str): The value to be checked.

        Returns:
        bool: True if the value is a valid Roman numeral, False otherwise.
        """
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

    def __add__(self, other):
        """
        Adds two RomanNumber objects.

        Parameters:
        other (RomanNumber): The other RomanNumber object to add.

        Returns:
        RomanNumber: A new RomanNumber object representing the sum.
        """
        result = self.decimal_number() + other.decimal_number()
        return RomanNumber(result)

    def __sub__(self, other):
        """
        Subtracts one RomanNumber object from another.

        Parameters:
        other (RomanNumber): The other RomanNumber object to subtract.

        Returns:
        RomanNumber: A new RomanNumber object representing the difference.
        """
        result = self.decimal_number() - other.decimal_number()
        return RomanNumber(result)

    def __mul__(self, other):
        """
        Multiplies two RomanNumber objects.

        Parameters:
        other (RomanNumber): The other RomanNumber object to multiply.

        Returns:
        RomanNumber: A new RomanNumber object representing the product.
        """
        result = self.decimal_number() * other.decimal_number()
        return RomanNumber(result)

    def __truediv__(self, other):
        """
        Divides one RomanNumber object by another, returns the result as a RomanNumber object if possible.

        Parameters:
        other (RomanNumber): The other RomanNumber object to divide by.

        Returns:
        RomanNumber: A new RomanNumber object representing the division result.
        """
        result = self.decimal_number() / other.decimal_number()
        if result == self.decimal_number() // other.decimal_number():
            return RomanNumber(int(result))
        return RomanNumber(result)

    def __floordiv__(self, other):
        """
        Divides one RomanNumber object by another, returns the integer division result as a RomanNumber object.

        Parameters:
        other (RomanNumber): The other RomanNumber object to divide by.

        Returns:
        RomanNumber: A new RomanNumber object representing the integer division result.
        """
        result = self.decimal_number() // other.decimal_number()
        return RomanNumber(result)

    def __mod__(self, other):
        """
        Computes the modulo of two RomanNumber objects.

        Parameters:
        other (RomanNumber): The other RomanNumber object to compute the modulo with.

        Returns:
        RomanNumber: A new RomanNumber object representing the modulo result.
        """
        result = self.decimal_number() % other.decimal_number()
        return RomanNumber(result)

    def __pow__(self, other):
        """
        Raises one RomanNumber object to the power of another.

        Parameters:
        other (RomanNumber): The other RomanNumber object to raise to the power of.

        Returns:
        RomanNumber: A new RomanNumber object representing the power result.
        """
        result = self.decimal_number() ** other.decimal_number()
        return RomanNumber(result)

    def __str__(self):
        """
        Returns a string representation of the Roman numeral.

        Returns:
        str: A string representation of the Roman numeral.
        """
        return str(self.rom_value)

    def __repr__(self):
        """
        Returns a string representation of the Roman numeral.

        Returns:
        str: A string representation of the Roman numeral.
        """
        return self.__str__()
