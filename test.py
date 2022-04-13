from cProfile import label
import tkinter as tk
from tkinter import *
def clear_frame():
    for widgets in screen.winfo_children():
        widgets.destroy()
def player_list_add(name, players):
    players.append(name)
    print(players)
    return(players)
player_num = 4
players = []
screen = Tk()
screen.geometry("600x600")
screen. title("What are the payers names")
for i in range(player_num):
    la_bell = Label(screen, text="What is the name of player" + str(i) + "?")
    textBox = Entry(screen, width = 25,)
    conbtn1 = Button(screen, text = "Submit", command=lambda player = textBox.get : player_list_add(la_bell.get))
    la_bell.grid(column = 1, row=1)
screen.mainloop()