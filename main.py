import tkinter as tk

window = tk.Tk()


ROW = 5
COLUMNS = 7

buttons = []
for i in range(ROW):
    temp = []
    for j in range(COLUMNS):
        btn = tk.Button(window)
        temp.append(btn)
    buttons.append(temp)

for i in range(ROW):
    temp = []
    for j in range(COLUMNS):
        btn = buttons[i][j]
        btn.grid(row=i,column=j)

for h in buttons:
    print(h)

window.mainloop()
