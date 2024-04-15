import random
from tkinter import messagebox


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
        if NavalBattle.playing_field is None:
            messagebox.showerror('Сообщение', 'Игровое поле не заполнено')
            print('Игровое поле не заполнено')
            exit()
        if NavalBattle.playing_field[y][x] == 'o' or NavalBattle.playing_field[y][x] == self.symbol:
            messagebox.showerror('Сообщение', 'Ошибка')
            print('ошибка')
        if NavalBattle.playing_field[y][x] == 0:
            NavalBattle.playing_field[y][x] = 'o'
            print('мимо')
        if NavalBattle.playing_field[y][x] == 1:
            NavalBattle.playing_field[y][x] = self.symbol
            print('попал')

    @classmethod
    def new_game(cls):
        playing_field = [[0] * 10 for _ in range(10)]
        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        for ship in ships:
            while True:
                orientation = random.randint(0, 1)

                if orientation == 0:
                    x_cor, y_cor = random.randint(0, 9), random.randint(0, 9 - ship + 1)
                else:
                    x_cor, y_cor = random.randint(0, 9 - ship + 1), random.randint(0, 9)

                availability = True

                for i in range(ship):

                    if orientation == 0:
                        new_x, new_y = x_cor, y_cor + i
                    else:
                        new_x, new_y = x_cor + i, y_cor

                    if not (0 <= new_x <= 9 and 0 <= new_y <= 9) or playing_field[new_x][new_y] == 1:
                        availability = False
                        break

                    for j in range(new_x - 1, new_x + 2):
                        for k in range(new_y - 1, new_y + 2):
                            if 0 <= j <= 9 and 0 <= k <= 9 and playing_field[j][k] == 1:
                                availability = False
                                break

                if availability:
                    if orientation == 0:
                        for i in range(ship):
                            playing_field[x_cor][y_cor + i] = 1
                    else:
                        for i in range(ship):
                            playing_field[x_cor + i][y_cor] = 1
                    break

        NavalBattle.playing_field = playing_field

    def __str__(self):
        output = ''
        for line in NavalBattle.playing_field:
            for cell in line:
                output += str(cell)
            output += '\n'
        return output
