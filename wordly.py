import pygame
##import pygame_gui

pygame.init()

#define variables
width = 800
height = 600
yellow = (204,204, 0)
green = (0, 255, 0)
black = (0, 0, 0)
gray = (166, 166, 166)

#define gui; create canvas
pygame.display.set_caption('Wordly')
canvas = pygame.display.set_mode((width, height))

background = pygame.Surface((width, height))
background.fill(pygame.Color('#000000'))

##manager = pygame_gui.UIManager((800, 600))

#draw background into canvas
canvas.blit(background, (0,0))

#draw word/letters container 
pygame.draw.rect(canvas, gray, (50,230,700,140), 5)

for i in range(190, 750, 140):
    pygame.draw.rect(canvas, gray, (i,230,5,140), 5)

#update display
pygame.display.update()

#main logic (with placeholders)

#check if the letter is yellow and repeats

#exit routine
is_running = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
