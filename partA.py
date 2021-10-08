# -*- coding: utf-8 -*-
"""
Candy Land Project

@author Karsyn Plunkett, canvas id: keh0083
@author Malik Robertson, canvas id: mar0061
@author Ann-Marie Willis, canvas id: aew0081

Candy Land Group 10

PART A
"""
import random

def create_board():
        board = ['Start']
        #Generate the board  by creating a list
        for i in range(1,14):
                #append each of these colors onto the list in order by labeling by color letter and group number
                if (i == 4 or i == 6 or i == 8 or i == 11):
                        board.append('R' + str(i))
                        if (i == 6):
                                board.append('Peanut')
                        board.append('P' + str(i))
                        if (i == 4):
                                board.append('Peppermint')
                        board.append('Y' + str(i))
                        if (i == 11):
                                board.append('Ice Cream')
                        board.append('B' + str(i))
                        board.append('O' + str(i))
                        if (i == 8):
                                board.append('Lollipop')
                        board.append('G' + str(i))
                else:
                        board.append('R' + str(i))
                        board.append('P' + str(i))
                        board.append('Y' + str(i))
                        board.append('B' + str(i))
                        board.append('O' + str(i))
                        board.append('G' + str(i))
        board.append('Castle') #append the castle to the list
        return board
#make the deck by making the correct number of single and double colors        
def make_deck():
        deck = []
        for i in range(1,4):
                deck.append("Red Single")
                deck.append("Purple Single")
        for j in range(1,5):
                deck.append("Orange Single")
                deck.append("Yellow Single")
                deck.append("Green Single")
                deck.append("Blue Single")
        for k in range(1,4):
                deck.append("Red Double")
                deck.append("Orange Double")
                deck.append("Purple Double")
                deck.append("Yellow Double")
                deck.append("Green Double")
                deck.append("Blue Double")
        #make one of each of the special cards
        deck.append('Ice Cream')
        deck.append('Peppermint')
        deck.append('Peanut')
        deck.append('Lollipop')
        return deck
#shuffle the deck to make the game more random and realistic 
def shuffle_deck(deck):
        random.shuffle(deck)
        return deck

def play_game():
        #call the board and deck functions from above
        board = create_board()
        deck = make_deck()
        #initalize position and group number
        compPos = 0
        groupNum = 1
        #label each special case position on the board
        peppermintPos = board.index('Peppermint')
        peanutPos = board.index('Peanut')
        lolliPos = board.index('Lollipop')
        iceCreamPos = board.index('Ice Cream')
        licoricePos1 = board.index('P5')
        licoricePos2 = board.index('Y9')
        #initialize card index and number of moves to 0
        cardIndex = 0
        numMoves = 0
        #initialize end game to false so the game can start
        endGame = False
        
        #Begin to play the game
        shuffle_deck(deck)
        #go through this loop until the game has ended
        while (endGame == False):
               playerCard = deck[cardIndex] #Draw Card
              #for the card drawn go through the loop that specifies the appropriate card
               if playerCard == 'Red Single':
                       #for the first red single card drawn, if the position is 0, make the group number to 0
                        if compPos == 0:
                               groupNum = 0
                        #increment the group number
                        groupNum = groupNum + 1
                        if (groupNum > 13): #if the group number is greater than 13, go to the castle
                               compPos = board.index('Castle')
                        else:
                                #go to the next red position which is R and the group number (ex 'R1')
                               compPos = board.index('R' + str(groupNum))
                #if the card drawn is purple single
               elif playerCard == 'Purple Single':
                       #if the position is ahead of the current P with the same group number then increment group number up
                       if compPos >= board.index('P' + str(groupNum)):
                               groupNum = groupNum + 1
                               if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                               else:
                                       #change the position to the next P with the new group number
                                       compPos = board.index('P' + str(groupNum))
                                       
                       else:
                               #if the current position is before the next purple in that group, then go to the purple in that group 
                               compPos = board.index('P' + str(groupNum))
                               
               elif playerCard == 'Yellow Single':
                       #if the position is ahead of the current Y with the same group number then increment group number up
                       if compPos >= board.index('Y' + str(groupNum)):
                               groupNum = groupNum + 1
                               if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                               else:
                                       #change the position to the next Y with the new group number
                                       compPos = board.index('Y' + str(groupNum))
                                       
                       else:
                               #if the current position is before the next yellow in that group, then go to the yellow in that group
                               compPos = board.index('Y' + str(groupNum))
                               
               elif playerCard == 'Blue Single':
                       #if the position is ahead of the current B with the same group number then increment group number up
                       if compPos >= board.index('B' + str(groupNum)):
                               groupNum = groupNum + 1
                               if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                               else:
                                       #change the position to the next B with the new group number
                                       compPos = board.index('B' + str(groupNum ))
                                       
                       else:
                               #if the current position is before the next blue in that group, then go to the blue in that group
                               compPos = board.index('B' + str(groupNum))
                               
               elif playerCard == 'Orange Single':
                       #if the position is ahead of the current O with the same group number then increment group number up
                       if compPos >= board.index('O' + str(groupNum)):
                               groupNum = groupNum + 1
                               if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                               else:
                                       #change the position to the next O with the new group number
                                       compPos = board.index('O' + str(groupNum))
                                       
                       else:
                               #if the current position is before the next orange in that group, then go to the orange in that group
                               compPos = board.index('O' + str(groupNum))
                               
               elif playerCard == 'Green Single':
                       #if the position is ahead of the current G with the same group number then increment group number up
                      if compPos >= board.index('G' + str(groupNum)):
                              groupNum = groupNum + 1
                              if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                              else:
                                       compPos = board.index('G' + str(groupNum))
                                       
                      else:
                              #if the current position is before the next green in that group, then go to the green in that group
                               compPos = board.index('G' + str(groupNum))
                       
               elif playerCard == 'Red Double':
                       #if the comp position is 0, then set the group number to 0
                        if (compPos == 0):
                               groupNum = 0
                        groupNum = groupNum + 2
                        if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                compPos = board.index('Castle')
                        else:
                                #change the position to the next R with the new group number
                                compPos = board.index('R' + str(groupNum))
                       
               elif playerCard == 'Purple Double':
                       #if the position is ahead of the current P with the same group number then increment group number up
                       if compPos >= board.index('P' + str(groupNum)):
                                groupNum = groupNum + 2 #increment group number
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next P with the new group number
                                        compPos = board.index('P' + str(groupNum))
                       #if the position is before the purple in the current group you are in then go through this loop and increment group number one                 
                       else:
                                groupNum = groupNum + 1 #increment group number
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next P with the new group number
                                        compPos = board.index('P' + str(groupNum))
                               
               elif playerCard == 'Yellow Double':
                       #if the position is ahead of the current Y with the same group number then increment group number up
                       if compPos >= board.index('Y' + str(groupNum)):
                                groupNum = groupNum + 2
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next Y with the new group number
                                        compPos = board.index('Y' + str(groupNum))
                        #if the position is before the Yellow in the current group you are in then go through this loop and increment group number one       
                       else:
                                groupNum = groupNum + 1
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next Y with the new group number
                                        compPos = board.index('Y' + str(groupNum))
                               
               elif playerCard == 'Blue Double':
                       #if the position is ahead of the current B with the same group number then increment group number up
                       if compPos >= board.index('B' + str(groupNum)):
                                groupNum = groupNum + 2
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next B with the new group number
                                        compPos = board.index('B' + str(groupNum))
                        
                        #if the position is before the Blue in the current group you are in then go through this loop and increment group number one       
                       else:
                                groupNum = groupNum + 1
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next B with the new group number
                                        compPos = board.index('B' + str(groupNum))
                                        
               elif playerCard == 'Orange Double':
                       #if the position is ahead of the current O with the same group number then increment group number up
                       if compPos >= board.index('O' + str(groupNum)):
                                groupNum = groupNum + 2
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next O with the new group number
                                        compPos = board.index('O' + str(groupNum))
                        
                        #if the position is before the Orange in the current group you are in then go through this loop and increment group number one       
                       else:
                                groupNum = groupNum + 1
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next O with the new group number
                                        compPos = board.index('O' + str(groupNum))
                                        
               elif playerCard == 'Green Double':
                       #if the position is ahead of the current G with the same group number then increment group number up
                       if compPos >= board.index('G' + str(groupNum)):
                                groupNum = groupNum + 2
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next G with the new group number
                                        compPos = board.index('G' + str(groupNum))
                       #if the position is before the Green in the current group you are in then go through this loop and increment group number one        
                       else:
                                groupNum = groupNum + 1
                                if (groupNum > 13): #if the group number is greater than 13, go to the castle
                                       compPos = board.index('Castle')
                                else:
                                        #change the position to the next G with the new group number
                                        compPos = board.index('G' + str(groupNum))
               #if the card is peppermint change the position to the peppermint position and change the group number to 4                              
               elif playerCard == 'Peppermint':
                       compPos = peppermintPos
                       groupNum = 4
                #if the card is peanut change the position to the peanut position and change the group number to 6 
               elif playerCard == 'Peanut':
                       compPos = peanutPos
                       groupNum = 6
                #if the card is lollipop change the position to the lollipop position and change the group number to 8 
               elif playerCard == 'Lollipop':
                       compPos = lolliPos
                       groupNum = 8
                #if the card is Ice Cream change the position to the Ice Cream position and change the group number to 11 
               elif playerCard == 'Ice Cream':
                       compPos = iceCreamPos
                       groupNum = 11
               #if the player lands on B1, they automatically go to B6 and the group number changes to 6
               if compPos == board.index('B1'):
                       compPos = board.index('B6')
                       groupNum = 6
                #if the player lands on G3, they automatically go to G4 and the group number changes to 4
               elif compPos == board.index('G3'):
                       compPos = board.index ('G4')
                       groupNum = 4
                #if the player lands on either of the licorice tiles, they lose a turn so increment the number of moves
               elif compPos == licoricePos1 or compPos == licoricePos2:
                       numMoves = numMoves + 1
                #if the position becomes castle, the game ends
               elif compPos == board.index('Castle'):
                       endGame = True
                #increment card index and number of moves each time it goes through the loop       
               cardIndex = cardIndex + 1
               numMoves = numMoves + 1
               
        return numMoves

#Main Code
#write data of the candy land project into a CSV file
#import csv and mean
def main():
        import csv
        from statistics import mean
        #create 2 empty lists to hold results data and the moves
        results = []
        allMoves = []
        #initialize min, max, and average variables
        minTurns = 0
        maxTurns = 0
        avgTurns = 0
        #write the new file
        file = open("PartAResults.csv", 'w', newline = '')    
        writer = csv.writer(file)
        #the headers in the csv file
        results.append(['Game', 'Number of Turns', ''])
        #play the game 1000 times and append the number of moves
        for i in range(1000):
                turns = play_game()
                allMoves.append(turns)
                results.append([str(i+1), str(turns), ''])
        #find the min, max, and mean using built in functions
        minTurns = min(allMoves)
        maxTurns = max(allMoves)
        avgTurns = mean(allMoves)         
        #print the found data
        print('Min: ', minTurns)
        print('Max: ', maxTurns)
        print('Average: ', avgTurns)
        #append minimum number to results
        results[0].append('Min')
        results[0].append(minTurns)
        #append maximum results
        results[1].append('Max')
        results[1].append(maxTurns)
        #append the average to thte results
        results[2].append('Average')
        results[2].append(avgTurns)
        #write results into the file
        writer.writerows(results)    
        file.close() #close the file
main()
