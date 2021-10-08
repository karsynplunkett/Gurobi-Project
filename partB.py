'''
Candy Land Project

@author Karsyn Plunkett, canvas id: keh0083
@author Malik Robertson, canvas id: mar0061
@author Ann-Marie Willis, canvas id: aew0081

Candy Land Group 10

PART B
'''
import random
import turtle

def create_board():
        board = ['Start']
        
        #Generate the board
        #go through the for loop between 1 and 14
        for i in range(1,14):
                #if i is one of these numbers go through the loop
                #this creates all of the tiles on the board
                if (i == 4 or i == 6 or i == 8 or i == 11):
                        board.append('R' + str(i))
                        #create the peanut tile
                        if (i == 6):
                                board.append('Peanut')
                        board.append('P' + str(i))
                        #create the peppermint tile
                        if (i == 4):
                                board.append('Peppermint')
                        board.append('Y' + str(i))
                        #create the ice Cream tile
                        if (i == 11):
                                board.append('Ice Cream')
                        board.append('B' + str(i))
                        board.append('O' + str(i))
                        #create the lollipop tile
                        if (i == 8):
                                board.append('Lollipop')
                        board.append('G' + str(i))
                #create all of the other tiles for all of the other numbers not included above
                else:
                        board.append('R' + str(i))
                        board.append('P' + str(i))
                        board.append('Y' + str(i))
                        board.append('B' + str(i))
                        board.append('O' + str(i))
                        board.append('G' + str(i))

        board.append('Castle')

        return board
#make the deck 
def make_deck():
        deck = []
        #make 4 cards that are red and purple
        for i in range(1,4):
                deck.append("Red Single")
                deck.append("Purple Single")
        #make 5 cards that are orange, yellow, green, blue
        for j in range(1,5):
                deck.append("Orange Single")
                deck.append("Yellow Single")
                deck.append("Green Single")
                deck.append("Blue Single")
        #make 4 cards that are red, orange, purple, yellow, green, or blue double
        for k in range(1,4):
                deck.append("Red Double")
                deck.append("Orange Double")
                deck.append("Purple Double")
                deck.append("Yellow Double")
                deck.append("Green Double")
                deck.append("Blue Double")
        #make ice cream, peppermint, peanut, lollipop cards
        deck.append('Ice Cream')
        deck.append('Peppermint')
        deck.append('Peanut')
        deck.append('Lollipop')
        #return the deck
        return deck
#function to shuffle the deck
def shuffle_deck(deck):
        random.shuffle(deck)
        return deck
 
#create the positions on the board for each tile on the board in dictionary formation
def pixel_init():
        pixels = {'Start':(-255, -260), 'R1':(-225, -265), 'P1':(-190, -275), 'Y1':(-150, -285), 'B1':(-110, -285), 'O1':(-70,-275), 'G1':(-30,-270),'R2':(10, -270),
                  'P2':(45, -270), 'Y2':(85, -285), 'B2':(120, -290), 'O2':(160,-290), 'G2':(200,-290), 'R3':(225, -260), 'P3':(225, -220), 'Y3':(200, -195),
                  'B3':(160, -195), 'O3':(120,-205), 'G3':(95,-180),'R4':(120, -150),
                  'P4':(160, -150), 'Peppermint':(190, -130), 'Y4':(185, -100), 'B4':(145, -90), 'O4':(105,-95), 'G4':(70,-105), 'R5':(40, -115),
                  'P5':(0, -135), 'Y5':(-30, -160), 'B5':(-60, -185), 'O5':(-90,-200), 'G5':(-125,-210),'R6':(-165, -210), 'Peanut':(-205,-195), 'P6':(-230, -170),
                  'Y6':(-245, -140), 'B6':(-245, -105), 'O6':(-230,-70), 'G6':(-190,-55), 'R7':(-155, -45), 'P7':(-115, -50), 'Y7':(-80, -60), 'B7':(-45, -65),
                  'O7': (-10,-70), 'G7':(25,-65),'R8':(60, -60), 'P8':(100, -50), 'Y8':(135, -35), 'B8':(170, -20), 'O8':(200,0), 'Lollipop':(230,20),
                  'G8':(245,50), 'R9':(215, 60), 'P9':(185, 45), 'Y9':(150, 30), 'B9':(115, 25), 'O9':(90,45), 'G9':(95,75),'R10':(125, 95),
                  'P10':(160, 95), 'Y10':(195, 100), 'B10':(200, 130), 'O10':(165,150), 'G10':(130,150), 'R11':(95, 145), 'P11':(60, 140),
                  'Y11':(25, 130), 'Ice Cream':(0, 110), 'B11':(-25, 85), 'O11':(-50,60), 'G11':(-75,35),'R12':(-110, 15),
                  'P12':(-145, 0), 'Y12':(-185, -5), 'B12':(-215, -10), 'O12':(-245,10), 'G12':(-245,50), 'R13':(-220, 75), 'P13':(-185, 85), 'Y13' : (-150, 90),
                  'B13':(-110, 90), 'O13':(-75,100), 'G13':(-45,120),'Castle':(-20, 150)}

        return pixels
#move the turtles across each tile to get to the position on the board 
def move_turtle(curPos, endPos, pixels, turtle):
        dicList = list(pixels.keys()) #make the dictionary into a list
        if curPos < endPos: # if the turtle is going to go forward go through this loop
                newDicList = dicList[curPos:endPos+1] #make a list for the positions that turtle will go through 

                for item in newDicList:
                        turtle.goto(pixels[item]) #make the turtle go to each tile
        else:
                newDicList = dicList[endPos:curPos + 1]#if the turtle is supposed to move backwards, go through this loop
                newDicList.reverse() #reverse the list
                for item in newDicList:
                        turtle.goto(pixels[item]) #make the turtle go to the postion one tile at a time

#Make the given turtle dance
def turtle_dance(turtle):
        turtle.speed(2)
        turtle.left(45)
        #Make turtle shake back and forth
        for i in range(10):
                turtle.right(90)
                turtle.left(90)
        

def play_game(forward_only=0, end_exact=0): #optional parameters
        #initialize by calling the board, deck, and pixels
        board = create_board()
        deck = make_deck()
        pixels = pixel_init()
        #import turtles. Change the scressnize and window 
        turtle.screensize(540, 720)
        turtle.setup(width=600, height=800)
        #insert the picture
        turtle.bgpic("gameBoard.png")
        #make a turtle and clone it. Change the two colors of the turtles
        player = turtle.Turtle()
        player.color('blue')
        player.shape('turtle')

        computer = player.clone()
        computer.color('Pink')
        #put the pen up and move the turtles to the start position
        player.penup()
        computer.penup()
        player.goto(pixels['Start'])
        computer.goto(pixels['Start'])
        #initialize all variables
        playerPos = 0
        compPos = 0
        oldPlayerPos = 0
        oldCompPos = 0
        groupNumPlayer = 1
        groupNumComputer = 1
        #create the special cases and set their board positions
        peppermintPos = board.index('Peppermint')
        peanutPos = board.index('Peanut')
        lolliPos = board.index('Lollipop')
        iceCreamPos = board.index('Ice Cream')
        licoricePos1 = board.index('P5')
        licoricePos2 = board.index('Y9')
        #initialize the player's turn, and the loss of a player's turn
        cardIndex = 0
        playerTurn = True
        playerLoseTurn = False #both lose turn variables are for when one loses a turn
        computerLoseTurn = False
        endGame = False

        #Begin to play the game
        shuffle_deck(deck)
        print('Your turtle is the blue turtle.') #printing which colored turtle is the user's

        while (endGame == False): #while the end of game still has not occurred, continue going through this loop
                #these cases are for when the player (or computer) has lost a turn, they go through this loop
                if (playerLoseTurn == True and playerTurn == True): #this makes sure the computer goes twice
                        playerTurn = False 
                        playerLoseTurn = False #resets the variable to False when done

                if (computerLoseTurn == True and playerTurn == False):#this makes the player go twice
                        playerTurn = True
                        computerLoseTurn = False #resets the variable to False when done

                if (playerTurn == True):
                        input('Press enter to draw a card ')
                        Card = deck[cardIndex] #Draw Card
                        print('Your card is a ' + Card) #prints the player's card

                if (playerTurn == False):
                        Card = deck[cardIndex] #computer draws a card
                        print('The computer drew a ' + Card + '\n') #computer card is printed
                #These if statements are for each card. You go through each if statement if you have that exact card
                if Card == 'Red Single':
                        #if it is the player's turn go through this loop
                        if (playerTurn == True):
                                oldPlayerPos = playerPos
                                if (playerPos == 0): #if the players position is 0, then set the groupNumber to 0
                                        groupNumPlayer = 0
                                #increment the group number
                                groupNumPlayer = groupNumPlayer + 1
                                if (groupNumPlayer > 13):
                                        playerPos = board.index('Castle')#make the turtle go to castle if the groupnumber is above 13
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['Castle'])

                                else:
                                        playerPos = board.index('R' + str(groupNumPlayer)) #if the groupnumber is not 13 or playposition is not 0, go through
                                        move_turtle(oldPlayerPos, playerPos, pixels, player) #move the turtle to the right color and groupnumber
                                        #player.goto(pixels['R' + str(groupNumPlayer)])

                        else: #if it is the computer's turn, go through this loop
                                oldCompPos = compPos #increment the computer's position
                                if (compPos == 0): #if the computer position is 0, make the groupnumber 0
                                        groupNumComputer = 0
                                #increment the group number of the computer
                                groupNumComputer = groupNumComputer + 1 

                                if (groupNumComputer > 13): #if the computers group number greater than 13, then you make the turtle go straight to castle
                                        compPos = board.index('Castle')
                                        move_turtle(oldCompPos, compPos, pixels, computer)
                                        #computer.goto(pixels['Castle'])

                                else: #if the position is neither 0 nor groupnumber is 13, go through this loop
                                        compPos = board.index('R' + str(groupNumComputer))
                                        move_turtle(oldCompPos, compPos, pixels, computer)#move the turtle to that tile on the board
                                        #computer.goto(pixels['R' + str(groupNumComputer)])                                       
                #if the card drawn is purple, you go through this loop
                elif Card == 'Purple Single': 
                        if (playerTurn == True): #if it is players turn, go through the loop
                                oldPlayerPos = playerPos #change the oldplayers position
                                if playerPos >= board.index('P' + str(groupNumPlayer)): #if the position is greater than the groupNumber you're in, go through this loop
                                        groupNumPlayer = groupNumPlayer + 1 #increment the group number
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, go to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player) 
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('P' + str(groupNumPlayer))#if the new position is not in group 13, go to that tile
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        playerPos = board.index('P' + str(groupNumPlayer)) #if the position is not greater than the place the turtle should go
                                        move_turtle(oldPlayerPos, playerPos, pixels, player) #then you go directly to that tile in group
                                        #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('P' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        groupNumComputer = groupNumComputer + 1 #change the groupnumber to go up one
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('P' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        compPos = board.index('P' + str(groupNumComputer)) #move the turtle in the same group to the right color tile
                                        computer.goto(pixels['P' + str(groupNumComputer)])

                elif Card == 'Yellow Single':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('Y' + str(groupNumPlayer)): #if the position is greater than that color and group number
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('Y' + str(groupNumPlayer))
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        playerPos = board.index('Y' + str(groupNumPlayer))
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('Y' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('Y' + str(groupNumComputer))#move the turtle to the tile corresponding to the new groupnumber
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        compPos = board.index('Y' + str(groupNumComputer))#move the turtle to the tile corresponding to the same groupnumber
                                        computer.goto(pixels['Y' + str(groupNumComputer)])

                elif Card == 'Blue Single':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('B' + str(groupNumPlayer)): #if the position is greater than that color and group number
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('B' + str(groupNumPlayer))#move the turtle to the tile corresponding to the new groupnumber
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        playerPos = board.index('B' + str(groupNumPlayer))#move the turtle to the tile to the same groupnumber, but new color
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('B' + str(groupNumComputer)):#if the position is greater than that color and group number
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('B' + str(groupNumComputer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        compPos = board.index('B' + str(groupNumComputer))
                                        computer.goto(pixels['B' + str(groupNumComputer)])

                elif Card == 'Orange Single':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('O' + str(groupNumPlayer)): #if the position is greater than that color and group number
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('O' + str(groupNumPlayer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        playerPos = board.index('O' + str(groupNumPlayer))
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('O' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('O' + str(groupNumComputer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        compPos = board.index('O' + str(groupNumComputer))
                                        computer.goto(pixels['O' + str(groupNumComputer)])

                elif Card == 'Green Single':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('G' + str(groupNumPlayer)):#if the position is greater than that color and group number
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('G' + str(groupNumPlayer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        playerPos = board.index('G' + str(groupNumPlayer))
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('G' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('G' + str(groupNumComputer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        compPos = board.index('G' + str(groupNumComputer))
                                        computer.goto(pixels['G' + str(groupNumComputer)])


                elif Card == 'Red Double':                                     
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if (playerPos == 0):
                                        groupNumPlayer = 0
                                if (groupNumPlayer == 13 and end_exact == 1):
                                        print("You must land exactly on the castle to win")
                                else:
                                        groupNumPlayer = groupNumPlayer + 2
                                        if (groupNumPlayer > 13):
                                                        playerPos = board.index('Castle')
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('R' + str(groupNumPlayer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['R' + str(groupNumPlayer)])                               
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if (compPos == 0):
                                        groupNumComputer = 0
                                if (groupNumComputer == 13 and end_exact == 1):
                                        continue
                                groupNumComputer = groupNumComputer + 2
                                if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                else:
                                        compPos = board.index('R' + str(groupNumComputer))#move the turtle to the tile corresponding to the new groupnumber and color
                                        move_turtle(oldCompPos, compPos, pixels, computer)
                                        #computer.goto(pixels['R' + str(groupNumComputer)])


                elif Card == 'Purple Double':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('P' + str(groupNumPlayer)): #if the position is greater than that color and group number
                                        if (groupNumPlayer == 13 and end_exact == 1):
                                                print("You must land exactly on the castle to win.")
                                        else:
                                                groupNumPlayer = groupNumPlayer + 2
                                                if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                        playerPos = board.index('Castle')
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['Castle'])

                                                else:
                                                        playerPos = board.index('P' + str(groupNumPlayer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('P' + str(groupNumPlayer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('P' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        if (groupNumComputer == 13 and end_exact == 1):
                                                continue
                                        groupNumComputer = groupNumComputer + 2
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('P' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('P' + str(groupNumComputer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                elif Card == 'Yellow Double':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('Y' + str(groupNumPlayer)): #if the position is greater than that color and group number
                                        if (groupNumPlayer == 13 and end_exact == 1):
                                                print("You must land exactly on the castle to win.")
                                        else:
                                                groupNumPlayer = groupNumPlayer + 2
                                                if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                        playerPos = board.index('Castle')
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['Castle'])

                                                else:
                                                        playerPos = board.index('Y' + str(groupNumPlayer))#move the turtle to the tile corresponding to the new groupnumber and color
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('Y' + str(groupNumPlayer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('Y' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        if (groupNumComputer == 13 and end_exact == 1):
                                                continue
                                        groupNumComputer = groupNumComputer + 2
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('Y' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('Y' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])


                elif Card == 'Blue Double':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('B' + str(groupNumPlayer)): #if the position is greater than that color and group number
                                        if (groupNumPlayer == 13 and end_exact == 1):
                                                print("You must land exactly on the castle to win.")
                                        else:
                                                groupNumPlayer = groupNumPlayer + 2
                                                if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                        playerPos = board.index('Castle')
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['Castle'])

                                                else:
                                                        playerPos = board.index('B' + str(groupNumPlayer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('B' + str(groupNumPlayer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('B' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        if (groupNumComputer == 13 and end_exact == 1):
                                                continue
                                        groupNumComputer = groupNumComputer + 2
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('B' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('B' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])


                elif Card == 'Orange Double':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('O' + str(groupNumPlayer)): #if the position is greater than that color and group number
                                        if (groupNumPlayer == 13 and end_exact == 1):
                                                print("You must land exactly on the castle to win.")
                                        else:
                                                groupNumPlayer = groupNumPlayer + 2
                                                if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                        playerPos = board.index('Castle')
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['Castle'])

                                                else:
                                                        playerPos = board.index('O' + str(groupNumPlayer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('O' + str(groupNumPlayer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('O' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        if (groupNumComputer == 13 and end_exact == 1):
                                                continue
                                        groupNumComputer = groupNumComputer + 2
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('O' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('O' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                elif Card == 'Green Double':
                        if (playerTurn == True): #if it is the player's turn go through this loop
                                oldPlayerPos = playerPos
                                if playerPos >= board.index('G' + str(groupNumPlayer)): #if the position is greater than that color and group number
                                        if (groupNumPlayer == 13 and end_exact == 1):
                                                print("You must land exactly on the castle to win.")
                                        else:
                                                groupNumPlayer = groupNumPlayer + 2
                                                if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                        playerPos = board.index('Castle')
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['Castle'])

                                                else:
                                                        playerPos = board.index('G' + str(groupNumPlayer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                        #player.goto(pixels['P' + str(groupNumPlayer)])

                                else:
                                        groupNumPlayer = groupNumPlayer + 1
                                        if (groupNumPlayer > 13): #if the group number is greater than 13, move to the castle
                                                playerPos = board.index('Castle')
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Castle'])

                                        else:
                                                playerPos = board.index('G' + str(groupNumPlayer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['P' + str(groupNumPlayer)])
                        #if it is the computers turn, go through this loop instead
                        else:
                                oldCompPos = compPos
                                if compPos >= board.index('G' + str(groupNumComputer)): #if the position is greater than that color and group number
                                        if (groupNumComputer == 13 and end_exact == 1):
                                                continue
                                        groupNumComputer = groupNumComputer + 2
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('G' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                                else:
                                        groupNumComputer = groupNumComputer + 1
                                        if (groupNumComputer > 13): #if the group number is greater than 13, move to the castle
                                                compPos = board.index('Castle')
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Castle'])

                                        else:
                                                compPos = board.index('G' + str(groupNumComputer)) #move the turtle to the tile corresponding to the new groupnumber and color
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['P' + str(groupNumComputer)])

                elif Card == 'Peppermint':
                        if forward_only == 0:
                                if (playerTurn == True): #if it is the player's turn go through this loop
                                        oldPlayerPos = playerPos
                                        playerPos = peppermintPos
                                        groupNumPlayer = 4
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['Peppermint'])

                                else:
                                        oldCompPos = compPos
                                        compPos = peppermintPos
                                        groupNumComputer = 4
                                        move_turtle(oldCompPos, compPos, pixels, computer)
                                        #computer.goto(pixels['Peppermint'])

                        else:
                                if (playerTurn == True): #if it is the player's turn go through this loop
                                        if (playerPos > peppermintPos):
                                                print("This is forward only mode, please stay put")
                                        else:
                                                oldPlayerPos = playerPos
                                                playerPos = peppermintPos
                                                groupNumPlayer = 4
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Peppermint'])
                                #if it is the computers turn, go through this loop instead
                                else:
                                        if (compPos < peppermintPos):
                                                oldCompPos = compPos
                                                compPos = peppermintPos
                                                groupNumComputer = 4
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Peppermint'])

                elif Card == 'Peanut':
                        if forward_only == 0:
                                if (playerTurn == True): #if it is the player's turn go through this loop
                                        oldPlayerPos = playerPos
                                        playerPos = peanutPos
                                        groupNumPlayer = 6
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['Peppermint'])
                                #if it is the computers turn, go through this loop instead
                                else:
                                        oldCompPos = compPos
                                        compPos = peanutPos
                                        groupNumComputer = 6
                                        move_turtle(oldCompPos, compPos, pixels, computer)
                                        #computer.goto(pixels['Peppermint'])

                        else:
                                if (playerTurn == True):#if it is the player's turn go through this loop
                                        if (playerPos > peanutPos):
                                                print("This is forward only mode, please stay put")
                                        else:
                                                oldPlayerPos = playerPos
                                                playerPos = peanutPos
                                                groupNumPlayer = 6
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Peppermint'])
                                #if it is the computers turn, go through this loop instead
                                else:
                                        if (compPos < peanutPos):
                                                oldCompPos = compPos
                                                compPos = peanutPos
                                                groupNumComputer = 6
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Peppermint'])

                elif Card == 'Lollipop':
                        if forward_only == 0:
                                if (playerTurn == True): #if it is the player's turn go through this loop
                                        oldPlayerPos = playerPos
                                        playerPos = lolliPos
                                        groupNumPlayer = 8
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['Peppermint'])
                                #if it is the computers turn, go through this loop instead
                                else:
                                        oldCompPos = compPos
                                        compPos = lolliPos
                                        groupNumComputer = 8
                                        move_turtle(oldCompPos, compPos, pixels, computer)
                                        #computer.goto(pixels['Peppermint'])

                        else:
                                if (playerTurn == True):#if it is the player's turn go through this loop
                                        if (playerPos > lolliPos):
                                                print("This is forward only mode, please stay put")
                                        else:
                                                oldPlayerPos = playerPos
                                                playerPos = lolliPos
                                                groupNumPlayer = 8
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Peppermint'])
                                #if it is the computers turn, go through this loop instead
                                else:
                                        if (compPos < lolliPos):
                                                oldCompPos = compPos
                                                compPos = lolliPos
                                                groupNumComputer = 8
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Peppermint'])

                elif Card == 'Ice Cream':
                        if forward_only == 0:
                                if (playerTurn == True): #if it is the player's turn go through this loop
                                        oldPlayerPos = playerPos
                                        playerPos = iceCreamPos
                                        groupNumPlayer = 11
                                        move_turtle(oldPlayerPos, playerPos, pixels, player)
                                        #player.goto(pixels['Peppermint'])
                                #if it is the computers turn, go through this loop instead
                                else:
                                        oldCompPos = compPos
                                        compPos = iceCreamPos
                                        groupNumComputer = 11
                                        move_turtle(oldCompPos, compPos, pixels, computer)
                                        #computer.goto(pixels['Peppermint'])

                        else:
                                if (playerTurn == True): #if it is the player's turn go through this loop
                                        if (playerPos > iceCreamPos):
                                                print("This is forward only mode, please stay put")
                                        else:
                                                oldPlayerPos = playerPos
                                                playerPos = iceCreamPos
                                                groupNumPlayer = 11
                                                move_turtle(oldPlayerPos, playerPos, pixels, player)
                                                #player.goto(pixels['Peppermint'])
                                #if it is the computers turn, go through this loop instead
                                else:
                                        if (compPos < iceCreamPos):
                                                oldCompPos = compPos
                                                compPos = iceCreamPos
                                                groupNumComputer = 11
                                                move_turtle(oldCompPos, compPos, pixels, computer)
                                                #computer.goto(pixels['Peppermint'])

                if (playerTurn == True): #if it is the player's turn go through this loop
                        #if player lands on B1, automatically move to B6
                        if playerPos == board.index('B1'):
                                playerPos = board.index('B6')
                                groupNumPlayer = 6 #change group number to 6
                                player.goto(pixels['B6'])
                        #if player lands on G3, automatically move to G4
                        elif playerPos == board.index('G3'):
                                playerPos = board.index ('G4')
                                groupNumPlayer = 4 #change the group number to 4
                                player.goto(pixels['G4'])
                        #if the player lands on either licorice, they lose a turn. set player Lose turn to true
                        elif playerPos == licoricePos1 or playerPos == licoricePos2:
                                print('Sorry, you lose a turn')
                                playerLoseTurn = True
                        #if the player lands on castle, end the game
                        elif playerPos == board.index('Castle'):
                                endGame = True
                                print('You are the winner!')
                                turtle_dance(player) #Make the winning turtle dance
                
                #if it is the computers turn, go through this loop instead
                else:
                        #if comp lands on B1, automatically move to B6
                        if compPos == board.index('B1'):
                                compPos = board.index('B6')
                                groupNumComputer = 6 #change group number to 6
                                computer.goto(pixels['B6'])
                        #if comp lands on G3, automatically move to G4
                        elif compPos == board.index('G3'):
                                compPos = board.index ('G4')
                                groupNumComputer = 4 #change the group number to 4
                                computer.goto(pixels['G4'])
                        #if the computer lands on either licorice, they lose a turn. set computer Lose turn to true
                        elif compPos == licoricePos1 or compPos == licoricePos2:
                                computerLoseTurn = True
                        #if the computer lands on castle, end the game
                        elif compPos == board.index('Castle'):
                                endGame = True
                                print('Sorry, you lost.... better luck next time')
                                turtle_dance(computer) #Make the winning turtle dance
                #if it is the player's turn, change playerTurn to false to make the computer go
                if (playerTurn == True):
                        playerTurn = False
                        
                #if it is the computer's turn, change playerTurn to true to make the player go
                else:
                        playerTurn = True
                #increment the card index each time the game goes through the while loop
                cardIndex = cardIndex + 1

#Main Code
play_game()

