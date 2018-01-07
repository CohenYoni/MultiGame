import unittest
import checkers
import laddersandsnakes
import tools
import pygame

# unit test for checkers
class TestChecker(unittest.TestCase):

    def test_new_piece(self):
        # check if creat new pieces
        print ('get new piece now testing in checkers...')
        self.assertEquals(checkers.new_piece('black', 3, False), {'color': 'black', 'SN': 3, 'king': False}, 'simple piece not created correctly')
        self.assertEquals(checkers.new_piece('white', 2, True), {'color': 'white', 'SN': 2, 'king': True}, 'king piece not created correctly')

    def test_new_player(self):
        # check if arguments 'answers' and 'questions' are rest
        print('get new player now testing in checkers...')
        player = checkers.new_player('human','white','nagamax', 0)
        self.assertEqual(player['get_questions'](), 0, 'questions is not reseted to zero in checkers')
        self.assertEqual(player['get_answers'](), 0, 'answers is not reseted to zero in checkers')

    def test_init_board(self):
        # checks whether the board is properly formatted
        print('initial board now testing in checkers...')
        board = [
            [None, {'color':'black', 'SN':1, 'king':False}, None, {'color':'black', 'SN':2, 'king':False}, None, {'color':'black', 'SN':3, 'king':False}, None, {'color':'black', 'SN':4, 'king':False}],
            [{'color':'black', 'SN':5, 'king':False}, None, {'color':'black', 'SN':6, 'king':False}, None, {'color':'black', 'SN':7, 'king':False}, None, {'color':'black', 'SN':8, 'king':False}, None],
            [None, {'color':'black', 'SN':9, 'king':False}, None, {'color':'black', 'SN':10, 'king':False}, None, {'color':'black', 'SN':11, 'king':False}, None, {'color':'black', 'SN':12, 'king':False}],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [{'color':'white', 'SN':1, 'king':False}, None, {'color':'white', 'SN':2, 'king':False}, None, {'color':'white', 'SN':3, 'king':False}, None, {'color':'white', 'SN':4, 'king':False}, None],
            [None, {'color':'white', 'SN':5, 'king':False}, None, {'color':'white', 'SN':6, 'king':False}, None, {'color':'white', 'SN':7, 'king':False}, None, {'color':'white', 'SN':8, 'king':False}],
            [{'color':'white', 'SN':9, 'king':False}, None, {'color':'white', 'SN':10, 'king':False}, None, {'color':'white', 'SN':11, 'king':False}, None, {'color':'white', 'SN':12, 'king':False}, None]
        ]
        self.assertEquals(checkers.init_board(), board, 'board not initialized correctly')

    def test_avail_moves(self):
        # checks if get available move's
        print('available move now testing in checkers...')
        # check all the jump moves
        board = [
            [None, {'color': 'black', 'SN': 1, 'king': False}, None, None, None, None, None, {'color': 'white', 'SN': 3, 'king': True}],
            [None, None, {'color': 'white', 'SN': 2, 'king': False}, None, None, None, None, None],
            [None, None, None, None, None, {'color': 'black', 'SN': 4, 'king': False}, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, {'color': 'black', 'SN': 7, 'king': False}, None, None, None, {'color': 'white', 'SN': 6, 'king': True}, None, None],
            [{'color': 'white', 'SN': 8, 'king': False}, None, None, None, None, None, {'color': 'black', 'SN': 5, 'king': True}, None],
        ]
        avail_black = checkers.avail_moves(board, "black")
        avail_white = checkers.avail_moves(board, "white")
        self.assertEqual(avail_black, ([[0, 1, 2, 3], [7, 6, 5, 4], [7, 6, 4, 3],
                                       [7, 6, 3, 2], [7, 6, 2, 1], [7, 6, 1, 0]], True),
                         'There are missing jumpes for the black player')
        self.assertEqual(avail_white, ([[0, 7, 3, 4], [0, 7, 4, 3], [0, 7, 5, 2], [7, 0, 5, 2]], True),
                         'There are missing jumpes for the white player')
        # check all the moves
        board = [
            [None, {'color': 'black', 'SN': 1, 'king': False}, None, None, None, None, None, {'color': 'white', 'SN': 3, 'king': True}],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [{'color': 'white', 'SN': 8, 'king': False}, None, None, None, None, None, {'color': 'black', 'SN': 5, 'king': True}, None],
        ]
        avail_black = checkers.avail_moves(board, "black")
        avail_white = checkers.avail_moves(board, "white")
        self.assertEqual(avail_black, ([[0, 1, 1, 2], [0, 1, 1, 0], [7, 6, 6, 7],
                                        [7, 6, 6, 5], [7, 6, 5, 4], [7, 6, 4, 3], [7, 6, 3, 2], [7, 6, 2, 1], [7, 6, 1, 0]], False),
                         'There are missing moves for the black player')
        self.assertEqual(avail_white, ([[0, 7, 1, 6], [0, 7, 2, 5], [0, 7, 3, 4], [0, 7, 4, 3], [0, 7, 5, 2], [0, 7, 6, 1], [7, 0, 6, 1]], False),
                         'There are missing moves for the white player')

    def test_can_jump(self):
        # check if get available jump
        print('can jump now testing in checkers...')
        board = [
            [None, {'color':'black', 'SN':1, 'king':False}, None, None, None, None, None, {'color':'white', 'SN':3, 'king':True}],
            [None, None, {'color':'white', 'SN':2, 'king':False}, None, None, None, None, None],
            [None, None, None, None, None, {'color':'black', 'SN':4, 'king':False}, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, {'color':'black', 'SN':7, 'king':False}, None, None, None, {'color':'white', 'SN':6, 'king':True}, None, None],
            [{'color':'white', 'SN':8, 'king':False}, None, None, None, None, None, {'color':'black', 'SN':5, 'king':True}, None],
        ]
        self.assertEquals(checkers.can_jump([0, 1], [2, 3], board, [1, 2]), True, 'return False on correct jump of simple black')
        self.assertEquals(checkers.can_jump([7, 0], [5, 2], board, [6, 1]), True, 'return False on correct jump of simple white')
        self.assertEquals(checkers.can_jump([0, 7], [3, 4], board), True, 'return False on correct jump of king white')
        self.assertEquals(checkers.can_jump([7, 6], [4, 3], board), True, 'return False on correct jump of king black')

    def test_can_move(self):
        # check if get move
        print('can move now testing in checkers...')
        board = [
            [None, {'color':'black', 'SN':1, 'king':False}, None, None, None, None, None, {'color':'white', 'SN':2, 'king':True}],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [{'color':'white', 'SN':4, 'king':False}, None, None, None, None, None, {'color':'black', 'SN':3, 'king':True}, None],
        ]
        self.assertEquals(checkers.can_move([0, 1], [1, 2], board), True, 'return False on correct move of simple black')
        self.assertEquals(checkers.can_move([7, 0], [6, 1], board), True, 'return False on correct move of simple white')
        self.assertEquals(checkers.can_move([0, 7], [4, 3], board), True, 'return False on correct move of king white')
        self.assertEquals(checkers.can_move([7, 6], [4, 3], board), True, 'return False on correct move of king white')

    def test_make_move(self):
        # check if make move correctly
        print('make move now testing in checkers...')
        board = [
            [None, None, None, None, None, None, None, None],
            [{'color':'white', 'SN':1, 'king':False}, None, None, None, None, None, None, None],
            [None, None, None, {'color':'black', 'SN':3, 'king':False}, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, {'color':'white', 'SN':4, 'king':False}, None, None, None, None, None],
            [None, {'color':'black', 'SN':2, 'king':False}, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        new_board = checkers.make_move([1, 0], [0, 1], board)
        new_board = checkers.make_move([6, 1], [7, 0], new_board)
        self.assertEquals(new_board[0][1], {'color':'white', 'SN':1, 'king':True}, 'the piece dosnt move to new position')
        self.assertEquals(new_board[1][0], None, 'the piece dosnt remove from old position')
        self.assertEquals(new_board[0][1]['king'], True, 'the white king dosnt create')
        self.assertEquals(new_board[7][0]['king'], True, 'the black king dosnt create')

    def test_count_pieces(self):
        # check if counter players correctly
        print('counter of pieces now testing in checkers...')
        board = [
            [None, None, None, None, None, None, None, None],
            [{'color': 'white', 'SN': 1, 'king': False}, None, None, None, None, None, None, None],
            [None, None, None, {'color': 'black', 'SN': 3, 'king': False}, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, {'color': 'white', 'SN': 4, 'king': False}, None, None, None, None, None],
            [None, {'color': 'black', 'SN': 2, 'king': False}, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        self.assertEquals(checkers.count_pieces(board), (2,2), 'counter of players not done correctly')

    def test_end_turn(self):
        # check if replace player correctly
        print('end turn now testing in checkers...')
        checkers.turn = 'white'
        checkers.end_turn()
        if checkers.turn == 'black': test = True
        else: test = False
        self.assertEquals(test, True, 'change of turn not done correctly' )

    def test_player_check(self):
        # check if get players correctly
        print('player check now testing in checkers...')
        player1 = checkers.new_player('human', 'black', 'minimax', 6)
        player2 = checkers.new_player('cpu', 'white', 'minimax', 6)
        player1Expected = checkers.new_player('cpu', 'black', 'minimax', 6)
        player2Expected = checkers.new_player('human', 'white', 'minimax', 6)
        checkers.player_check(player1, player2)
        self.assertEqual(player1['type'] == player1Expected['type'], True,
                         'type of black player not change correctly')
        self.assertEqual(player2['type'] == player2Expected['type'], True,
                         'type of white player not change correctly')


# unit test for ladder and snakes
class TestLaddersAndSnakes(unittest.TestCase):

    def test_new_player(self):
        # check if arguments 'answers' and 'questions' are rest
        print('new player now testing in ladders and snakes...')
        player = laddersandsnakes.new_player()
        self.assertEqual(player['get_questions'](), 0, 'questions is not reseted to zero in ladders and snakes')
        self.assertEqual(player['get_answers'](), 0, 'answers is not reseted to zero in ladders and snakes')

    def test_Cube(self):
        # check if cube in range
        print('cube now testing in ladders and snakes...')
        check=laddersandsnakes.Cube(1) in range(1,7)
        self.assertEqual(check, True, 'cube out of range 1-6')

    def test_move(self):
        # check if the new position is correct
        print('move now testing in ladders and snakes...')
        self.assertEqual(laddersandsnakes.move(2,5), (laddersandsnakes.col[7%10], laddersandsnakes.row[7//10+1], 7), 'location is not correct')

    def test_check_move(self):
        # check if the new position is snake or ladder
        print('check move now testing in ladders and snakes...')
        check1 = laddersandsnakes.check_move(5,1)
        self.assertEqual(check1[2], 5, 'there are no snake or ladder -> displacement should not be')



# unit test for tools
class TestTools(unittest.TestCase):

    def test_read_from_xl(self):
        # check if read from xl correctly
        print('read from xl now testing in tools...')
        test = [['May', 'Hagbi', 'age 8-12', 12, 9, 'Ladders And Snakes', 'Math']]
        self.assertEqual(tools.read_from_xl('XL_for_testing.xlsx'), test, 'reading from xl not done correctly')

    def test_write_to_xl(self):
        # check if write to xl correctly
        print('write to xl now testing in tools...')
        list = [['Yoni', 'Cohen', 'age 6-8', 12, 10, 'Ladders And Snakes', 'Math']]
        tools.write_to_xl('File_Test.xlsx', list)
        self.assertEqual(tools.read_from_xl('File_Test.xlsx'), list, 'writing to xl not done correctly')

    def test_avg_per_age(self):
        # check if calculate average per age correctly
        print('average per age now testing in tools...')
        DB = [['May', 'Hagbi', 'age 8-12', 12, 9, 'Ladders And Snakes', 'Math']]
        self.assertEqual(tools.avg_per_age('6-8', 'Ladders And Snakes', DB), 0, 'average calculation per age not done correctly')
        self.assertEqual(tools.avg_per_age('8-12', 'Ladders And Snakes', DB), 75.00, 'average calculation per age not done correctly')

    def test_avg_per_game(self):
        # check if calculate average per game correctly
        print('average per game now testing in tools...')
        DB = [['May', 'Hagbi', 'age 8-12', 10, 7, 'Ladders And Snakes', 'Math'],
              ['Yoni', 'Cohen', 'age 6-8', 12, 10, 'Ladders And Snakes', 'Math']]
        self.assertEqual(tools.avg_per_game('Checkers', DB), 0, 'average calculation per game not done correctly')
        self.assertEqual(tools.avg_per_game('Ladders And Snakes', DB), 76.50, 'average calculation per game not done correctly')

    def test_grade_one_game(self):
        # check if calculate grade of kid correctly
        print('grade of one game now testing in tools...')
        kid_data_list = ['Yoni', 'Cohen', 'age 6-8', 12, 10, 'Checkers', 'Land of Israel']
        self.assertEqual(tools.grade_one_game(kid_data_list), 83, 'calculation of grade not done correctly')

    def test_find_kid_games(self):
        # check if fond kid in the list correctly
        print('find kid games now testing in tools...')
        DB = [['May', 'Hagbi', 'age 8-12', 10, 7, 'Ladders And Snakes', 'Math'],
              ['Yoni', 'Cohen', 'age 6-8', 12, 10, 'Ladders And Snakes', 'Math']]
        kid_data_game1 = [['May', 'Hagbi', 'age 8-12', 10, 7, 'Ladders And Snakes', 'Math']]
        kid_data_game2 = [['Yoni', 'Cohen', 'age 6-8', 12, 10, 'Ladders And Snakes', 'Math']]
        self.assertEqual(tools.find_kid_games('May', 'Hagbi', DB), kid_data_game1, 'Finding a kid not done correctly')
        self.assertEqual(tools.find_kid_games('Yoni', 'Cohen', DB), kid_data_game2, 'Finding a kid not done correctly')
        self.assertEqual(tools.find_kid_games('May', 'Cohen', DB), [], 'Finding a kid not done correctly')



















