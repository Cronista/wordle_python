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

#main logic
#create the Draw and Try dictionaries
tryDict = {
        1: {"value": "", "repeat": 0, "color": [0, 0, 0]},
        2: {"value": "", "repeat": 0, "color": [0, 0, 0]},
        3: {"value": "", "repeat": 0, "color": [0, 0, 0]},
        4: {"value": "", "repeat": 0, "color": [0, 0, 0]},
        5: {"value": "", "repeat": 0, "color": [0, 0, 0]}
    }

drawDict = {
        1: {"value": "", "repeat": 0, "color": [0, 0, 0]},
        2: {"value": "", "repeat": 0, "color": [0, 0, 0]},
        3: {"value": "", "repeat": 0, "color": [0, 0, 0]},
        4: {"value": "", "repeat": 0, "color": [0, 0, 0]},
        5: {"value": "", "repeat": 0, "color": [0, 0, 0]}
    }

def wordle():

    while gameover == False:

        #populate tryDict with user input(not done yet)
            
        #check for input length
        if tryDict[i]["value"] == '':
            print(f'Five letter words only.\n')
            input()
            wordle() #exit if loop only, not entire game loop

        #more checks (not done yet)

 #check if it is yellow and repeats (not done yet)
def yellowAndRepeats(dict1, dict2):

#update the attempts list, tries
def tryListUpdate():

#check if the game is over or present the score if won
def gameStatus(dict1, dict2): 

#reset the game. Whole routine
def reset():

#update the virtual keyboard with the status of letters used: black, gray, yellow or green
def keyboard():

#exit routine
is_running = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
