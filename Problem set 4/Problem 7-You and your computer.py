# Now that your computer can choose a word, you need to give the computer the
# option to play. Write the code that re-implements the playGame function. You
# will modify the function to behave as described below in the function's
# comments. As before, you should use the HAND_SIZE constant to determine the
# number of cards in a hand. Be sure to try out different values for HAND_SIZE
# with your program.

def playGame(wordList):
	"""
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.
    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.
    4) After the computer or user has played the hand, repeat from step 1
    wordList: list (string)
    """

    while True:
        x = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if x == 'e':
            break
        elif x == 'n':
            while True:
                z = str(input('Enter u to have yourself play, c to have the computer play: '))
                if z == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif z == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')            
	elif x == 'r':
      	try:
                hand
                z = str(input('Enter u to have yourself play, c to have the computer play: '))
                if z == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif z == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print('Invalid command.')
            except:
                print('You have not played a hand yet. Please play a new hand first!')
       else:
       	print('Invalid command.')


