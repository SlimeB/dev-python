import tkinter
from tkinter.constants import ANCHOR
from typing import Text
mainWindow = tkinter.Tk()
mainWindow.title("calculadora")
mainWindow.geometry("480x640+100+100")


keyPad=tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky="nsew")
keyPad.grid(row=2, column=0, sticky="nsew")
tkinter.Frame(keyPad, width=20, height=20).grid(row=0, column=0)
tkinter.Entry(bg="red").grid(row=2, column=1)
tkinter.Button(keyPad, text="1", anchor="s", padx="5", pady="5").grid(row=1, column=1, sticky="se")
tkinter.Button(keyPad, text="2", anchor="e", padx="5", pady="5").grid(row=1, column=2, sticky="se")

mainWindow.mainloop()
print("programa finalizado")