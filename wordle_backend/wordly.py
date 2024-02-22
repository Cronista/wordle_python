import pygame
import random
#import pygame_gui

#color definition
yellow = [204,204, 0]
green = [0, 255, 0]
black = [0, 0, 0]
gray = [166, 166, 166]

#create the Draw and Try dictionaries
tryDict = {
        1: {"value": "", "repeat": 0, "color": black},
        2: {"value": "", "repeat": 0, "color": black},
        3: {"value": "", "repeat": 0, "color": black},
        4: {"value": "", "repeat": 0, "color": black},
        5: {"value": "", "repeat": 0, "color": black}
    }

drawDict = {
        1: {"value": "", "repeat": 0, "color": black},
        2: {"value": "", "repeat": 0, "color": black},
        3: {"value": "", "repeat": 0, "color": black},
        4: {"value": "", "repeat": 0, "color": black},
        5: {"value": "", "repeat": 0, "color": black}
    }

#end game counters
#win messages
winmsg = ["Inacreditável...", "Incrível!", "Sensacional!", "Muito bom", "Bom", "Ufa!"] 

#var to check if maximum attempts were reached
tryPos = 0
gameover = False

#variable to store attempted word for indexing
bindTryDict = ""

#main logic  
def wordle():

    global gameover, tryPos
    
    while gameover == False:

        userInput(tryDict)

        checkIfWordList(tryDict)

        userInputReset()
        
        yellowAndRepeats(drawDict, tryDict)
        
        checkForGreen(drawDict, tryDict)
        
        missYellowry(drawDict, tryDict)
        
        resetDrawTry("RC", "R")

        doAccentTryDict(tryDict)

        tryListUpdate()

        if gameStatus(tryDict) == 5:

            for i in range(6):

                if tryPos == i:

                    print(winmsg[i])
                    print("\n")
                    input()

                    resetDicts_EndVars()
                    tryListClear()
                    keyboardClear()
                    draw()
                    wordle()

        #print visuals return text; debug/playtest
        for i in tryDict:

            print(
                tryDict[i]["value"] + 
                str(tryDict[i]["color"]), 
                end=" "
                )
        
        print("\n")

        resetDrawTry("", "C")

        tryPos += 1

        if tryPos == 6:

            gameover = True
            print(draw()[1])
            print("\n")
            input()

            resetDicts_EndVars()
            tryListClear()
            keyboardClear()
            draw()
            wordle()    

def draw():

    #word list and word draw management
    #open uppercase word list, format and store it in a variable
    with open("lista_palavras_semAcent_maisc.txt","r") as file:
        
        strippy = [lines.strip() for lines in file]

    #random draw and assignment to drawDict
    strippyRand = strippy[random.randint(1, 3000)]
    for i in drawDict:

        drawDict[i]["value"] = strippyRand[i-1]

    #variable to store draw index position on "lista_palavras_semAcent_maisc.txt"
    indexDraw = strippy.index(strippyRand)

    return indexDraw, strippyRand

draw()

#user input into tryDict. Text only. Will be converted to GUI.
def userInput(tryVar):

    uInput = input()

    #check for input length before assigning to dict. Five letter words only
    if len(uInput) != 5:

        print(f'Apenas palavras de cinco letras.\n')
        wordle()

    for i in tryVar:

        tryVar[i]["value"] = uInput[i-1]

#check if the current attempt is in the word list. No 3000 words limit.
def checkIfWordList(tryVar):

    global bindTryDict

    with open("lista_palavras_semAcent_maisc.txt","r") as file:
    
        strippy = [lines.strip() for lines in file]

    for i in tryVar:

        bindTryDict += tryVar[i]["value"]

    if not bindTryDict in strippy:

        print(f"Palavra inválida.\n")
        bindTryDict = ""
        wordle()        

#clear the user input field
def userInputReset():
    #todo
    return None
            
#check if the letter is yellow and if it repeats
def yellowAndRepeats(drawVar, tryVar):  

    #unested double For Loop to check various conditions on the nature of each letter in tryDict and drawDict
    for j in range(len(drawVar) * len(tryVar)):

        i, i2 = divmod(j, len(tryVar))

        #check for same letter within drawDict
        if drawVar[i+1]["value"] == drawVar[i2+1]["value"]:

            drawVar[i+1]["repeat"] += 1 

        #check for same letter within tryDict
        if tryVar[i+1]["value"] == tryVar[i2+1]["value"]:

            tryVar[i+1]["repeat"] += 1

        #color letters yellow that are equal between drawDict and tryDict that were not yet evaluated as such
        if (drawVar[i+1]["value"] == tryVar[i2+1]["value"] and

            drawVar[i+1]["color"] != yellow and

            tryVar[i2+1]["color"] != yellow
        ):
            drawVar[i+1]["color"] = yellow

            tryVar[i2+1]["color"] = yellow

            #call keyboard function to update the virtual keyboard
            keyboard(i2+1, "colorType")

#verify and color green when the letters are equal and on the same position
def checkForGreen(drawVar, tryVar):

    for i in range(1,6):

        if drawVar[i]["value"] == tryVar[i]["value"]:

            drawVar[i]["color"] = green

            tryVar[i]["color"] = green

            keyboard(i, "colorType")
            keyboard(i, "blackType")

#check whether a rogue yellow was mistakenly colored and remove it 
def missYellowry(drawVar, tryVar):

    for j in range(len(drawVar) * len(tryVar)):

        oneYellowIndex, twoYellowIndex = divmod(j, len(tryVar))

        if (tryVar[oneYellowIndex + 1]["value"] == drawVar[twoYellowIndex + 1]["value"] and

            tryVar[oneYellowIndex + 1]["color"] != drawVar[twoYellowIndex + 1]["color"] and

            tryVar[oneYellowIndex + 1]["color"] != green and
            
            drawVar[twoYellowIndex + 1]["repeat"] < tryVar[oneYellowIndex + 1]["repeat"]
        ):
            tryVar[oneYellowIndex + 1]["color"] = black

#reset the values information from the try and draw dictionaries, setting up for the next attempt
def resetDrawTry(drawType, tryType):

    #repeat reset
    if "R" in drawType:

        for i in drawDict:

            drawDict[i]["repeat"] = 0

    if "R" in tryType:

        for i in tryDict:

            tryDict[i]["repeat"] = 0
    
    #color reset 
    if "C" in drawType:

        for i in drawDict:

            drawDict[i]["color"] = black

    if "C" in tryType:

        for i in tryDict:

            tryDict[i]["color"] = black

#match unaccented charaters in "...semAcen..." list with "lista_palavras.txt" to tryDict
def doAccentTryDict(tryVar):

    global bindTryDict

    with open("lista_palavras.txt","r") as file:

        strippy = [lines.strip() for lines in file]

    with open("lista_palavras_semAcent_maisc.txt", "r") as file:

        strippySemAcent = [lines.strip() for lines in file]

    for i in tryVar:

        tryVar[i]["value"] = strippy[strippySemAcent.index(bindTryDict)][i-1].upper()

    #reset bindTryDict for next attempt
    bindTryDict = ""

#update the attempts list
def tryListUpdate():
    #todo
    return None

#check the game score
def gameStatus(tryVar): 

    count = 0
    for i in tryVar:

        if tryVar[i]["color"] == green:

            count += 1

    return count

#reset the dictionaries and end game variables
def resetDicts_EndVars():

    global tryPos, gameover
    tryPos = 0
    gameover = False

    for i in tryDict:

        tryDict[i]["value"] = ""

        tryDict[i]["repeat"] = 0

        tryDict[i]["color"] = black

        drawDict[i]["value"] = ""

        drawDict[i]["repeat"] = 0
        
        drawDict[i]["color"] = black

#clear the attempts list
def tryListClear():
    #todo
    return None

#clear the virtual keyboard
def keyboardClear():
    #todo
    return None

#update the virtual keyboard with the color information of each letter used in the attempt: black, gray, yellow or green
def keyboard(currentIndex, type):
    #todo
    return None

# pygame.init()

# #define variables
# width = 800
# height = 600

# #define gui; create canvas
# pygame.display.set_caption('Wordly')
# canvas = pygame.display.set_mode((width, height))

# background = pygame.Surface((width, height))
# background.fill(pygame.Color('#000000'))

# ##manager = pygame_gui.UIManager((800, 600))

# #draw background into canvas
# canvas.blit(background, (0,0))

# #draw word/letters container 
# pygame.draw.rect(canvas, gray, (50,230,700,140), 5)

# for i in range(190, 750, 140):
#     pygame.draw.rect(canvas, gray, (i,230,5,140), 5)

# #update display
# pygame.display.update()

#start    
wordle()

# #exit routine
# is_running = True

# while is_running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             is_running = False

