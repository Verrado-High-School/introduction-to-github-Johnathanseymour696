#Johnathan
#Rock paper scissors gamw

# break into pieces
# Welcome page, with , name entry
# Score screen with computer, players (name) , ties
# Option for game r,q,p,s
#Game will loop until q is entered
#each loop it will get a random choice from the computer
# a choice from the player, compare the two , and update the score.
#When the game is over (q is entered ) final score is displayed

#WELCOME PAGE
#prompt for the player name
# a welcome message 

#____________________________________________________________________________________________________

# import
import random
# variables
playerScore = 0
computerScore = 0
ties = 0
# make a list
cChoices =["r","p","s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name")
#main loop
while True:
	#print score
    print("Score:")
    print("Computer:" + str(computerScore))
    print(name + ":" + str(playerScore))
    print("ties:" + str(ties))
    choice = input("Enter 'r' for rock, 'p' for paper, and 's' for scissors or 'q' to quit")
    computerChoice = random.choice(cChoices)
    print(computerChoice)
    if choice == "q":
    	break
    
    if choice == "r":
    	print(name + "Picked Rock")
    	if computerChoice=="r": # Tie
            print("Computer picked Rock")
            print("This is a tie ")
            ties = ties + 1
    		
    	elif computerChoice == "p":
    		print("Computer picked Paper")
    		print("Paper beats Rock")
    		computerScore += 1
    		
    	else:# s is the only choice left
    		 print("Computer picked Scissors")
    		 print("Rock beats scissors")
    		 playerScore += 1

    elif choice == "p":
    	print(name + "Picked Paper")
    	if computerChoice== "p":
    		print("Computer picked Paper")
    		print("This is a Tie")
    		ties = ties + 1

    	elif computerchoice == "r":
    		print("Computer picked Rock")
    		print("Paper beats Rock")
    		playerScore += 1
    	else:
    		print("Computer picked Scissors")
    		print("Scissors beat paper.")
    		computerScore +=1

    elif choice == "s":
    	print(name + "Picked Scissors")
    	if computerChoice=="s":
    		print("Computer picked scissors ")
    		print("This is a tie")
    		ties = ties + 1

    	elif computerChoice == "r":
    		print("Computer picked rock ")
    		print("Scissors beat rock")
    		computerScore +=1

    	else:
    		print("Computer picked paper")
    		print("Scissors beat paper")
    		playerScore +=1
    else: #print type something else
        print("This is not an correct input.")
