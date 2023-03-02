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
        
        wordLength(tryDict)
        
        yellowAndRepeats(drawDict, tryDict)
        
        checkForGreen(drawDict, tryDict)
        
        missYellowry(drawDict, tryDict)
        
        tryListUpdate()
        
#more checks (not done yet)
        
#check for input length. Five letter words only
def wordLength(tryVar):
    
    for i in tryVar:
        
        if tryVar[i]["value"] == '':

            print(f'Five letter words only.\n')
            input()
            wordle()
            
#check if it is yellow and repeats
def yellowAndRepeats(drawVar, tryVar):
    
    #double For Loop to check various conditions on the nature of each letter in tryDict and drawDict
    for i in range(1,6):

        for i2 in range(1,6):

            #check for same letter within drawDict
            if drawVar[i]["value"] == drawVar[i2]["value"]:
                drawVar[i]["repeat"] += 1 

            #check for same letter within tryDict
            if tryVar[i]["value"] == tryVar[i2]["value"]:
                tryVar[i]["repeat"] += 1

            #color yellow letters that are equal between drawDict and tryDict that were not yet evaluated as such
            if (drawVar[i]["value"] == tryVar[i2]["value"] and
                drawVar[i]["color"] != [204, 204, 0] and
                tryVar[i2]["color"] != [204, 204, 0]
            ):
                drawVar[i]["color"] = [204, 204, 0]
                tryVar[i2]["color"] = [204, 204, 0]
                #call keyboard function to update the virtual keyboard
                keyboard(i2, "colorType")

#verify and color green when the letters are equal and on the same position
def checkForGreen(drawVar, tryVar):

    for i in range(1,6):

        if drawVar[i]["value"] == tryVar[i]["value"]:
            drawVar[i]["color"] = [0, 255, 0]
            tryVar[i]["color"] = [0, 255, 0]
            keyboard(i, "colorType")
            keyboard(i, "blackType")

#check whether a rogue yellow was mistakenly colored and remove it 
def missYellowry(drawVar, tryVar):

    for oneYellowIndex in range(1,6):

        for twoYellowIndex in range(1,6):

            if (tryVar[oneYellowIndex]["value"] == drawVar[twoYellowIndex]["value"] and

                tryVar[oneYellowIndex]["color"] != drawVar[twoYellowIndex]["color"] and

                tryVar[oneYellowIndex]["color"] != [0, 255, 0] and
                
                drawVar[twoYellowIndex]["repeat"] < tryVar[oneYellowIndex]["repeat"]
            ):
                tryVar[oneYellowIndex]["color"] = [0, 0, 0]


#update the attempts list, tries
def tryListUpdate():

#check if the game is over or present the score if won
def gameStatus(dict1, dict2): 

#reset the game. Whole routine
def reset():

#update the virtual keyboard with the color information of each letter used in the attempt: black, gray, yellow or green
def keyboard(currentIndex, type):

#exit routine
is_running = True

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
