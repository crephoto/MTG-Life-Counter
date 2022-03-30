import tkinter as tk

DRAW_HEIGHT = 560
DRAW_WIDTH = 560
PALETTE_HEIGHT = 40

def draw_palette(canvas):
    canvas.create_rectangle(0, 0, DRAW_WIDTH, PALETTE_HEIGHT, fill = 'light grey', width= 0)
    canvas.create_rectangle(DRAW_WIDTH/8, PALETTE_HEIGHT/5, 3*DRAW_WIDTH/8, 4*PALETTE_HEIGHT/5, fill = 'dark grey', width = 1)
    canvas.create_rectangle(5*DRAW_WIDTH/8, PALETTE_HEIGHT/5, 7*DRAW_WIDTH/8, 4*PALETTE_HEIGHT/5, fill = 'dark grey',width = 1)
    canvas.create_text(DRAW_WIDTH/4, PALETTE_HEIGHT/2, text = 'clear screen') #non-functional
    
class Brush():
    def __init__(self,stroke_size,stroke_color):
        self.size = stroke_size
        self.color = stroke_color
        self.mode = 'draw'
        self.pos = (0,0)
        self.clicked = False
        
    def render(self,canvas):
        if self.clicked:
            canvas.create_oval( self.pos.x-self.size/2, self.pos.y-self.size/2,
                                self.pos.x+self.size/2, self.pos.y+self.size/2,
                                width = 0, fill = self.color )
            
    def mouse_moved(self,event):
        self.pos = event
    
    def mouse_clicked(self,throwaway):
        self.clicked = True
    
    def mouse_released(self,throwaway):
        self.clicked = False


#set up root window and canvas
root = tk.Tk()
root.geometry('{}x{}'.format(DRAW_WIDTH,DRAW_HEIGHT+PALETTE_HEIGHT))
c = tk.Canvas(root, width = DRAW_WIDTH, height = DRAW_HEIGHT + PALETTE_HEIGHT, bg = 'white')
c.pack()

b = Brush(40,'black')

#bind actions to functions
c.bind("<Button-1>",b.mouse_clicked)
c.bind("<ButtonRelease-1>",b.mouse_released)
c.bind("<Motion>",b.mouse_moved)

#main loop
while 1:
    b.render(c)
    draw_palette(c)
    root.update()