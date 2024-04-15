class NavalBattle:
    """
    The `NavalBattle` class represents a simple naval battle game.

    Attributes:
    symbol (str): The symbol representing the player's ships on the playing field.
    playing_field (list): A 2D list representing the playing field of the naval battle.

    Methods:
    __init__(symbol): Initializes a new `NavalBattle` object with the provided symbol.
    show(): Displays the current state of the playing field.
    shot(x, y): Takes a shot at the specified coordinates on the playing field.
    __str__(): Returns a string representation of the playing field.
    """

    playing_field = None

    def __init__(self, symbol):
        """
        Initializes a new `NavalBattle` object with the provided symbol.

        Parameters:
        symbol (str): The symbol representing the player's ships on the playing field.
        """
        self.symbol = symbol

    @staticmethod
    def show():
        """
        Displays the current state of the playing field.
        """
        for line in NavalBattle.playing_field:
            for cell in line:
                if cell == 0 or cell == 1:
                    print('~', end='')
                else:
                    print(cell, end='')
            print()

    def shot(self, x, y):
        """
        Takes a shot at the specified coordinates on the playing field.

        Parameters:
        x (int): The x-coordinate of the shot.
        y (int): The y-coordinate of the shot.
        """
        x -= 1
        y -= 1
        if NavalBattle.playing_field[y][x] == 0:
            NavalBattle.playing_field[y][x] = 'o'
            print('мимо')
        if NavalBattle.playing_field[y][x] == 1:
            NavalBattle.playing_field[y][x] = self.symbol
            print('попал')

    def __str__(self):
        """
        Returns a string representation of the playing field.

        Returns:
        str: A string representation of the playing field.
        """
        output = ''
        for line in NavalBattle.playing_field:
            for cell in line:
                output += str(cell)
            output += '\n'
        return output
