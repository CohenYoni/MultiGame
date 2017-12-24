import Question_Israel_earth
from Question_Israel_earth import *
from copy import deepcopy  # http://www.wellho.net/resources/ex.php4?item=y111/deepcop.py

######################## CHECKERS GAME ########################

'''
strategies: minimax, negascout, negamax, minimax w/ab cutoff
'''

######################## DIMENSIONS ########################
board_width = 600
board_height = 600
player_width = player_height = 60
king_width = 80
king_height = 75
panel_width = panel_height = 75

######################## IMAGES ########################

pygame.display.set_caption('Checkers')  # set title of the window
checkersIconImg = pygame.image.load('checkers_icon.png')
pygame.display.set_icon(checkersIconImg)
BoardGameImg = pygame.image.load('checkerboard.png') # load background
RivalImg = pygame.image.load('rival_screen.png') # load choose rival screen background
DifficultyImg = pygame.image.load('difficulty.png') # load choose difficulty screen background

blackPlayerImgs = {1: pygame.image.load('black_player.png'), 2: pygame.image.load('black_player.png'),
                   3: pygame.image.load('black_player.png'), 4: pygame.image.load('black_player.png'),
                   5: pygame.image.load('black_player.png'), 6: pygame.image.load('black_player.png'),
                   7: pygame.image.load('black_player.png'), 8: pygame.image.load('black_player.png'),
                   9: pygame.image.load('black_player.png'), 10: pygame.image.load('black_player.png'),
                   11: pygame.image.load('black_player.png'), 12: pygame.image.load('black_player.png')}
whitePlayerImgs = {1: pygame.image.load('white_player.png'), 2: pygame.image.load('white_player.png'),
                   3: pygame.image.load('white_player.png'), 4: pygame.image.load('white_player.png'),
                   5: pygame.image.load('white_player.png'), 6: pygame.image.load('white_player.png'),
                   7: pygame.image.load('white_player.png'), 8: pygame.image.load('white_player.png'),
                   9: pygame.image.load('white_player.png'), 10: pygame.image.load('white_player.png'),
                   11: pygame.image.load('white_player.png'), 12: pygame.image.load('white_player.png')}

######################## VARIABLES ########################
# odd row with even col, even row with odd col
col_center = {1: 5, 2: 5 + panel_width, 3: 5 + panel_width * 2, 4: 5 + panel_width * 3, 5: 5 + panel_width * 4,
              6: 5 + panel_width * 5, 7: 5 + panel_width * 6, 8: 5 + panel_width * 7}
row_center = {1: 5, 2: 5 + panel_height, 3: 5 + panel_height * 2, 4: 5 + panel_height * 3, 5: 5 + panel_height * 4,
              6: 5 + panel_height * 5, 7: 5 + panel_height * 6, 8: 5 + panel_height * 7}

turn = 'white'  # keep track of whose turn it is. white begins.
selected = (0, 0)  # a tuple keeping track of which piece is selected
move_limit = [150, 0]  # move limit for each game (declares game as draw otherwise)
empty_position = None

# artificial intelligence related
best_move = ()  # best move for the player as determined by strategy

# gui variables
board_size = 8  # board is 8x8 squares
left = 1  # left mouse button
fps = 20  # framerate of the scene (to save cpu time)
pause = 5  # number of seconds to pause the game for after end of game


######################## FUNCTIONS ########################

# create a new piece
def new_piece(color, serial_number, king=False):
    '''king variable- True if king, False otherwise'''
    return {'color': color, 'SN': serial_number, 'king': king}

# create a player. dispatch dictionary and message passing.
'''
API: 'type', 'color', 'strategy', 'ply_depth',  'update_questions', 'update_answers',  'get_questions', 'get_answers'
'''
def new_player(type, color, strategy, ply_depth):
    '''type- cpu or human, strategy- choice of strategy: minimax, negascout, negamax, minimax w/ab, ply_depth- ply depth for algorithms.'''

    questions = 0 # number of questions appears in the game
    correct_ans = 0 # number of correct answers

    # increace the number of quastions that appears
    def update_questions():
        nonlocal questions
        questions += 1
    # increace the number of correct answers if its true
    def update_answers(was_currect):
        nonlocal correct_ans
        if was_currect:
            correct_ans += 1

    def get_num_of_questions():
        return questions

    def get_num_of_corranswers():
        return correct_ans

    #dispatch dictionary.
    return {'type': type, 'color': color, 'strategy': strategy, 'ply_depth': ply_depth,
            'update_questions': update_questions, 'update_answers': update_answers,
            'get_questions': get_num_of_questions, 'get_answers': get_num_of_corranswers}

# will initialize board with all the pieces
def init_board():
    '''return initialized board'''
    global move_limit
    move_limit[1] = 0  # reset move limit

    board = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, -1, 0, -1, 0, -1, 0],
        [0, -1, 0, -1, 0, -1, 0, -1],
        [-1, 0, -1, 0, -1, 0, -1, 0]
    ]  # initial board setting

    SN_black = SN_white = 1
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (board[row][col] == 1):
                board[row][col] = new_piece('black', SN_black, False)# basic black piece
                SN_black += 1
            elif (board[row][col] == -1):
                board[row][col] = new_piece('white', SN_white, False)  # basic white piece
                SN_white += 1
            elif (board[row][col] == 0):
                board[row][col] = empty_position
    return board

def get_king(color):
    '''load king image'''
    if color == 'black':
        return pygame.image.load('king_black.png')
    elif color == 'white':
        return pygame.image.load('king_white.png')

def place_display(row, col, color, piece_id, king = False):
    '''place a piece image on the screen'''
    if color == 'black':
        if not king:
            gameDisplay.blit(blackPlayerImgs[piece_id], (col_center[col], row_center[row]))
        else:
            gameDisplay.blit(get_king('black'), (col_center[col]-8, row_center[row]-8))
    elif color == 'white':
        if not king:
            gameDisplay.blit(whitePlayerImgs[piece_id], (col_center[col], row_center[row]))
        else:
            gameDisplay.blit(get_king('white'), (col_center[col]-8, row_center[row]-8))

def update_display(board):
    '''change position on the screen from the matrix board'''
    gameDisplay.blit(BoardGameImg, (0, 0))
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != empty_position: #each panel contain a tuple (color, piece ID, king or player)
                place_display(row+1, col+1, board[row][col]['color'], board[row][col]['SN'], board[row][col]['king'])
                # row+1, col+1: place_display begins from 1 to boarde size, include.
    pygame.display.update()

# will return array with available moves to the player on board
def avail_moves(board, color):
    moves = []  # will store available jumps and moves
    there_is_jump = False
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != empty_position and board[row][col]['color'] == color:  # for all the players pieces...
                # ...check for jumps first
                if not board[row][col]['king']:
                    if can_jump([row, col], [row + 2, col + 2], board, [row + 1, col + 1]) == True: moves.append([row, col, row + 2, col + 2])
                    if can_jump([row, col], [row - 2, col + 2], board, [row - 1, col + 1]) == True: moves.append([row, col, row - 2, col + 2])
                    if can_jump([row, col], [row + 2, col - 2], board, [row + 1, col - 1]) == True: moves.append([row, col, row + 2, col - 2])
                    if can_jump([row, col], [row - 2, col - 2], board, [row - 1, col - 1]) == True: moves.append([row, col, row - 2, col - 2])
                else:
                    r, c = row + 1, col + 1 # move down right
                    while r < board_size and c < board_size:
                        if can_jump([row, col], [r, c], board) == True: moves.append([row, col, r, c])
                        r, c = r + 1, c + 1
                    r, c = row + 1, col - 1  # move down left
                    while r < board_size and c >= 0:
                        if can_jump([row, col], [r, c], board) == True: moves.append([row, col, r, c])
                        r, c = r + 1, c - 1
                    r, c = row - 1, col + 1  # move up right
                    while r >= 0 and c < board_size:
                        if can_jump([row, col], [r, c], board) == True: moves.append([row, col, r, c])
                        r, c = r - 1, c + 1
                    r, c = row - 1, col - 1  # move up left
                    while r >= 0 and c >= 0:
                        if can_jump([row, col], [r, c], board) == True: moves.append([row, col, r, c])
                        r, c = r - 1, c - 1
    if len(moves) > 0:
        there_is_jump = True
    if len(moves) == 0:  # if there are no jumps in the list (no jumps available)
    # ...check for regular moves
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != empty_position and board[row][col]['color'] == color:  # for all the players pieces...
                    if not board[row][col]['king']:
                        if can_move([row, col], [row + 1, col + 1], board) == True: moves.append([row, col, row + 1, col + 1])
                        if can_move([row, col], [row - 1, col + 1], board) == True: moves.append([row, col, row - 1, col + 1])
                        if can_move([row, col], [row + 1, col - 1], board) == True: moves.append([row, col, row + 1, col - 1])
                        if can_move([row, col], [row - 1, col - 1], board) == True: moves.append([row, col, row - 1, col - 1])
                    else:
                        r, c = row + 1, col + 1  # move down right
                        while r < board_size and c < board_size:
                            if can_move([row, col], [r, c], board) == True: moves.append([row, col, r, c])
                            r, c = r + 1, c + 1
                        r, c = row + 1, col - 1  # move down left
                        while r < board_size and c >= 0:
                            if can_move([row, col], [r, c], board) == True: moves.append([row, col, r, c])
                            r, c = r + 1, c - 1
                        r, c = row - 1, col + 1  # move up right
                        while r >= 0 and c < board_size:
                            if can_move([row, col], [r, c], board) == True: moves.append([row, col, r, c])
                            r, c = r - 1, c + 1
                        r, c = row - 1, col - 1  # move up left
                        while r >= 0 and c >= 0:
                            if can_move([row, col], [r, c], board) == True: moves.append([row, col, r, c])
                            r, c = r - 1, c - 1

    return moves, there_is_jump  # return the list with available jumps or moves

# will return true if the jump is legal
def can_jump(current_pos, new_pos, board, via_pos = None): #via_pos can be None, if the player is king
    '''check if the player can jump to the new position. position is a tuple (row, col)'''
    # is a piece at current position?
    if board[current_pos[0]][current_pos[1]] == empty_position: return False
    # is destination off board?
    if new_pos[0] < 0 or new_pos[0] >= board_size or new_pos[1] < 0 or new_pos[1] >= board_size: return False
    # does destination contain a piece already?
    if board[new_pos[0]][new_pos[1]] != empty_position: return False
    # are we jumping something?
    if via_pos != None and board[via_pos[0]][via_pos[1]] == empty_position: return False
    # are we jumping to same or next row or col?
    if abs(current_pos[0] - new_pos[0]) <= 1 or abs(current_pos[1] - new_pos[1]) <= 1: return False
    # for white piece
    if board[current_pos[0]][current_pos[1]]['color'] == 'white':
        if not (board[current_pos[0]][current_pos[1]]['king']) and new_pos[0] >= current_pos[0]: return False  # only move up
        if via_pos != None and board[via_pos[0]][via_pos[1]]['color'] != 'black': return False  # only jump blacks
    # for black piece
    if board[current_pos[0]][current_pos[1]]['color'] == 'black':
        if not (board[current_pos[0]][current_pos[1]]['king']) and new_pos[0] <= current_pos[0]: return False  # only move down
        if via_pos != None and board[via_pos[0]][via_pos[1]]['color'] != 'white': return False  # only jump whites
    # check king jump
    if board[current_pos[0]][current_pos[1]]['king'] == True:
        if new_pos[0] > current_pos[0] and new_pos[1] > current_pos[1]: # move down right
            row = current_pos[0] + 1
            col = current_pos[1] + 1
            count_pieces = 0
            while row < new_pos[0] and col < new_pos[1]:
                if board[row][col] != empty_position: # there is pieces on the slant
                    count_pieces += 1
                    if board[row][col]['color'] == board[current_pos[0]][current_pos[1]]['color']: return False # only jump different pieces
                    if count_pieces > 1: return False # can jump only one piece
                row += 1
                col += 1
            # is there piece to jump on the slant?
            if count_pieces == 0: return False
        elif new_pos[0] > current_pos[0] and new_pos[1] < current_pos[1]: # move down left
            row = current_pos[0] + 1
            col = current_pos[1] - 1
            count_pieces = 0
            while row < new_pos[0] and col > new_pos[1]:
                if board[row][col] != empty_position: # there is pieces on the slant
                    count_pieces += 1
                    if board[row][col]['color'] == board[current_pos[0]][current_pos[1]]['color']: return False # only jump different pieces
                    if count_pieces > 1: return False # can jump only one piece
                row += 1
                col -= 1
            # is there piece to jump on the slant?
            if count_pieces == 0: return False
        elif new_pos[0] < current_pos[0] and new_pos[1] > current_pos[1]: # move up right
            row = current_pos[0] - 1
            col = current_pos[1] + 1
            count_pieces = 0
            while row > new_pos[0] and col < new_pos[1]:
                if board[row][col] != empty_position: # there is pieces on the slant
                    count_pieces += 1
                    if board[row][col]['color'] == board[current_pos[0]][current_pos[1]]['color']: return False # only jump different pieces
                    if count_pieces > 1: return False # can jump only one piece
                row -= 1
                col += 1
            # is there piece to jump on the slant?
            if count_pieces == 0: return False
        elif new_pos[0] < current_pos[0] and new_pos[1] < current_pos[1]: # move up left
            row = current_pos[0] - 1
            col = current_pos[1] - 1
            count_pieces = 0
            while row > new_pos[0] and col > new_pos[1]:
                if board[row][col] != empty_position: # there is pieces on the slant
                    count_pieces += 1
                    if board[row][col]['color'] == board[current_pos[0]][current_pos[1]]['color']: return False # only jump different pieces
                    if count_pieces > 1: return False # can jump only one piece
                row -= 1
                col -= 1
            # is there piece to jump on the slant?
            if count_pieces == 0: return False
    return True  # jump is possible

# will return true if the move is legal
def can_move(current_pos, new_pos, board):
    # is a piece at current position?
    if board[current_pos[0]][current_pos[1]] == empty_position: return False
    # is destination off board?
    if new_pos[0] < 0 or new_pos[0] >= board_size or new_pos[1] < 0 or new_pos[1] >= board_size: return False
    # does destination contain a piece already?
    if board[new_pos[0]][new_pos[1]] != empty_position: return False
    # are we move the piece the next row or col?
    if not (board[current_pos[0]][current_pos[1]]['king']) and (abs(current_pos[0] - new_pos[0]) != 1 or abs(current_pos[1] - new_pos[1]) != 1): return False
    # are we move to different row and column?
    if current_pos[0] == new_pos[0] or current_pos[1] == new_pos[1]: return False
    # for white piece (not king)
    if not (board[current_pos[0]][current_pos[1]]['king']) and board[current_pos[0]][current_pos[1]]['color'] == 'white':
        if new_pos[0] >= current_pos[0]: return False  # only move up
    # for black piece
    if not (board[current_pos[0]][current_pos[1]]['king']) and board[current_pos[0]][current_pos[1]]['color'] == 'black':
        if new_pos[0] <= current_pos[0]: return False  # only move down
    # for kings
    if board[current_pos[0]][current_pos[1]]['king'] == True:
        if new_pos[0] > current_pos[0] and new_pos[1] > current_pos[1]: # move down right
            row = current_pos[0] + 1
            col = current_pos[1] + 1
            while row < new_pos[0] and col < new_pos[1]:
                if board[row][col] != empty_position: return False  # there is pieces on the slant
                row += 1
                col += 1
        elif new_pos[0] > current_pos[0] and new_pos[1] < current_pos[1]: # move down left
            row = current_pos[0] + 1
            col = current_pos[1] - 1
            while row < new_pos[0] and col > new_pos[1]:
                if board[row][col] != empty_position: return False  # there is pieces on the slant
                row += 1
                col -= 1
        elif new_pos[0] < current_pos[0] and new_pos[1] > current_pos[1]: # move up right
            row = current_pos[0] - 1
            col = current_pos[1] + 1
            while row > new_pos[0] and col < new_pos[1]:
                if board[row][col] != empty_position: return False  # there is pieces on the slant
                row -= 1
                col += 1
        elif new_pos[0] < current_pos[0] and new_pos[1] < current_pos[1]: # move up left
            row = current_pos[0] - 1
            col = current_pos[1] - 1
            while row > new_pos[0] and col > new_pos[1]:
                if board[row][col] != empty_position: return False  # there is pieces on the slant
                row -= 1
                col -= 1
    return True  # move is possible

# make a move on a board, assuming it's legit
def make_move(current_pos, new_pos, board):
    board[new_pos[0]][new_pos[1]] = board[current_pos[0]][current_pos[1]]  # make the move
    board[current_pos[0]][current_pos[1]] = empty_position  # delete the source

    # check if we made a king
    if new_pos[0] == 0 and board[new_pos[0]][new_pos[1]]['color'] == 'white': board[new_pos[0]][new_pos[1]]['king'] = True
    if new_pos[0] == (board_size-1) and board[new_pos[0]][new_pos[1]]['color'] == 'black': board[new_pos[0]][new_pos[1]]['king'] = True

    #delete the jumped piece, if king jump
    if (new_pos[0] - current_pos[0]) > 1 and (new_pos[1] - current_pos[1]) > 1:  # we made a jump down right
        row, col = current_pos[0] + 1, current_pos[1] + 1
        while row < new_pos[0] and col < new_pos[1]:
            board[row][col] = empty_position # delete the jumped piece
            row, col = row + 1, col + 1
    elif (new_pos[0] - current_pos[0]) > 1 and (new_pos[1] - current_pos[1]) < -1:  # we made a jump down left
        row, col = current_pos[0] + 1, current_pos[1] - 1
        while row < new_pos[0] and col > new_pos[1]:
            board[row][col] = empty_position  # delete the jumped piece
            row, col = row + 1, col - 1
    elif (new_pos[0] - current_pos[0]) < -1 and (new_pos[1] - current_pos[1]) > 1:  # we made a jump up right
        row, col = current_pos[0] - 1, current_pos[1] + 1
        while row > new_pos[0] and col < new_pos[1]:
            board[row][col] = empty_position  # delete the jumped piece
            row, col = row - 1, col + 1
    elif (new_pos[0] - current_pos[0]) < -1 and (new_pos[1] - current_pos[1]) < -1:  # we made a jump up left
        row, col = current_pos[0] - 1, current_pos[1] - 1
        while row > new_pos[0] and col > new_pos[1]:
            board[row][col] = empty_position  # delete the jumped piece
            row, col = row - 1, col - 1

    return board

# have we killed the opponent already?
def count_pieces(board):
    black, white = 0, 0  # keep track of score
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] != empty_position:
                if board[row][col]['color'] == 'black':
                    black += 1  # we see a black piece
                else:
                    white += 1  # we see a white piece

    return black, white

# end turn
def end_turn():
    global turn  # use global variables

    if turn != 'black':
        turn = 'black'
    else:
        turn = 'white'

# make changes to ply's if playing vs human (problem with scope)
# will check for errors in players settings
def player_check(player_black, player_white):

    if player_black['type'] == 'human' and player_white['type'] == 'cpu' or player_black['type'] == 'cpu' and \
                    player_white['type'] == 'cpu':
        player_black['type'] = 'cpu'
        player_white['type'] = 'human'

    if player_black['ply_depth'] < 0: player_black['ply_depth'] = 1
    if player_white['ply_depth'] < 0: player_white['ply_depth'] = 1

    if player_black['color'] != 'black': player_black['color'] = 'black'
    if player_white['color'] != 'white': player_white['color'] = 'white'

    if player_black['strategy'] != 'minimax' or player_black['strategy'] != 'negascout':
        if player_black['strategy'] != 'negamax' or player_black['strategy'] != 'alpha-beta':
            player_black['strategy'] = 'alpha-beta'
    if player_white['strategy'] != 'minimax' or player_white['strategy'] != 'negascout':
        if player_white['strategy'] != 'negamax' or player_white['strategy'] != 'alpha-beta':
            player_white['strategy'] = 'alpha-beta'

    # if human has higher ply_setting, cpu will do unnecessary calculations
    if player_black['type'] != 'cpu' and player_white['type'] == 'cpu':
        player_black['ply_depth'] = player_white['ply_depth']
    elif player_white['type'] != 'cpu' and player_black['type'] == 'cpu':
        player_white['ply_depth'] = player_black['ply_depth']

    return player_black, player_white

# initialize players and the boardfor the game
'''difficulty: hard, moderate, easy. strategy: alpha-beta, minimax, negascout, negamax.'''
def game_init(player1_type='cpu', player2_type='human', difficulty='easy', strategy='alpha-beta'):
    '''difficulty: hard, moderate, easy'''
    # hard difficulty
    if difficulty == 'hard':
        black = new_player(player1_type, 'black', strategy, 8)  # init black player
        white = new_player(player2_type, 'white', strategy, 8)  # init white player
    # moderate difficulty
    elif difficulty == 'moderate':
        black = new_player(player1_type, 'black', strategy, 4)  # init black player
        white = new_player(player2_type, 'white', strategy, 4)  # init white player
    # easy difficulty
    else:
        black = new_player(player1_type, 'black', strategy, 1)  # init black player
        white = new_player(player2_type, 'white', strategy, 1)  # init white player

    board = init_board()
    return board, black, white

######################## CORE FUNCTIONS ########################

# will evaluate board for a player
def evaluate(game, player):
    ''' this function just adds up the pieces on board (100 = piece, 175 = king) and returns the difference '''

    def simple_score(game, player):
        black, white = 0, 0  # keep track of score
        for row in range(board_size):
            for col in range(board_size):
                if (game[row][col] != empty_position and game[row][col]['color'] == 'black'):  # select black pieces on board
                    if not game[row][col]['king']:
                        black += 100  # 100pt for normal pieces
                    else:
                        black += 175  # 175pts for kings
                elif (game[row][col] != empty_position and game[row][col]['color'] == 'white'):  # select white pieces on board
                    if not game[row][col]['king']:
                        white += 100  # 100pt for normal pieces
                    else:
                        white += 175  # 175pts for kings
        if player != 'black':
            return white - black
        else:
            return black - white

    ''' this function will add bonus to pieces going to opposing side '''

    def piece_rank(game, player):
        black, white = 0, 0  # keep track of score
        for row in range(board_size):
            for col in range(board_size):
                if (game[row][col] != empty_position and game[row][col]['color'] == 'black'):  # select black pieces on board
                    if not game[row][col]['king']:  # not for kings
                        black = black + (row * row)
                elif (game[row][col] != empty_position and game[row][col]['color'] == 'white'):  # select white pieces on board
                    if not game[row][col]['king']:  # not for kings
                        white = white + ((7 - row) * (7 - row))
        if player != 'black':
            return white - black
        else:
            return black - white

    ''' a king on an edge could become trapped, thus deduce some points '''

    def edge_king(game, player):
        black, white = 0, 0  # keep track of score
        for row in range(board_size):
            if (game[row][0] != empty_position and game[row][0]['king'] == True):
                if game[row][0]['color'] != 'white':
                    black += -25
                else:
                    white += -25
            if (game[row][7] != empty_position and game[row][7]['king'] == True):
                if game[row][7]['color'] != 'white':
                    black += -25
                else:
                    white += -25
        if player != 'black':
            return white - black
        else:
            return black - white

    multi = random.uniform(0.97, 1.03)  # will add +/- 3 percent to the score to make things more unpredictable

    return (simple_score(game, player) + piece_rank(game, player) + edge_king(game, player)) * 1

# will generate possible moves and board states until a given depth
''' http://en.wikipedia.org/wiki/Minimax '''
''' function minimax(node, depth) '''
def minimax(board, player_color, ply, player_black, player_white):
    global best_move

    # find out ply depth for player
    ply_depth = 0
    if player_color != 'black':
        ply_depth = player_white['ply_depth']
    else:
        ply_depth = player_black['ply_depth']

    end = count_pieces(board)

    ''' if node is a terminal node or depth = CutoffDepth '''
    if ply >= ply_depth or end[0] == 0 or end[1] == 0:  # are we still playing?
        ''' return the heuristic value of node '''
        score = evaluate(board, player_color)  # return evaluation of board as we have reached final ply or end state
        return score

    ''' if the adversary is to play at node '''
    if player_color != turn:  # if the opponent is to play on this node...

        ''' let beta := +infinity '''
        beta = +10000

        ''' foreach child of node '''
        moves, irrelevant = avail_moves(board, player_color)  # get the available moves for player
        for i in range(len(moves)):
            # create a deep copy of the board (otherwise pieces would be just references)
            new_board = deepcopy(board)
            new_board = make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)  # make move on new board

            ''' beta := min(beta, minimax(child, depth+1)) '''
            # ...make a switch of players for minimax...
            if player_color == 'black':
                player_color = 'white'
            else:
                player_color = 'black'

            temp_beta = minimax(new_board, player_color, ply + 1, player_black, player_white)
            if temp_beta < beta:
                beta = temp_beta  # take the lowest beta

        ''' return beta '''
        return beta

    else:  # else we are to play
        ''' else {we are to play at node} '''
        ''' let alpha := -infinity '''
        alpha = -10000

        ''' foreach child of node '''
        moves, irrelevant = avail_moves(board, player_color)  # get the available moves for player
        for i in range(len(moves)):
            # create a deep copy of the board (otherwise pieces would be just references)
            new_board = deepcopy(board)
            new_board = make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)  # make move on new board

            ''' alpha := max(alpha, minimax(child, depth+1)) '''
            # ...make a switch of players for minimax...
            if player_color == 'black':
                player_color = 'white'
            else:
                player_color = 'black'

            temp_alpha = minimax(new_board, player_color, ply + 1, player_black, player_white)
            if temp_alpha > alpha:
                alpha = temp_alpha  # take the highest alpha
                if ply == 0: best_move = (moves[i][0], moves[i][1]), (moves[i][2], moves[i][3])  # save the move as it's our turn

        ''' return alpha '''
        return alpha

''' http://en.wikipedia.org/wiki/Negascout '''
''' function negascout(node, depth, alpha, beta) '''
def negascout(board, ply, alpha, beta, player_color, player_black, player_white):
    global best_move

    # find out ply depth for player
    ply_depth = 0
    if player_color != 'black':
        ply_depth = player_white['ply_depth']
    else:
        ply_depth = player_black['ply_depth']

    end = count_pieces(board)

    ''' if node is a terminal node or depth = 0 '''
    if ply >= ply_depth or end[0] == 0 or end[1] == 0:  # are we still playing?
        ''' return the heuristic value of node '''
        score = evaluate(board, player_color)  # return evaluation of board as we have reached final ply or end state
        return score
    ''' b := beta '''
    b = beta

    ''' foreach child of node '''
    moves, irrelevant = avail_moves(board, player_color)  # get the available moves for player
    for i in range(len(moves)):
        # create a deep copy of the board (otherwise pieces would be just references)
        new_board = deepcopy(board)
        new_board = make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)  # make move on new board

        ''' alpha := -negascout (child, depth-1, -b, -alpha) '''
        # ...make a switch of players
        if player_color == 'black':
            player_color = 'white'
        else:
            player_color = 'black'

        alpha = -negascout(new_board, ply + 1, -b, -alpha, player_color, player_black, player_white)
        ''' if alpha >= beta '''
        if alpha >= beta:
            ''' return alpha '''
            return alpha  # beta cut-off
        ''' if alpha >= b '''
        if alpha >= b:  # check if null-window failed high

            ''' alpha := -negascout(child, depth-1, -beta, -alpha) '''
            # ...make a switch of players
            if player_color == 'black':
                player_color = 'white'
            else:
                player_color = 'black'

            alpha = -negascout(new_board, ply + 1, -beta, -alpha, player_color, player_black, player_white)  # full re-search
            ''' if alpha >= beta '''
            if alpha >= beta:
                ''' return alpha '''
                return alpha  # beta cut-off
        ''' b := alpha+1 '''
        b = alpha + 1  # set new null window
    ''' return alpha '''
    if ply == 0: best_move = (moves[i][0], moves[i][1]), (moves[i][2], moves[i][3])  # save the move
    return alpha

''' http://en.wikipedia.org/wiki/Negamax '''
''' function negamax(node, depth, alpha, beta) '''
def negamax(board, ply, alpha, beta, player_color, player_black, player_white):
    global best_move

    # find out ply depth for player
    ply_depth = 0
    if player_color != 'black':
        ply_depth = player_white['ply_depth']
    else:
        ply_depth = player_black['ply_depth']

    end = count_pieces(board)

    ''' if node is a terminal node or depth = 0 '''
    if ply >= ply_depth or end[0] == 0 or end[1] == 0:  # are we still playing?
        ''' return the heuristic value of node '''
        score = evaluate(board, player_color)  # return evaluation of board as we have reached final ply or end state
        return score

    ''' else '''
    ''' foreach child of node '''
    moves, irrelevant = avail_moves(board, player_color)  # get the available moves for player
    for i in range(len(moves)):
        # create a deep copy of the board (otherwise pieces would be just references)
        new_board = deepcopy(board)
        new_board = make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)  # make move on new board

        ''' alpha := max(alpha, -negamax(child, depth-1, -beta, -alpha)) '''
        # ...make a switch of players
        if player_color == 'black':
            player_color = 'white'
        else:
            player_color = 'black'

        temp_alpha = -negamax(new_board, ply + 1, -beta, -alpha, player_color, player_black, player_white)
        if temp_alpha >= alpha:
            if ply == 0: best_move = (moves[i][0], moves[i][1]), (moves[i][2], moves[i][3])  # save the move
            alpha = temp_alpha

        ''' {the following if statement constitutes alpha-beta pruning} '''
        ''' if alpha>=beta '''
        if alpha >= beta:
            ''' return beta '''
            if ply == 0: best_move = (moves[i][0], moves[i][1]), (moves[i][2], moves[i][3])  # save the move
            return beta
    ''' return alpha '''
    return alpha

''' http://www.ocf.berkeley.edu/~yosenl/extras/alphabeta/alphabeta.html '''
''' alpha-beta(player,board,alpha,beta) '''
def alpha_beta(player_color, board, ply, alpha, beta, player_black, player_white):
    global best_move

    # find out ply depth for player
    ply_depth = 0
    if player_color != 'black':
        ply_depth = player_white['ply_depth']
    else:
        ply_depth = player_black['ply_depth']

    end = count_pieces(board)

    ''' if(game over in current board position) '''
    if ply >= ply_depth or end[0] == 0 or end[1] == 0:  # are we still playing?
        ''' return winner '''
        score = evaluate(board, player_color)  # return evaluation of board as we have reached final ply or end state
        return score

    ''' children = all legal moves for player from this board '''
    moves, irrelevant = avail_moves(board, player_color)  # get the available moves for player

    ''' if(max's turn) '''
    if player_color == turn:  # if we are to play on node...
        ''' for each child '''
        for i in range(len(moves)):
            # create a deep copy of the board (otherwise pieces would be just references)
            new_board = deepcopy(board)
            new_board = make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)  # make move on new board

            ''' score = alpha-beta(other player,child,alpha,beta) '''
            # ...make a switch of players for minimax...
            if player_color == 'black':
                player_color = 'white'
            else:
                player_color = 'black'

            score = alpha_beta(player_color, new_board, ply + 1, alpha, beta, player_black, player_white)

            ''' if score > alpha then alpha = score (we have found a better best move) '''
            if score > alpha:
                if ply == 0: best_move = (moves[i][0], moves[i][1]), (moves[i][2], moves[i][3])  # save the move
                alpha = score
            ''' if alpha >= beta then return alpha (cut off) '''
            if alpha >= beta:
                # if ply == 0: best_move = (moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]) # save the move
                return alpha

        ''' return alpha (this is our best move) '''
        return alpha

    else:  # the opponent is to play on this node...
        ''' else (min's turn) '''
        ''' for each child '''
        for i in range(len(moves)):
            # create a deep copy of the board (otherwise pieces would be just references)
            new_board = deepcopy(board)
            new_board = make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)  # make move on new board

            ''' score = alpha-beta(other player,child,alpha,beta) '''
            # ...make a switch of players for minimax...
            if player_color == 'black':
                player_color = 'white'
            else:
                player_color = 'black'

            score = alpha_beta(player_color, new_board, ply + 1, alpha, beta, player_black, player_white)

            ''' if score < beta then beta = score (opponent has found a better worse move) '''
            if score < beta: beta = score
            ''' if alpha >= beta then return beta (cut off) '''
            if alpha >= beta: return beta
        ''' return beta (this is the opponent's best move) '''
        return beta

# play as a computer
def cpu_play(player, board, player_white, player_black):
    global move_limit  # global variable

    # find and print the best move for cpu
    if player['strategy'] == 'minimax':
        alpha = minimax(board, player['color'], 0, player_black, player_white)
    elif player['strategy'] == 'negascout':
        alpha = negascout(board, 0, -10000, +10000, player['color'], player_black, player_white)
    elif player['strategy'] == 'negamax':
        alpha = negamax(board, 0, -10000, +10000, player['color'], player_black, player_white)
    elif player['strategy'] == 'alpha-beta':
        alpha = alpha_beta(player['color'], board, 0, -10000, +10000, player_black, player_white)

    #if alpha == -10000:  # no more moves available... all is lost
        #if player['color'] == 'white':
            #black won
        #else:
            #white won

    board = make_move(best_move[0], best_move[1], board)  # make the move on board
    move_limit[1] += 1  # add to move limit
    end_turn()  # end turn
    return board

######################## GUI FUNCTIONS ########################

# function displaying position of clicked square
def mouse_click(pos, board, playerBlack, player_White):
    global selected, move_limit  # use global variables
    was_jump = False
    jumped = False
    if 0 < pos[0] < board_width and 0 < pos[1] < board_height:
        # only go ahead if we can actually play :)
        if (turn == 'white' and player_White['type'] != 'cpu') or (turn == 'black' and playerBlack['type'] != 'cpu'):
            col = pos[0] // panel_width
            row = pos[1] // panel_height

            if board[row][col] != empty_position and board[row][col]['color'] == turn:
                selected = row, col  # 'select' a piece
            else:
                moves, was_jump = avail_moves(board, turn)  # get available moves for that player
                for i in range(len(moves)):
                    if selected[0] == moves[i][0] and selected[1] == moves[i][1]:
                        if row == moves[i][2] and col == moves[i][3]:
                            board = make_move(selected, (row, col), board)  # make the move
                            if was_jump:
                                jumped = True
                            move_limit[1] += 1  # add to move limit
                            end_turn()  # end turn
    return jumped

######################## START OF GAME ########################

def checkers_loop(level_quastion = 1, playerBlack_type = 'cpu', playerWhite_type = 'human', level_game = 'easy', strategy = 'alpha-beta', back = None):
    board, player_black, player_white = game_init(playerBlack_type, playerWhite_type, level_game, strategy)
    player_black, player_white = player_check(player_black, player_white)  # will check for errors in player settings
    gameDisplay.fill(colors['white'])
    gameDisplay.blit(BoardGameImg, (0, 0))
    update_display(board)
    pygame.display.update()
    gameExit = False
    while not gameExit: # main game loop
        for event in pygame.event.get(): # the event loop
            if event.type == pygame.QUIT: # quit game
                gameExit = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == left:
                if 0 < event.pos[0] < board_width and 0 <  event.pos[1] < board_height: #if the click is in the game-board
                    was_jump = mouse_click(event.pos, board, player_black, player_white)  # mouse click
                    update_display(board)
                    if was_jump:
                        was_correct = question_Israel_earth(level_quastion)
                        time.sleep(2)
                        update_display(board)
                        if turn != 'white' and player_white['type'] == 'human':
                            player_white['update_questions']()
                            player_white['update_answers'](was_correct)
                        if turn != 'black' and player_black['type'] == 'human':
                            player_black['update_questions']()
                            player_black['update_answers'](was_correct)

        button("Back", 620, 430, 125, 60, colors['gray_l'], colors['gray'], back)
        button("Exit", 620, 520, 125, 60, colors['gray_l'], colors['gray'], QuitTheGame)
        if player_black['type'] == 'human':
            text("Black: {0}/{1}".format(player_black['get_questions'](), player_black['get_answers']()), 620, 200)
        text("White: {0}/{1}".format(player_white['get_answers'](), player_white['get_questions']()), 620, 240)

                        # let user know what's happening (whose turn it is)
        if (turn == 'white' and player_white['type'] == 'human'):
            text('WHITE TURN', display_width - 180, display_height - 500)
            pygame.display.update()
        elif (turn == 'black' and player_black['type'] == 'human'):
            text('BLACK TURN', display_width - 180, display_height - 500)
        else:
            text('CPU THINKING...', display_width - 200, display_height - 500)

        # check state of game
        end = count_pieces(board)
        if end[1] == 0:
            if player_black['type'] == 'human':
                message_display("Black you win!")
            else:
                message_display("Computer won...")
            gameExit = True
        elif end[0] == 0:
            message_display("White you win!")
            gameExit = True
        elif move_limit[0] == move_limit[1]: # check if we breached the threshold for number of moves
            message_display("Draw")
            gameExit = True
        else:
            pygame.display.flip()  # display scene from buffer

        # cpu play
        if turn == 'white' and player_white['type'] == 'cpu':
            board = cpu_play(player_white, board, player_white, player_black)  # white cpu turn
            time.sleep(1.5)
            update_display(board)
        elif turn == 'black' and player_black['type'] == 'cpu':
            board = cpu_play(player_black, board, player_white, player_black)  # black cpu turn
            time.sleep(1.5)
            update_display(board)


        clock.tick(fps)  # saves cpu time

    if player_black['type'] == 'cpu':
        return level_quastion, player_white['get_questions'], None, player_white['get_answers'], None
    else:
        return level_quastion, player_white['get_questions'](), player_black['get_questions'](), player_white['get_answers'](), player_black['get_answers']()


def difficulty_cpu(level_quastion = 1, back = None):
    white_quastions = black_quastions = white_ans = black_ans = 0  # as start
    gameDisplay.fill(colors['white'])
    strategies = ['minimax', 'negascout', 'negamax', 'alpha-beta']
    strategy_chosen = random.randrange(0, len(strategies)) # different strategy each game
    loopExit = False
    while not loopExit:
        for event in pygame.event.get(): # the event loop
            if event.type == pygame.QUIT: # quit game
                loopExit = True
        gameDisplay.blit(DifficultyImg, (0, 0))

        if 1 == button_2("Easy", 150, 330, 100, 60, colors['gray_l'], colors['gray'], '1'):
            level_quastion, white_quastions, black_quastions, white_ans, black_ans = checkers_loop(level_quastion, 'cpu', 'human', 'easy', strategies[strategy_chosen], back)
            loopExit = True
        if 2 == button_2("Moderate", 350, 330, 100, 60, colors['gray_l'], colors['gray'], '2'):
            level_quastion, white_quastions, black_quastions, white_ans, black_ans = checkers_loop(level_quastion, 'cpu', 'human', "moderate", strategies[strategy_chosen], back)
            loopExit = True
        if 3 == button_2("Hard", 550, 330, 100, 60, colors['gray_l'], colors['gray'], '3'):
            level_quastion, white_quastions, black_quastions, white_ans, black_ans = checkers_loop(level_quastion, 'cpu', 'human', "hard", strategies[strategy_chosen], back)
            loopExit = True
        pygame.display.update()
        clock.tick(fps)

    return level_quastion, white_quastions, black_quastions, white_ans, black_ans


def rival(level_quastion = 1, back = None):
    white_quastions = black_quastions = white_ans = black_ans = 0 # as start
    gameDisplay.fill(colors['white'])
    loopExit = False
    while not loopExit:
        for event in pygame.event.get(): # the event loop
            if event.type == pygame.QUIT: # quit game
                loopExit = True
        gameDisplay.blit(RivalImg, (0, 0))


        if 1 == button_2("Player vs Computer", 100, 430, 200, 60, colors['gray_l'], colors['gray'], '1'):
            level_quastion, white_quastions, black_quastions, white_ans, black_ans = difficulty_cpu(level_quastion, back)
            loopExit = True
        if 2 == button_2("Player vs Player", 500, 430, 200, 60, colors['gray_l'], colors['gray'], '2'):
            level_quastion, white_quastions, black_quastions, white_ans, black_ans = checkers_loop(level_quastion, 'human', 'human', 'easy', 'mimimax', back)
            loopExit = True

        pygame.display.update()
        clock.tick(fps)

    return level_quastion, white_quastions, black_quastions, white_ans, black_ans


rival()
pygame.quit()
quit()
