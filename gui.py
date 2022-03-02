from cmath import rect
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 800))
main_font = pygame.font.SysFont("Cambria",32)
#colors
white = (225, 225, 225)
cyan = (0,225,225)
megenta = (255, 0, 255)

screen.fill(megenta)


#button image
start_img = pygame.image.load(r"\\ct-aa-fp1.ct.k12itc.us\000127524\Documents\python\MTG-Life-Counter\il_794xN.1424581313_cu13.jpg").convert_alpha()


#create button and define size
#class Button():
#    def __init__(self, image, x_pos ,y_pos, text_input):
#        self.image = image
#        self.x_pos = x_pos
#        self.y_pos = y_pos
#        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
#        self.text_input = text_input
#        self.text = main_font.render(self.text_input, True, "white")
#        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
#
#    def update(self):
#	    
#button_surface = pygame.image.load("button.png")
#button_surface = pygame.transform.scale(button_surface, (400, 150))
#button = Button(button_surface, 400, 300, "Button")




#loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    pygame.display.flip()


