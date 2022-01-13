#run at https://py2.codeskulptor.org/#user48_GPUnx2m14P_3.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_number = 0
num_range = 100
number_of_guesses = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    global number_of_guesses
    
    if num_range == 100:
        number_of_guesses = 7
    else:
        number_of_guesses = 10
        
    secret_number = random.randrange(0, num_range) 
    
    print "New game! Range is from 0 to", num_range,"\nYou have", number_of_guesses,"attempts to guess the number!"
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    print ""
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range 
    num_range = 1000
    print ""
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global number_of_guesses
    player_guess = int(guess)   
    
    if player_guess < secret_number:
        print "\nGuess was", player_guess,"\nHigher!"
    elif player_guess > secret_number:
        print "\nGuess was", player_guess,"\nLower!"
    else:
        print "\nGuess was", player_guess,"\nCorrect! \n"
        new_game()
        return
    
    number_of_guesses -= 1
        
    if number_of_guesses == 0:
        print "Game over! The attempts are over\n"
        new_game()
        return
    
    print "Number of remaining guesses is", number_of_guesses
    
# create frame
f = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is (0, 100]", range100, 200)
f.add_button("Range is (0, 1000]", range1000, 200)
f.add_input("Your Guess", input_guess, 200)

# call new_game 
new_game()
f.start()

# always remember to check your completed program against the grading rubric
