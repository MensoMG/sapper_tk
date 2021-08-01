import tkinter as tk

class MineSweeper:
    
    window = tk.Tk()
    COLUMNS = 10
    ROW = 10

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROW):
            temp = []
            for j in range(MineSweeper.COLUMNS):
                btn = tk.Button(MineSweeper.window, font='Calibri 15 bold')
                temp.append(btn)
        self.buttons.append(temp)


    def create_widgets(self):
        for i in range(MineSweeper.ROW):
            for j in range(MineSweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i,column=j)

    
    def start(self):
        MineSweeper.window.mainloop()




game = MineSweeper()
game.create_widgets()

for h in game.buttons:
    print(h)

game.start()
