import random, simplegui, math

secret_number, remaining_guesses, num_range = 0, 0, 0

def print_remaining_guesses(msg):
    print '\n', msg
    print 'Number of remaining guesses is', remaining_guesses

def new_game_with_range(new_num_range):
    global num_range
    num_range = new_num_range
    new_game()

def new_game():
    global secret_number, remaining_guesses
    secret_number = random.randrange(0, num_range)
    remaining_guesses = int(math.ceil(math.log(num_range, 2)))
    print_remaining_guesses('New game. Range is from 0 to ' + str(num_range))
    
def range100(): new_game_with_range(100)
def range1000(): new_game_with_range(1000)
    
def input_guess(guess):
    global remaining_guesses
    remaining_guesses -= 1
    guess_int = int(guess)    
    print_remaining_guesses('Guess was '+ guess)
    
    if guess_int == secret_number:
        print 'Correct!'
        new_game()
    elif remaining_guesses <= 0:
        print 'You ran out of guesses. The number was', secret_number
        new_game()
    elif guess_int > secret_number:
        print 'Lower!'
    else:
        print 'Higher!'
        
frame = simplegui.create_frame("Guess",200,200)
frame.add_button('Range: 0 - 100', range100)
frame.add_button('Range: 0 - 1000', range1000)
frame.add_input('Enter a guess', input_guess, 100)

range100()

frame.start()