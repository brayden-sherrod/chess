# A basic chess playing game using the command line for movements and shwowing the board with pygame
# Authors: Perry Jamail, Vince Palombi, and Brayden Sherrod
# Date: Started June 2, 2023

from chessboard import display

def print_instructions():
    print("These are the instructions we will set on how to enter move commands")
    print("\nType 'run' to start the game.\n")

def start_game(): # Handle starting game procedures
    game_board = display.start()
    return game_board

def end_game(): # Handle closing out game procedures
    print("Thanks for playing.")
    display.terminate()

########################################################################################
# BASIC COMMANDS FOR THE CHESS BOARD DISPLAY
# valid_fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'

# FEN is a format of representing a chess board which I need to learn too
# Here is some documentaion on it: https://www.chess.com/terms/fen-chess

# # Checking GUI window for QUIT event. (Esc or GUI CANCEL)
# display.check_for_quit()

# # Position change/update
# display.update(valid_fen, game_board)

# # Close window
# display.terminate()

##########################################################################################


# Main function where all other functions will run from
def main():
    print("\n\nWelcome to chess!")
    print("To play the game each player will take turns typing in their moves when prompted and the board will be displayed throughout.")
    print_instructions()
    game_running = True
    while game_running:
        command = input("> ")
        if command.lower() == 'run':
            board = start_game()
        elif command.lower() == 'exit':
            end_game()
            game_running = False

main()