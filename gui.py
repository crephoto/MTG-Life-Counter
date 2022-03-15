from tkinter import *

screen  = Tk()
#creating text
mylabel = Label(screen, text= "My MTG app!")
#screen size
screen.geometry("600x800")
#put in on the screen
mylabel.pack()
#creates button and displays
btn_2 = Button(screen, text = '2', bd = '5', command = screen.destroy)
btn_2.pack(side = 'top') 
btn_3 = Button(screen, text = '3', bd = '5', command = screen.destroy)
btn_3.pack(side = 'top') 
btn_4 = Button(screen, text = '4', bd = '5', command = screen.destroy)
btn_4.pack(side = 'top') 
btn_5 = Button(screen, text = '5', bd = '5', command = screen.destroy)
btn_5.pack(side = 'top') 
btn_6 = Button(screen, text = '6', bd = '5', command = screen.destroy)
btn_6.pack(side = 'top') 




screen.mainloop()