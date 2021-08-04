import tkinter as tk
from random import shuffle


class MyButton(tk.Button):

    def __init__(self, master, x, y, number, *args, **kwargs):
        super(MyButton, self).__init__(master, width=1, font='Calibri 15 bold', *args, **kwargs,)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self):
        return f'MyButton ({self.x} {self.y}) - {self.number}'


class MineSweeper:

    window = tk.Tk()
    ROW = 10
    COLUMNS = 10
    MINES = 15

    def __init__(self):
        self.buttons = []
        count = 1 
        for rows in range(MineSweeper.ROW):
            temp = []
            for clmns in range(MineSweeper.COLUMNS):
                btn = MyButton(MineSweeper.window, x=rows, y=clmns, number=count)
                temp.append(btn)
                count += 1
            self.buttons.append(temp)

    def create_widgets(self):
        for rows in range(MineSweeper.ROW):
            for clmns in range(MineSweeper.COLUMNS):
                btn = self.buttons[rows][clmns]
                btn.grid(row=rows, column=clmns)
    
    def start(self):
        self.create_widgets()
        self.print_buttons()
        print(self.get_mines_places())
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for i in game.buttons:
            print(i)

    def get_mines_places(self):
        pos_mines = list(range(1, MineSweeper.ROW*MineSweeper.COLUMNS+1))
        shuffle(pos_mines)
        return(pos_mines[:MineSweeper.MINES])

game = MineSweeper()
game.start()

