import tkinter as tk
from random import shuffle


class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0,  *args, **kwargs):
        super(MyButton, self).__init__(master, width=1, font='Calibri 15 bold', *args, **kwargs,)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False

    def __repr__(self):
        return f'MyButton ({self.x} {self.y}) - {self.number} = {self.is_mine}'


class MineSweeper:

    window = tk.Tk()
    ROW = 5
    COLUMNS = 4
    MINES = 5

    def __init__(self):
        self.buttons = []
        for rows in range(MineSweeper.ROW+2):
            temp = []
            for clmns in range(MineSweeper.COLUMNS+2):
                btn = MyButton(MineSweeper.window, x=rows, y=clmns)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)
  
    def click(self, clicked_button: MyButton): 
        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
        else:
            clicked_button.config(text=clicked_button.number)
        clicked_button.config(state='disabled')

    def create_widgets(self):
        for rows in range(MineSweeper.ROW+2):
            for clmns in range(MineSweeper.COLUMNS+2):
                btn = self.buttons[rows][clmns]
                btn.grid(row=rows, column=clmns)
    
    def open_all_buttons(self):
        for rows in range(MineSweeper.ROW+2):
            for clmns in range(MineSweeper.COLUMNS+2):
                btn = self.buttons[rows][clmns]
                if btn.is_mine:
                    btn.config(text='*', background='red', disabledforeground='black')
                else:
                    btn.config(text=btn.number, disabledforeground='black')

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.print_buttons()
        self.open_all_buttons()
        print(self.get_mines_places())
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for i in self.buttons:
            print(i)

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1
        for rows in range(1, MineSweeper.ROW+1):
            for clmns in range(1, MineSweeper.COLUMNS+1):
                btn = self.buttons[rows][clmns]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1
    @staticmethod
    def get_mines_places():
        pos_mines = list(range(1, MineSweeper.ROW*MineSweeper.COLUMNS+1))
        shuffle(pos_mines)
        return(pos_mines[:MineSweeper.MINES])

game = MineSweeper()
game.start()

