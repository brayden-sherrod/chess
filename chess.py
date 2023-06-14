# A basic chess playing game using the command line for movements and shwowing the board with pygame
# Authors: Perry Jamail, Vince Palombi, and Brayden Sherrod
# Date: Started June 2, 2023

from chessboard import display

def print_instructions():
    print("These are the instructions we will set on how to enter move commands")
    print("\nType 'run' to start the game.\n")

def start_game(): # Handle starting game procedures
    board_display = display.start()
    board_dict = {'a8': 'r', 'b8': 'n', 'c8': 'b', 'd8': 'q', 'e8': 'k', 'f8': 'b', 'g8': 'n', 'h8': 'r', # Initalize the board in a dictionary format with the same lettering
                  'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p', # scheme as the FEN to be used in with the display
                  'a6': '',  'b6': '',  'c6': '',  'd6': '',  'e6': '',  'f6': '',  'g6': '',  'h6': '',  # Where black pieces are represented with a lowercase letter
                  'a5': '',  'b5': '',  'c5': '',  'd5': '',  'e5': '',  'f5': '',  'g5': '',  'h5': '',  # and white pieces are represented with an uppercase letter
                  'a4': '',  'b4': '',  'c4': '',  'd4': '',  'e4': '',  'f4': '',  'g4': '',  'h4': '',  # K,k is for king and N,n is for knight
                  'a3': '',  'b3': '',  'c3': '',  'd3': '',  'e3': '',  'f3': '',  'g3': '',  'h3': '',  
                  'a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
                  'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': 'K', 'f1': 'B', 'g1': 'N', 'h1': 'R',}
    return (board_display, board_dict)

def end_game(): # Handle closing out game procedures
    print("Thanks for playing.")
    display.terminate()

def empty(board_dict, current_pos):
    print("Is board empty or not")
    if board_dict.get(current_pos) == '':
        return True
    else:
        return False

def check_pawn(board_dict, current_pos, to_pos, color):
    """
    Check if the propsed move is legal and possible (no pieces in the way, can move that way, etc.)
    if the move is possible return True, if not return False
    """
    return True

def check_rook(board_dict, current_pos, to_pos, color):
    """
    Check if the propsed move is legal and possible (no pieces in the way, can move that way, etc.)
    if the move is possible return True, if not return False
    """
    return True

def check_bishop(board_dict, current_pos, to_pos, color):
    """
    Check if the propsed move is legal and possible (no pieces in the way, can move that way, etc.)
    if the move is possible return True, if not return False
    """
    return True

def check_knight(board_dict, current_pos, to_pos, color):
    """
    Check if the propsed move is legal and possible (no pieces in the way, can move that way, etc.)
    if the move is possible return True, if not return False
    """
    return True

def check_queen(board_dict, current_pos, to_pos, color):
    """
    Check if the propsed move is legal and possible (no pieces in the way, can move that way, etc.)
    if the move is possible return True, if not return False
    """
    return True

def check_king(board_dict, current_pos, to_pos, color):
    """
    Check if the propsed move is legal and possible (no pieces in the way, can move that way, etc.)
    if the move is possible return True, if not return False
    """
    return True

def check_move(board_dict, current_pos, to_pos):
    """
    Call piece function depending on the piece at current pos (shown and to be defined above^^^)
    Return the result of the check piece function either True or False
    """
    move_possible = False
    piece = board_dict.get(current_pos)
    if piece.isupper():
        color = 'w'
    else:
        color = 'b'

    piece_lower = piece.lower()
    if piece_lower == "p":
        move_possible = check_pawn(board_dict, current_pos, to_pos, color)
    elif piece_lower == "r":
        move_possible = check_rook(board_dict, current_pos, to_pos, color)
    elif piece_lower == "b":
        move_possible = check_bishop(board_dict, current_pos, to_pos, color)
    elif piece_lower == "n":
        move_possible = check_knight(board_dict, current_pos, to_pos, color)
    elif piece_lower == "q":
        move_possible = check_queen(board_dict, current_pos, to_pos, color)
    elif piece_lower == "k":
        move_possible = check_king(board_dict, current_pos, to_pos, color)
    return move_possible
    
def execute_move(board_dict, current_pos, to_pos):
    """
    Change the dictionary to match the move made
    return the board_dict
    """

def convert_to_fen(board_dict):
    """
    Convert the dictionary to FEN string and return the string"""
    print("Here the dictionary is converted to the fen string for the display")

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
            board_display, board_dict = start_game()
            continue
        elif command.lower() == 'exit' or command.lower() == 'quit':
            end_game()
            game_running = False
            continue
        
        command_list = command.split()
        if len(command_list) == 0:
            continue
        else:
            action = command_list[0]
            if action == 'move':
                if len(command_list) < 3:
                    print("There is not enough information given to make a move.")
                    print("To move a piece enter the command 'move' 'current postion' 'position to move to'")
                    print("An example of the move command is 'move e2 e4' which moves the white e pawn up two spaces.")
                else:
                    current_pos = command_list[1]
                    to_pos = command_list[2]
                    if empty(board_dict, current_pos):
                        print("There is no piece at position:", current_pos, "\nPlease try again.")
                    else:
                        can_move = check_move(board_dict, current_pos, to_pos)
                        if can_move:
                            board_dict = execute_move(board_dict, current_pos, to_pos)
                            board_FEN = convert_to_fen(board_dict)
                            display.update(board_FEN, board_display)
                        else:
                            print("That move is not possible.")  # Ideally we will have more in depth messages in the indivudal functions explaining why the move isn't possible
                        

main()