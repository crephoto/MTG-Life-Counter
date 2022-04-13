import tkinter as tk
from tkinter import *
life = []
lifeStart = 0
player_num = 2
def useless_function(lifeStart, player_num):
    life = [lifeStart]*player_num
    print(str(life))
    return(life)
screen = Tk()
screen.geometry("600x600")
screen. title("Chose how much life you want to start with")
btn1 = Button(screen, text = "20", width = 20, height = 10, command=lambda lifeStart = 20 : useless_function(lifeStart, player_num))
btn2 = Button(screen, text = "40", width = 20, height = 10, command=lambda lifeStart = 40 : useless_function(lifeStart, player_num))
btn1.grid(row = 1, column = 1, ipady=5, ipadx=5)
btn2.grid(row = 2, column = 1, ipady=5, ipadx=5)

screen.mainloop()