class NavalBattle:
    playing_field = None

    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def show():
        for line in NavalBattle.playing_field:
            for cell in line:
                if cell == 0 or cell == 1:
                    print('~', end='')
                else:
                    print(cell, end='')
            print()

    def shot(self, x, y):
        x -= 1
        y -= 1
        if NavalBattle.playing_field[y][x] == 0:
            NavalBattle.playing_field[y][x] = 'o'
            print('мимо')
        if NavalBattle.playing_field[y][x] == 1:
            NavalBattle.playing_field[y][x] = self.symbol
            print('попал')

    def __str__(self):
        output = ''
        for line in NavalBattle.playing_field:
            for cell in line:
                output += str(cell)
            output += '\n'
        return output
