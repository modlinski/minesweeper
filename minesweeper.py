"""
brief: Main module for saper game.
"""
import random


class Saper(object):
    """
    Game object for saper.
    """

    @staticmethod
    def empty_board():
        empty_board = []
        for row in xrange(10):
            row = []
            for field in xrange(10):
                row.append({'val': 0, 'display': '#'})
            empty_board.append(row)
        return empty_board

    @staticmethod
    def set_mines(number, board):
        # size = len(empty_board[0])
        lista = []
        for x in xrange(1, len(board[0])-1):
            for y in xrange(1, len(board[0])-1):
                field = {'x': x, 'y': y}
                lista.append(field)

        for i in xrange(number):
            mine_field = random.choice(lista)
            selected_row = mine_field['x']
            selected_field = mine_field['y']
            board[selected_row][selected_field] = {'val': 1, 'display': '#'}
            lista.remove(mine_field)
        return board

    @staticmethod
    def display_user_board(board):

        # print '--------------SAPER--------------'
        # user_board = []
        # for raw in board[1: len(board[0])-1]:
        #     user_row = []
        #     for field in raw[1: len(board[0])-1]:
        #         user_row.append(field['display'])
        #     user_board.append(user_row)
        # for raw in user_board:
        #     print raw
        # print '--------------SAPER--------------'
        print '--------------SAPER--------------'
        for raw in board[1: len(board[0]) - 1]:
            print [x['display'] for x in raw]
        print '--------------SAPER--------------'


    @staticmethod
    def display_mines_board(empty_board):

        user_board = []
        for raw in empty_board:
            user_row = []
            for field in raw:
                user_row.append(field['val'])
            user_board.append(user_row)
        for raw in user_board:
            print raw

    @staticmethod
    def check_board(x, y, board):

        checked_board = board

        # can be useful

        checked_board[x-1][y+1]['x'] = x-1
        checked_board[x-1][y+1]['y'] = y+1
        checked_board[x-1][y]['x'] = x-1
        checked_board[x-1][y]['y'] = y
        checked_board[x-1][y-1]['x'] = x-1
        checked_board[x-1][y-1]['y'] = y-1
        checked_board[x][y-1]['x'] = x
        checked_board[x][y-1]['y'] = y-1
        checked_board[x][y+1]['x'] = x
        checked_board[x][y+1]['y'] = y+1
        checked_board[x+1][y+1]['x'] = x+1
        checked_board[x+1][y+1]['y'] = y+1
        checked_board[x+1][y]['x'] = x+1
        checked_board[x+1][y]['y'] = y
        checked_board[x+1][y-1]['x'] = x+1
        checked_board[x+1][y-1]['y'] = y-1

        around = [checked_board[x-1][y+1],
                  checked_board[x-1][y],
                  checked_board[x-1][y-1],
                  checked_board[x][y-1],
                  checked_board[x][y+1],
                  checked_board[x+1][y+1],
                  checked_board[x+1][y],
                  checked_board[x+1][y-1]]

        around_values = [checked_board[x-1][y+1]['val'],
                         checked_board[x-1][y]['val'],
                         checked_board[x-1][y-1]['val'],
                         checked_board[x][y-1]['val'],
                         checked_board[x][y+1]['val'],
                         checked_board[x+1][y+1]['val'],
                         checked_board[x+1][y]['val'],
                         checked_board[x+1][y-1]['val']]
        # print around
        if around_values.count(1) == 0:
            checked_board[x][y]['display'] = 'e'
            for field in around:
                # print field
                if field['val'] == 0:
                    checked_board[field['x']][field['y']]['display'] = 'e'
                    # self.check_board(x, y, board)
                # else:
                #     pass

        else:
            checked_board[x][y]['display'] = str(around_values.count(1))
        return checked_board

    def click(self, x, y, board):

        if board[x][y]['val'] == 0:
            board = self.check_board(x, y, board)
        if board[x][y]['val'] == 1:
            self.display_mines_board(board)
            print
            print 'You lost!'

    def game(self):
        board = self.empty_board()
        board_mines = self.set_mines(10, board)
        for i in xrange(15):
            self.display_user_board(board_mines)
            x = int(raw_input('Choose x: '))
            y = int(raw_input('Choose y: '))
            self.click(x, y, board_mines)

saper = Saper()
saper.game()
