from tkinter import *

screen  = Tk()
#creating text
mylabel = Label(screen, text= "Welcome! Choose how many players are playing.")

screen.title("The best MTG App!")
#screen size
screen.geometry("600x600")

#creates button
btn_2 = Button(screen, text = '2', command = screen.destroy)
btn_3 = Button(screen, text = '3', command = screen.destroy)
btn_4 = Button(screen, text = '4', command = screen.destroy)
btn_5 = Button(screen, text = '5', command = screen.destroy)
btn_6 = Button(screen, text = '6', command = screen.destroy)
#Set Grid
mylabel.grid(row=0, column=0,sticky="NSEW")
btn_2.grid(row=1, column=0,sticky="NSEW")
btn_3.grid(row=2, column=0,sticky="NSEW")
btn_4.grid(row=3, column=0,sticky="NSEW")
btn_5.grid(row=4, column=0,sticky="NSEW")
btn_6.grid(row=5, column=0,sticky="NSEW")

#configue our column and rows
row_number = 1
Grid.columnconfigure(screen, 0, weight=1)
button_list = [btn_2, btn_3, btn_4, btn_5, btn_6]
for button in button_list:
    Grid.rowconfigure(screen, row_number, weight=1)
    row_number+=1







screen.mainloop()