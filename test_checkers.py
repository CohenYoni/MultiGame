import unittest
import checkers
import pygame

class TestChecker(unittest.TestCase):

    def test_piece(self):
        print ('get piece now testing...')
        self.assertEquals(checkers.piece('black', 3, False), {'color': 'black', 'SN': 3, 'king': False}, 'simple piece not created correctly')
        self.assertEquals(checkers.piece('white', 2, True), {'color': 'white', 'SN': 2, 'king': True}, 'king piece not created correctly')


    def test_init_board(self):
        print('initial board now testing...')
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

    def test_can_jump(self):
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

